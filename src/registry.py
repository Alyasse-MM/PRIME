# Dynamically import all exercise classes from the exercises directory and
# register them in grades specific registries.

import importlib
import inspect
from pathlib import Path
import streamlit as st
from exercises.base_exercise import BaseExercise

def get_exercises_from_folder(path: str) -> dict:
    """
    Imports all exercise classes from the specified directory and organizes them into a registry grouped by chapter.

    Args:
        path (str): The path to the directory containing exercise files.

    Returns:
        dict: A dictionary of exercises grouped by chapter.
    """

    exercises_dict = {}
    exercises_path = Path(path)

    if not Path(path).is_absolute():
        exercises_path = (Path(__file__).parent / path).resolve()
    else:
        exercises_path = Path(path).resolve()
    if not exercises_path.exists():
        st.error(f"Folder not found: {exercises_path}")
        return exercises_dict

    for file_path in exercises_path.rglob("*.py"):
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

        chap_titles = getattr(module, "CHAPTER", {"fr": "Other", "en": "Other"})
        chap = chap_titles["en"]
        if chap not in exercises_dict:
            exercises_dict[chap] = {"title": chap_titles, "exercises": []}

        for obj in vars(module).values():
            if inspect.isclass(obj) and issubclass(obj, BaseExercise) and obj is not BaseExercise:
                if obj.__module__ == module_name:
                    exercises_dict[chap]["exercises"].append(obj)
    return exercises_dict

def get_exercises_from_folders(paths : list[str]) -> dict:
    """
    Imports all exercise classes from the specified directories and organizes them into a registry grouped by chapter.

    Args:
        paths (list[str]): A list of paths to the directories containing exercise files.

    Returns:
        dict: A dictionary of exercises grouped by chapter.
    """

    exercises_dict = {}
    for path in paths:
        grade_exercises = get_exercises_from_folder(path)
        for chap_title, chap_data in grade_exercises.items():
            if chap_title not in exercises_dict:
                exercises_dict[chap_title] = chap_data
            else:
                chap_title = chap_title+" (Duplicate)"
                chap_data["title"]["en"] = chap_data["title"]["en"] + " (Duplicate)"
                chap_data["title"]["fr"] = chap_data["title"]["fr"] + " (Duplicata)"
                exercises_dict[chap_title] = chap_data
    return exercises_dict