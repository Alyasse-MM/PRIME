# Dynamically import all exercise classes from the exercises directory and
# register them in grades specific registries.

import importlib
import inspect
from pathlib import Path
import streamlit as st

from exercises.base_exercise import BaseExercise

EXERCISE_REGISTRY_SECONDE = {}
EXERCISE_REGISTRY_PREMIERE = {}
EXERCISE_REGISTRY_TERMINALE = {}

grades = {
    "seconde": EXERCISE_REGISTRY_SECONDE,
    "premiere": EXERCISE_REGISTRY_PREMIERE,
    "terminale": EXERCISE_REGISTRY_TERMINALE
}

current_dir = Path(__file__).parent

for folder_name, target_dict in grades.items():
    exercises_dir = current_dir / "exercises" / folder_name

    if not exercises_dir.exists():
        continue

    for file_path in exercises_dir.rglob("*.py"):
        if file_path.name == "__init__.py":
            continue

        relative_path = file_path.relative_to(current_dir)
        module_name = ".".join(relative_path.with_suffix("").parts)

        try:
            module = importlib.import_module(module_name)
        except Exception as e:
            print(f"Erreur lors du chargement de {module_name}: {e}")
            continue

        chap_fr = getattr(module, "CHAPTER_FR", "Autre")
        chap_en = getattr(module, "CHAPTER_EN", "Other")

        if chap_fr not in target_dict:
            if st.session_state.lang == "fr":
                target_dict[chap_fr] = []
            else:
                target_dict[chap_en] = []

        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseExercise) and obj is not BaseExercise:
                if obj.__module__ == module_name:
                    target_dict[chap_fr].append(obj)