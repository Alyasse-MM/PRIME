import streamlit as st
import matplotlib.figure as Figure
from exercises.base_exercise import BaseExercise
from functools import partial
from enum import Enum, auto
from registry import get_exercises_from_folder

class Controller:
    class state(Enum):
        HOME = auto()
        GRADE = auto()
        CHAPTER = auto()
        EXERCISE = auto()

    def __init__(self):
        if "lang" not in st.session_state:
            st.session_state.lang = "fr"
        self.lang = st.session_state.lang
        
        if "app_state" not in st.session_state:
            st.session_state.app_state = self.state.HOME
            
        if "current_grade_key" not in st.session_state:
            st.session_state.current_grade_key = "accueil"
            
        if "current_chapter" not in st.session_state:
            st.session_state.current_chapter = None
            
        if "current_exercise" not in st.session_state:
            st.session_state.current_exercise = None

        if "cached_exercises_list" not in st.session_state:
            st.session_state.cached_exercises_list = None

        self.page_titles = {
            "accueil" : {"fr" : "Accueil", "en" : "Home"},
            "seconde" : {"fr" : "Seconde", "en" : "10th Grade"},
            "premiere" : {"fr" : "Première", "en" : "11th Grade"},
            "terminale" : {"fr" : "Terminale", "en" : "12th Grade"}
        }

    def switch_language(self):
        # The label is in the targeted language
        toggle_label = {"en": "Passer en Français", "fr": "Switch to English"}
        if st.sidebar.button(toggle_label[self.lang]):
            st.session_state.lang = "en" if self.lang == "fr" else "fr"
            st.rerun()

    def switch_page_context(self, grade_key: str):
        if st.session_state.current_grade_key != grade_key:
            st.session_state.current_grade_key = grade_key
            st.session_state.current_chapter = None
            st.session_state.current_exercise = None

            if grade_key == "accueil":
                st.session_state.app_state = self.state.HOME
                st.session_state.cached_exercises_list = None
            else:
                st.session_state.app_state = self.state.GRADE
                st.session_state.cached_exercises_list = get_exercises_from_folder(f"exercises/{grade_key}")

    def render_sidebar(self):
        st.sidebar.title("PRIME")
        st.sidebar.markdown("*(Python Randomized Interactive Math Exercises)*")

        repo_url = "https://github.com/Alyasse-MM/PRIME"
        badge_markdown = f"[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717.svg?style=for-the-badge&logo=github)]({repo_url})"
        st.sidebar.markdown(badge_markdown)

        self.switch_language()
        st.sidebar.divider()

        # Build dynamic pages pointing to unified instance methods
        page_home = st.Page(partial(self.switch_page_context, "accueil"), title=self.page_titles["accueil"][self.lang], url_path="accueil")
        page_sec  = st.Page(partial(self.switch_page_context, "seconde"), title=self.page_titles["seconde"][self.lang], url_path="seconde")
        page_prem = st.Page(partial(self.switch_page_context, "premiere"), title=self.page_titles["premiere"][self.lang], url_path="premiere")
        page_term = st.Page(partial(self.switch_page_context, "terminale"), title=self.page_titles["terminale"][self.lang], url_path="terminale")

        pg = st.navigation([page_home, page_sec, page_prem, page_term], position="sidebar")
        pg.run()

    def render_main(self):
        st.set_page_config(page_title="PRIME - Homepage", layout="centered")
        title = {"fr": "Accueil", "en": "Homepage"}
        st.title(title[self.lang])

    def render_content_block(self, items: list):
        """Iterates through a list of mixed media and renders them appropriately."""
        for item in items:
            if isinstance(item, str):
                st.markdown(item)
            elif isinstance(item, Figure.Figure):
                st.pyplot(item)    

    def render_exercise(self):
        ex = st.session_state.current_exercise
        if not ex:
            st.session_state.app_state = self.state.CHAPTER
            st.rerun()

        # Fix key path lookup names
        grade_key = st.session_state.current_grade_key
        st.header(self.page_titles[grade_key][self.lang].capitalize())
        st.title(f"{ex.title[self.lang]}")
        
        back_label = {"en": "⬅ Back to exercises", "fr": "⬅ Retour aux exercices"}
        if st.button(back_label[self.lang]):
            st.session_state.current_exercise = None
            st.session_state.app_state = self.state.CHAPTER
            st.rerun()

        st.divider()

        data = ex.get_data()
        st.subheader(data["title"][self.lang])
        st.caption(f"ID: {data['id']} | Seed: {data['seed']}")
        self.render_content_block(data["statement"][self.lang])

        for i, q in enumerate(data["questions"]):
            st.markdown(f"#### Question {i+1}")
            self.render_content_block(q[self.lang]['question'])
            
            with st.expander({"en": "Show Insight", "fr": "Voir l'indice"}[self.lang]):
                self.render_content_block(q[self.lang]['insight'])
            
            with st.expander({"en": "Show Solution", "fr": "Voir la solution"}[self.lang]):
                self.render_content_block(q[self.lang]['answer'])

    def render_exercise_selection(self):
        chapter_key = st.session_state.current_chapter
        chapter_data = st.session_state.cached_exercises_list.get(chapter_key) if st.session_state.cached_exercises_list else None

        if not chapter_data:
            st.session_state.app_state = self.state.GRADE
            st.rerun()

        grade_key = st.session_state.current_grade_key
        st.header(self.page_titles[grade_key][self.lang].capitalize())
        st.title(chapter_data["title"][self.lang])
        
        back_label = {"en": "⬅ Back to chapters", "fr": "⬅ Retour aux chapitres"}
        if st.button(back_label[self.lang]):
            st.session_state.current_chapter = None
            st.session_state.app_state = self.state.GRADE
            st.rerun()

        st.divider()

        for ExerciseClass in chapter_data["exercises"]:
            col1, col2 = st.columns([0.8, 0.2], vertical_alignment="center")
            with col1:
                st.write(f"**{ExerciseClass.title[self.lang]}**")
            with col2:
                btn_label = {"en": "Generate", "fr": "Générer"}
                if st.button(btn_label[self.lang], key=f"btn_{ExerciseClass.id}"):
                    st.session_state.current_exercise = ExerciseClass()
                    st.session_state.app_state = self.state.EXERCISE
                    st.rerun()

    def render_chapter_selection(self):
        grade_key = st.session_state.current_grade_key
        display_title = self.page_titles[grade_key][self.lang].capitalize()
        
        st.set_page_config(page_title=f"PRIME - {display_title}", layout="centered")
        st.title(display_title)

        exercises_list = st.session_state.cached_exercises_list
        
        if not exercises_list:
            msg = {"en": "No exercises available.", "fr": "Aucun exercice disponible."}
            st.info(msg[self.lang])
            return

        menu_title = {"en": "Select a chapter:", "fr": "Sélectionnez un chapitre :"}
        st.markdown(f"### {menu_title[self.lang]}")

        for chapter_key, chapter_data in exercises_list.items():
            chapter_title = chapter_data["title"][self.lang]
            count = len(chapter_data["exercises"])
            
            col1, col2 = st.columns([0.8, 0.2], vertical_alignment="center")
            with col1:
                st.markdown(f"**{chapter_title} ({count})**")
            with col2:
                button_label = {"en": "Access", "fr": "Accéder"}
                if st.button(button_label[self.lang], key=f"chap_btn_{chapter_key}", use_container_width=True):
                    st.session_state.current_chapter = chapter_key
                    st.session_state.app_state = self.state.CHAPTER
                    st.rerun()

    def render(self):
        """
        Renders the page for a specific grade.

        Args:
            grade_titles (dict[str, str]): The titles for the grade in different languages.
            registry (dict): The registry of exercises for the grade.
        """
        self.render_sidebar()

        current_view = st.session_state.app_state

        if current_view == self.state.HOME:
            self.render_main()
        elif current_view == self.state.EXERCISE:
            self.render_exercise()
        elif current_view == self.state.CHAPTER:
            self.render_exercise_selection()
        elif current_view == self.state.GRADE:
            self.render_chapter_selection()