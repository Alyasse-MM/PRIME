from registry import EXERCISE_REGISTRY_SECONDE
from views.render import render_grade_page
import streamlit as st

title = {"fr": "seconde", "en": "10th grade"}
render_grade_page(title[st.session_state.lang], EXERCISE_REGISTRY_SECONDE)