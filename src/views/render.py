from numpy import size
import streamlit as st
from exercises.base_exercise import BaseExercise

def render_grade_page(grade_title: str, registry: dict[str, list[type[BaseExercise]]]):
    """
    Renders the page for a specific grade.

    Args:
        grade (str): The grade to render the page for.
        registry (list): The list of exercises for the grade.
    """

    st.set_page_config(page_title=f"PRIME - {grade_title.capitalize()}", layout="centered")

    if "page" not in st.session_state:
        st.session_state.page = grade_title

    st.title(f"{grade_title.capitalize()}")
    if len(registry) == 0:
        if st.session_state.lang == "fr":
            st.info("Pas encore implémenté")
        else:
            st.info("Not implemented yet")
    else:
        for chapter, exercises in registry.items():
            with st.expander(f"{chapter} ({len(exercises)} exercices)", expanded=False):
                for exercise_class in exercises:
                    if st.session_state.lang == "fr":
                        st.write(exercise_class.lang_fr)
                    else:
                        st.write(exercise_class.lang_en)