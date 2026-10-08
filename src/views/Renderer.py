from functools import partial

import streamlit as st
import matplotlib.figure as Figure

from controller.Controller import Controller, State

class Renderer:

    def __init__(self):
        self.controller = Controller()

        self.page_titles = {
            "accueil" : {"fr" : "Accueil", "en" : "Home"},
            "seconde" : {"fr" : "Seconde", "en" : "10th Grade"},
            "premiere" : {"fr" : "Première", "en" : "11th Grade"},
            "terminale" : {"fr" : "Terminale", "en" : "12th Grade"}
        }
        self.lang=self.controller.get_current_language()

    def render_language_switch(self):
        """
        Renderes the switch language button.
        """
        # The label is in the targeted language
        toggle_label = {"en": "Passer en Français", "fr": "Switch to English"}
        if st.sidebar.button(toggle_label[self.lang]):
            self.controller.switch_language()
            st.rerun()

    def render_sidebar(self):
        """
        Renderes the sidebar
        """
        st.sidebar.title("PRIME")
        st.sidebar.markdown("*(Python Randomized Interactive Math Exercises)*")

        repo_url = "https://github.com/Alyasse-MM/PRIME"
        badge_markdown = f"[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717.svg?style=for-the-badge&logo=github)]({repo_url})"
        st.sidebar.markdown(badge_markdown)

        self.render_language_switch()
        st.sidebar.divider()
        
        page_home = st.Page(partial(self.controller.switch_page_context, "accueil"), title=self.page_titles["accueil"][self.lang], url_path="accueil")
        page_prem = st.Page(partial(self.controller.switch_page_context, "premiere"), title=self.page_titles["premiere"][self.lang], url_path="premiere")
        page_sec  = st.Page(partial(self.controller.switch_page_context, "seconde"), title=self.page_titles["seconde"][self.lang], url_path="seconde")
        page_term = st.Page(partial(self.controller.switch_page_context, "terminale"), title=self.page_titles["terminale"][self.lang], url_path="terminale")

        pg = st.navigation([page_home, page_sec, page_prem, page_term], position="sidebar")
        pg.run()

    def render_main(self):
        """
        Renders the homepage.
        """
        st.set_page_config(page_title="PRIME - Homepage", layout="centered")
        title = {"fr": "Accueil", "en": "Homepage"}
        st.title(title[self.lang])

    def render_content_block(self, items: list):
        """
        Iterates through a list of mixed media and renders them appropriately.
        """
        for item in items:
            if isinstance(item, str):
                st.markdown(item)
            elif isinstance(item, Figure.Figure):
                st.pyplot(item)    

    def render_exercise(self):
        """
        Renders the currently selected exercise.
        """
        ex = self.controller.get_current_exercise()
        if not ex:
            self.controller.set_app_state(State.CHAPTER)
            st.rerun()

        grade_key = self.controller.get_current_grade_key()
        st.header(self.page_titles[grade_key][self.lang].capitalize())
        st.title(f"{ex.title[self.lang]}")
        
        back_label = {"en": "⬅ Back to exercises", "fr": "⬅ Retour aux exercices"}
        if st.button(back_label[self.lang]):
            self.controller.set_current_exercise(None)
            self.controller.set_app_state(State.CHAPTER)
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
        """
        Renderers the exercise selection page, using data from currently selected chapter.
        """
        chapter_key = self.controller.get_current_chapter()
        chapter_data = self.controller.get_cached_exercises_list().get(chapter_key)

        if not chapter_data:
            self.controller.set_app_state(State.GRADE)
            st.rerun()

        grade_key = self.controller.get_current_grade_key()
        st.header(self.page_titles[grade_key][self.lang].capitalize())
        st.title(chapter_data["title"][self.lang])
        
        back_label = {"en": "⬅ Back to chapters", "fr": "⬅ Retour aux chapitres"}
        if st.button(back_label[self.lang]):
            self.controller.set_current_chapter(None)
            self.controller.set_app_state(State.GRADE)
            st.rerun()

        st.divider()

        for ExerciseClass in chapter_data["exercises"]:
            col1, col2 = st.columns([0.8, 0.2], vertical_alignment="center")
            with col1:
                st.write(f"**{ExerciseClass.title[self.lang]}**")
            with col2:
                btn_label = {"en": "Generate", "fr": "Générer"}
                if st.button(btn_label[self.lang], key=f"btn_{ExerciseClass.id}"):
                    self.controller.set_current_exercise(ExerciseClass())
                    self.controller.set_app_state(State.EXERCISE)
                    st.rerun()

    def render_chapter_selection(self):
        """
        Renders the chapter selection page, using data from the currently selected grade.
        """

        grade_key = self.controller.get_current_grade_key()
        display_title = self.page_titles[grade_key][self.lang].capitalize()
        
        st.set_page_config(page_title=f"PRIME - {display_title}", layout="centered")
        st.title(display_title)

        exercises_list = self.controller.get_cached_exercises_list()
        
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
                    self.controller.set_current_chapter(chapter_key)
                    self.controller.set_app_state(State.CHAPTER)
                    st.rerun()

    def render(self):
        """
        Renders the page corresponding to the current state.
        """
        self.render_sidebar()

        current_view = self.controller.get_app_state()

        if current_view == State.HOME:
            self.render_main()
        elif current_view == State.EXERCISE:
            self.render_exercise()
        elif current_view == State.CHAPTER:
            self.render_exercise_selection()
        elif current_view == State.GRADE:
            self.render_chapter_selection()