from registry import get_exercises_from_folder
from views.render import render_grade_page
import streamlit as st

title = {"fr": "terminale", "en": "12th grade"}
path = "exercises/terminale"
render_grade_page(title, get_exercises_from_folder(path))