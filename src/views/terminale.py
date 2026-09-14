from registry import EXERCISE_REGISTRY_TERMINALE
from views.render import render_grade_page
import streamlit as st

title = "terminale" if st.session_state.lang == "fr" else "12th grade"
render_grade_page(title, EXERCISE_REGISTRY_TERMINALE)