import streamlit as st

def render_grade_page(grade: str, registry: list):
    """
    Renders the page for a specific grade.

    Args:
        grade (str): The grade to render the page for.
        registry (list): The list of exercises for the grade.
    """

    st.set_page_config(page_title=f"PRIME - {grade.capitalize()}", layout="centered")

    if "page" not in st.session_state:
        st.session_state.page = grade

    st.title(f"{grade.capitalize()}")
    if st.session_state.lang == "fr":
        st.info("Pas encore implémenté")
    else:
        st.info("Not implemented yet")