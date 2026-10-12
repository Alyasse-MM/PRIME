from enum import Enum, auto
from pathlib import Path

import streamlit as st

from model.StudyPlan import StudyPlan
from exercises.base_exercise import BaseExercise

class State(Enum):
    HOME = auto()
    STUDYPLAN = auto()
    MODULE = auto()
    EXERCISE = auto()

class Controller:
    def __init__(self):
        if "lang" not in st.session_state:
            st.session_state.lang = "fr"
        self.lang = st.session_state.lang
        
        if "app_state" not in st.session_state:
            st.session_state.app_state = State.HOME

        if "current_studyplan" not in st.session_state:
            st.session_state.current_studyplan = None
        
        if "current_studyplan_metadata" not in st.session_state:
            st.session_state.current_studyplan_metadata = self.get_homepage_metadata()
            
        if "current_module" not in st.session_state:
            st.session_state.current_module = None
            
        if "current_exercise" not in st.session_state:
            st.session_state.current_exercise = None

        if "cached_exercises_list" not in st.session_state:
            st.session_state.cached_exercises_list = None

    def get_homepage_metadata(self) -> dict[str,dict[str,str]]:
        result = StudyPlan.get_homepage_metadata()
        return result

    def get_current_studyplan_key(self) -> str:
        return st.session_state.current_studyplan_metadata["key"]
    
    def get_current_studyplan_names(self) -> dict[str,str]:
        return st.session_state.current_studyplan_metadata["names"]
    
    def get_current_studyplan_description(self) -> dict[str,str]:
        return st.session_state.current_studyplan_metadata["descriptions"]
    
    def get_current_language(self) -> str:
        """
        Returns:
            str: The current app language as a two character string."""
        return st.session_state.lang
    def switch_language(self):
        """
        Switch the app language.

        To French if English was the current one, to English if French was the current one.
        """
        st.session_state.lang = "en" if self.lang == "fr" else "fr"

    def get_app_state(self) -> State:
        """
        Returns:
            State: The current app state.
        """
        return st.session_state.app_state
    def set_app_state(self, new_state: State):
        """
        Changes the current app state
        
        Args:
            new_state (State): The new app state."""
        st.session_state.app_state = new_state

    def get_current_studyplan_metadata(self) -> dict[str,dict,dict]:
        """
        Returns:
            dict[srt,dict,dict]: The key, names, and description of the currently selected module`
        """
        return st.session_state.current_studyplan_metadata
    def set_current_studyplan_metadata(self, new_metadata: dict[str,dict,dict]):
        """
        Changes the current studyplan's metadata
        
        Args:
            new_metadata (dict[str,dict,dict]): The key, names, and descriptions of the new selected module.
        """
        st.session_state.current_studyplan_metadata = new_metadata
    
    def get_current_module(self) -> str:
        """
        Returns:
            str: The name of the currently selected module.
        """
        return st.session_state.current_module
    def set_current_module(self, new_module: str):
        """
        Changes the current module
        
        Args:
            new_module (str): The name of the new selected module.
        """
        st.session_state.current_module = new_module
    
    def get_current_exercise(self) -> BaseExercise:
        """
        Returns:
            BaseExercise subclass: the currently selected exercise class. 
        """
        return st.session_state.current_exercise
    def set_current_exercise(self, new_exercise: BaseExercise):
        """Changes the current exercise.

        Args:
            new_exercise (BaseExercise subclass): The new exercise class to use.
        """
        st.session_state.current_exercise = new_exercise

    def get_cached_exercises_list(self) -> dict:
        """
        Returns:
            dict: the currently selected studyplan's dictionary of exercises grouped by module.
        """
        return st.session_state.cached_exercises_list if st.session_state.cached_exercises_list else None

    def switch_page_context(self, module_metadata: dict[str, str, str]):
        """
        Sets the current studyplan state parameters and resets navigation paths.
        
        Args:
            module_metadata (dict[str, str, str]): The key, names, and descriptions of the newly selected module.
        """
        if st.session_state.current_studyplan_metadata != module_metadata:
            st.session_state.current_studyplan_metadata = module_metadata
            st.session_state.current_module = None
            st.session_state.current_exercise = None

            if module_metadata["key"] == "accueil":
                st.session_state.app_state = State.HOME
                st.session_state.current_studyplan = None
                self.set_current_studyplan_metadata(self.get_homepage_metadata())
                st.session_state.cached_exercises_list = None
            else:
                st.session_state.app_state = State.STUDYPLAN
                st.session_state.current_studyplan = StudyPlan.create(f"../exercises/{module_metadata["key"]}")
                checked_path=st.session_state.current_studyplan.get_path()
                self.set_current_studyplan_metadata(module_metadata)
                st.session_state.cached_exercises_list = StudyPlan.get_exercises_from_folder(checked_path)

    def get_modules_list(self) -> list[dict[str,str,str]]:
        study_plans = []
        default_module_repertory = StudyPlan.get_checked_path(Path("../exercises"))
        for entry in default_module_repertory.rglob("**"):
            if entry.is_dir():
                module_key, module_names, module_descriptions = StudyPlan.get_metadata(entry)
                if module_key is not None and module_names is not None:
                    study_plans.append({"key":module_key, "names":module_names, "descriptions":module_descriptions})
        return study_plans