from registry import EXERCISE_REGISTRY_PREMIERE
from views.render import render_grade_page
import streamlit as st

title = "premiere" if st.session_state.lang == "fr" else "11th grade"
render_grade_page(title, EXERCISE_REGISTRY_PREMIERE)