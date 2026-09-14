from registry import EXERCISE_REGISTRY_SECONDE
from views.render import render_grade_page
import streamlit as st

title = "seconde" if st.session_state.lang == "fr" else "10th grade"

render_grade_page(title, EXERCISE_REGISTRY_SECONDE)