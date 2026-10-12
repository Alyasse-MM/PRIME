import json
import importlib
import inspect
from pathlib import Path

import streamlit as st

from exercises.base_exercise import BaseExercise

class StudyPlan:
    def __init__(self, path: Path, key: str, names: dict, descriptions: dict):
        self.path = path
        self.key = key
        self.names = names
        self.descriptions = descriptions
        self.data = StudyPlan.get_exercises_from_folder(path)

    @st.cache_data
    @staticmethod
    def get_checked_path(path) -> None | Path:
        """
        Resolves relative or absolute paths against the current file's directory.
        Verifies that the target path exists and is actually a directory.
        """
        raw_path = Path(path)

        if raw_path.is_absolute():
            checked_path = raw_path.resolve()
        else:
            checked_path = (Path(__file__).parent / raw_path).resolve()

        if not checked_path.exists() or not checked_path.is_dir():
            return None

        return checked_path

    @st.cache_data
    @staticmethod
    def get_metadata(module_path : Path) -> tuple[str, dict, dict] | tuple[None, None, None]:
        """
        Load a study plan's metadata from a json file in `module_path`.
        Returns (name, description) or (None, None) if the file doesn't exist or is malformed.
        """

        json_path = module_path / "metadata.json"
        
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
            if not isinstance(json_data, dict):
                json_data = {}
        except (FileNotFoundError, json.JSONDecodeError):
            return None, None, None

        key = json_data.get("key", str(module_path))
        name = json_data.get("name", {"fr": "Programme", "en": "Study plan"})
        description = json_data.get("description", {"fr": "Un assortiment d'exercises", "en": "A set of exercises"})
        return key, name, description

    @st.cache_data
    @staticmethod
    def get_homepage_metadata() -> dict[str,dict[str,str]]:
        return {"key":"accueil",
                "names":{"fr":"Accueil","en":"Homepage",},
                "descriptions":{"fr":"Bienvenue sur PRIME","en":"Welcome on PRIME"}}

    @classmethod
    def create(cls, path: str) -> StudyPlan:
        """Factory method to safely instantiate the class."""
        checked_path = cls.get_checked_path(path)
        
        if checked_path is None:
            return None

        key, names, descriptions = cls.get_metadata(checked_path)
        if (key, names,descriptions)==(None, None,None):
            return None
            
        return cls(checked_path, key, names, descriptions)

    @st.cache_resource
    @staticmethod
    def get_exercises_from_folder(module_path: Path) -> dict:
        """
        Imports all exercise classes from the specified directory and organizes them into a registry grouped by module.

        Args:
            path (str): The path to the directory containing exercise files.

        Returns:
            dict: A dictionary of exercises grouped by module.
        """

        exercises_dict = {}

        for file_path in module_path.rglob("*.py"):
            if file_path.name == "__init__.py":
                continue

            try:
                abs_file_path = Path(file_path).resolve()
                module_name = abs_file_path.stem
                spec = importlib.util.spec_from_file_location(module_name, abs_file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            except Exception as e:
                print(f"Error while loading {module_name}: {e}")
                continue

            module_titles = getattr(module, "MODULE", {"fr": "Other", "en": "Other"})
            module_key = module_titles["en"]
            if module_key not in exercises_dict:
                exercises_dict[module_key] = {"title": module_titles, "exercises": []}

            for obj in vars(module).values():
                if inspect.isclass(obj) and issubclass(obj, BaseExercise) and obj is not BaseExercise:
                    if obj.__module__ == module_name:
                        exercises_dict[module_key]["exercises"].append(obj)
        return exercises_dict

    @staticmethod
    def get_exercises_from_folders(paths : list[str]) -> dict:
        """
        Imports all exercise classes from the specified directories and organizes them into a registry grouped by module.

        Args:
            paths (list[str]): A list of paths to the directories containing exercise files.

        Returns:
            dict: A dictionary of exercises grouped by module.
        """

        exercises_dict = {}
        for path in paths:
            studyplan_exercises = StudyPlan.get_exercises_from_folder(path)
            for module_title, module_data in studyplan_exercises.items():
                if module_title not in exercises_dict:
                    exercises_dict[module_title] = module_data
                else:
                    module_title = module_title+" (Duplicate)"
                    module_data["title"]["en"] = module_data["title"]["en"] + " (Duplicate)"
                    module_data["title"]["fr"] = module_data["title"]["fr"] + " (Duplicata)"
                    exercises_dict[module_title] = module_data
        return exercises_dict

    @staticmethod
    def to_list(exercises_dict: dict) -> list:
        """
        Convert the exercises dictionary to a list of tuples "exercise_class, module_title".

        Args:
            exercises_dict (dict): A dictionary of exercises grouped by module.

        Returns:
            list: A list of tuples (exercise_class, module_title).
        """
        exercises_list = []
        for module_title, module_data in exercises_dict.items():
            for exercise_class in module_data["exercises"]:
                exercises_list.append((exercise_class, module_title))

                
        return exercises_list

    def get_path(self) -> Path:
        return self.path

    def get_names(self) -> dict:
        return self.names

    def get_descriptions(self) -> dict:
        return self.descriptions

    def get_data(self) -> dict:
        return self.data