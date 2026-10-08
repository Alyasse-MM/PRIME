from enum import Enum, auto

import streamlit as st

from registry import get_exercises_from_folder
from exercises.base_exercise import BaseExercise

class State(Enum):
    HOME = auto()
    GRADE = auto()
    CHAPTER = auto()
    EXERCISE = auto()

class Controller:
    def __init__(self):
        if "lang" not in st.session_state:
            st.session_state.lang = "fr"
        self.lang = st.session_state.lang
        
        if "app_state" not in st.session_state:
            st.session_state.app_state = State.HOME
            
        if "current_grade_key" not in st.session_state:
            st.session_state.current_grade_key = "accueil"
            
        if "current_chapter" not in st.session_state:
            st.session_state.current_chapter = None
            
        if "current_exercise" not in st.session_state:
            st.session_state.current_exercise = None

        if "cached_exercises_list" not in st.session_state:
            st.session_state.cached_exercises_list = None

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

    def get_current_grade_key(self) -> str:
        """
        Returns:
            str: The name of the currently selected chapter or `accueil`
        """
        return st.session_state.current_grade_key
    def set_current_grade_key(self, new_grade_key: str):
        """
        Changes the current grade
        
        Args:
            new_grade_key (str): The name of the new selected grade.
        """
        st.session_state.curreng_grade_key = new_grade_key
    
    def get_current_chapter(self) -> str:
        """
        Returns:
            str: The name of the currently selected chapter.
        """
        return st.session_state.current_chapter
    def set_current_chapter(self, new_chapter: str):
        """
        Changes the current chapter
        
        Args:
            new_chapter (str): The name of the new selected chapter.
        """
        st.session_state.current_chapter = new_chapter
    
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
            dict: the currently selected grade's dictionary of exercises grouped by chapter.
        """
        return st.session_state.cached_exercises_list if st.session_state.cached_exercises_list else None

    def switch_page_context(self, grade_key: str):
        """
        Sets the current grade key to `grade_key` and both `current_chapter` and `current_exercise` to None.  
        If `grade_key == accueil`, then `st.session_state.app_state` is set to `State.HOME` and `cached_exercises_list` is set to `None`  
        Otherwise, `st.session_state.app_state` is set to `State.GRADE` and the selected grade's exercises list is loaded in `cached_exercises_list`.
        
        Args:
            grade_key (str): The name of the newly selected grade.
        """
        if st.session_state.current_grade_key != grade_key:
            st.session_state.current_grade_key = grade_key
            st.session_state.current_chapter = None
            st.session_state.current_exercise = None

            if grade_key == "accueil":
                st.session_state.app_state = State.HOME
                st.session_state.cached_exercises_list = None
            else:
                st.session_state.app_state = State.GRADE
                st.session_state.cached_exercises_list = get_exercises_from_folder(f"exercises/{grade_key}")
