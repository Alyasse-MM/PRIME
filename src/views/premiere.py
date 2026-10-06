from registry import get_exercises_from_folder
from views.render import render_grade_page
import streamlit as st

title = {"fr": "premiere", "en": "11th grade"}
path = "exercises/premiere"
render_grade_page(title, get_exercises_from_folder(path))