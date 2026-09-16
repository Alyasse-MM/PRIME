import streamlit as st

st.set_page_config(page_title="PRIME - Homepage", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "homepage"

title = {"fr": "Accueil", "en": "Homepage"}
st.title(title[st.session_state.lang])