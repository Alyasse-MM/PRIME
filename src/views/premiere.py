from registry import EXERCISE_REGISTRY_PREMIERE
from views.render import render_grade_page
import streamlit as st

title = {"fr": "premiere", "en": "11th grade"}
render_grade_page(title[st.session_state.lang], EXERCISE_REGISTRY_PREMIERE)