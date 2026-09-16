from registry import EXERCISE_REGISTRY_TERMINALE
from views.render import render_grade_page
import streamlit as st

title = {"fr": "terminale", "en": "12th grade"}
render_grade_page(title[st.session_state.lang], EXERCISE_REGISTRY_TERMINALE)