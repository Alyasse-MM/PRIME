# Dynamically import all exercise classes from the exercises directory and
# register them in grades specific registries.

import importlib
import inspect
from pathlib import Path
import streamlit as st
from exercises.base_exercise import BaseExercise

def registry(path: str) -> dict:
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