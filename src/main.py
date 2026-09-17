import streamlit as st

if "lang" not in st.session_state:
    st.session_state.lang = "fr"

st.sidebar.title("PRIME")
st.sidebar.markdown("*(Python Randomized Interactive Math Exercises)*")

repo_url = "https://github.com/Alyasse-MM/PRIME"
badge_markdown = f"[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717.svg?style=for-the-badge&logo=github)]({repo_url})"

st.sidebar.markdown(badge_markdown)

toggle_label = {"en": "Switch to English", "fr": "Passer en Français"}
if st.sidebar.button(toggle_label[st.session_state.lang]):
    st.session_state.lang = "en" if st.session_state.lang == "fr" else "fr"
    st.rerun()

st.sidebar.divider()

if st.session_state.lang == "fr":
    title_home = "Accueil"
    title_2nde = "Seconde"
    title_1ere = "Première"
    title_term = "Terminale"
else:
    title_home = "Home"
    title_2nde = "10th Grade"
    title_1ere = "11th Grade"
    title_term = "12th Grade"

page_home = st.Page("views/homepage.py", title=title_home)
page_seconde = st.Page("views/seconde.py", title=title_2nde)
page_premiere = st.Page("views/premiere.py", title=title_1ere)
page_terminale = st.Page("views/terminale.py", title=title_term)

pg = st.navigation([page_home, page_seconde, page_premiere, page_terminale])
pg.run()