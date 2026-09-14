import streamlit as st

st.set_page_config(page_title="PRIME - Homepage", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "homepage"

if st.session_state.lang == "fr":
    st.title("Bienvenue sur PRIME")
else:
    st.title("Welcome to PRIME !")