# Dynamically import all exercise classes from the exercises directory and
# register them in EXERCISE_REGISTRY.

import importlib
import inspect
from pathlib import Path

from exercises.base_exercise import BaseExercise

EXERCISE_REGISTRY = []

current_dir = Path(__file__).parent
exercises_dir = current_dir / "exercises"

for file_path in exercises_dir.rglob("*.py"):
    if file_path.name == "__init__.py":
        continue

    relative_path = file_path.relative_to(current_dir.parent)
    module_name = ".".join(relative_path.with_suffix("").parts)

    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        print(f"Erreur lors du chargement de {module_name}: {e}")
        continue

    for name, obj in inspect.getmembers(module, inspect.isclass):
        if issubclass(obj, BaseExercise) and obj is not BaseExercise:
            if obj.__module__ == module_name:
                EXERCISE_REGISTRY.append(obj)