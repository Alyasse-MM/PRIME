import json
import importlib
import inspect
import random
from pathlib import Path

import streamlit as st

from exercises.base_exercise import BaseExercise

DEFAULT_STUDYPLAN_DIR = Path("../exercises")

class StudyPlan:
    def __init__(self, paths, key: str, names: dict, descriptions: dict):
        self.paths = paths
        self.key = key
        self.names = names
        self.descriptions = descriptions
        if isinstance(paths, list):
            self.data = StudyPlan.get_exercises_from_folders(paths)
        else:
            self.data = StudyPlan.get_exercises_from_folder(paths)

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
    def get_metadata(module_path : Path) -> tuple[str, dict, dict, None] | tuple[str, dict, dict, list] | tuple[None, None, None, None]:
        """
        Load a study plan's metadata from a json file in `module_path`.
        Args:
            module_path (Path): a path to a module's repository
        Returns:
            metadata (tuple(key, name, description, None)): if the given module is a standard one.
            metadada (tuple(key, name, description, includes)): if the given module is a dynamic one.
            metadata (tuple(None, None, None, None)): if an error was encountered while reading metadata.
        """

        json_path = module_path / "metadata.json"
        
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
            if not isinstance(json_data, dict):
                json_data = {}
        except (FileNotFoundError, json.JSONDecodeError):
            return None, None, None, None

        key = json_data.get("key", str(module_path))
        name = json_data.get("name", {"fr": "Programme", "en": "Study plan"})
        description = json_data.get("description", {"fr": "Un assortiment d'exercises", "en": "A set of exercises"})
        includes = json_data.get("includes", [])
        return key, name, description, includes

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

        key, names, descriptions, paths = cls.get_metadata(checked_path)
        if (key, names,descriptions, paths)==(None, None, None, None):
            return None
        if (len(paths)>0):
            checked_paths=[]
            for element in paths:
                checked_paths.append(cls.get_checked_path(DEFAULT_STUDYPLAN_DIR / element))
            return cls(checked_paths, key, names, descriptions)
        else:
            return cls(checked_path, key, names, descriptions)

    @st.cache_resource
    @staticmethod
    def get_exercises_from_folder(module_path: Path) -> dict:
        """
        Imports all exercise classes from the specified directory and organizes them into a registry grouped by module.

        Args:
            path (str): The path to the directory containing exercise files.

        Returns:
            data (dict): A dictionary of exercises grouped by module.
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

    @st.cache_resource
    @staticmethod
    def get_exercises_from_folders(paths : list[Path]) -> dict:
        """
        Imports all exercise classes from the specified directories and organizes them into a registry grouped by module.

        Args:
            paths (list[Path]): A list of paths to the directories containing the included study plans.

        Returns:
            data (dict): A dictionary of exercises grouped by module.
        """

        exercises_dict = {}
        for path in paths:
            studyplan_key,studyplan_names,_,_ = StudyPlan.get_metadata(path)
            studyplan_exercises = StudyPlan.get_exercises_from_folder(path)
            for module_title, module_data in studyplan_exercises.items():
                new_module_title = module_title+" ("+studyplan_key+")"
                new_module_data = module_data.copy()
                new_module_data["title"] = module_data["title"].copy()
                new_module_data["title"]["en"] = new_module_data["title"]["en"] + " (" + studyplan_names["en"] + ")"
                new_module_data["title"]["fr"] = new_module_data["title"]["fr"] + " (" + studyplan_names["fr"] + ")"
                exercises_dict[new_module_title] = new_module_data
        return exercises_dict

    @st.cache_resource
    @staticmethod
    def randomize_order(exercises_dict: dict, seed=int, part_size=15) -> dict:
        """
        Randomizes the order of exercises in `exercises_dict` in a new dictionary. 

        Args:
            exercises_dict (dict): A dictionary of exercises grouped by module.
            part_size (int): Maximum number of items per part.

        Returns:
            data (dict): A dictionnary of `exercise_class` divided in
            `n` parts of size `part_size` maximum.
        """
        exercises_list = []
        for module_data in exercises_dict.values():
            for exercise_class in module_data["exercises"]:
                exercises_list.append((exercise_class))

        random.Random(seed).shuffle(exercises_list)
        
        randomized_dict = {}
        
        for i in range(0, len(exercises_list), part_size):
            part_index = (i // part_size) + 1
            titles={"en":f"Part {part_index}","fr":f"Partie {part_index}"}
            randomized_dict[f"Part {part_index}"] = {}
            randomized_dict[f"Part {part_index}"]["title"] = titles
            randomized_dict[f"Part {part_index}"]["exercises"] = exercises_list[i : i + part_size]
            
        return randomized_dict

    def get_paths(self) -> Path:
        return self.paths

    def get_names(self) -> dict:
        return self.names

    def get_descriptions(self) -> dict:
        return self.descriptions

    def get_data(self) -> dict:
        return self.data

    def get_randomized_data(self,seed:int) -> dict:
        return StudyPlan.randomize_order(self.data,seed)

    def get_new_seed(self) -> int:
        return random.randint(100000,999999)