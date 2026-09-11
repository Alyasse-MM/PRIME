from registry import EXERCISE_REGISTRY
import streamlit as st

st.set_page_config(page_title="PRIME - Homepage", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "homepage"

st.sidebar.title("PRIME")
st.sidebar.markdown("*(Python Randomized, Interactive Math Exercises)*")
if st.sidebar.button("Accueil", type="primary"):
    st.session_state.page = "homepage"
if st.sidebar.button("Seconde", type="primary"):
    st.session_state.page = "seconde"
if st.sidebar.button("Première", type="primary"):
    st.session_state.page = "premiere"
if st.sidebar.button("Terminale", type="primary"):
    st.session_state.page = "terminale"

if st.session_state.page == "homepage":
    st.title("Bienvenue sur PRIME !")
elif st.session_state.page == "seconde":
    st.title("Seconde - $2^{nde}$")
    st.info("Not implemented yet")
elif st.session_state.page == "premiere":
    st.title("Première - $1^{ère}$")
    st.info("Not implemented yet")
elif st.session_state.page == "terminale":
    st.title("Terminale - $T^{le}$")
    st.info("Not implemented yet")