from functools import partial

import streamlit as st
import matplotlib.figure as Figure

from controller.Controller import Controller, State

class Renderer:

    def __init__(self):
        self.controller = Controller()

        self.lang=self.controller.get_current_language()

    def render_language_switch(self):
        """
        Renders the switch language button.
        """
        # The label is in the targeted language
        toggle_label = {"en": "Passer en Français", "fr": "Switch to English"}
        if st.sidebar.button(toggle_label[self.lang]):
            self.controller.switch_language()
            st.rerun()

    def render_sidebar(self):
        """
        Renders the sidebar
        """
        st.sidebar.title("PRIME")
        st.sidebar.markdown("*(Python Randomized Interactive Math Exercises)*")

        repo_url = "https://github.com/Alyasse-MM/PRIME"
        badge_markdown = f"[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717.svg?style=for-the-badge&logo=github)]({repo_url})"
        st.sidebar.markdown(badge_markdown)

        self.render_language_switch()
        st.sidebar.divider()

        studyplans = [self.controller.get_homepage_metadata()]
        studyplans.extend(self.controller.get_studyplan_list())
        pages=[]
        for studyplan in studyplans:
            pages.append(st.Page(partial(self.controller.switch_page_context, studyplan), title=studyplan["names"][self.lang], url_path=studyplan["key"]))
        pg = st.navigation(pages, position="sidebar")
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
            self.controller.set_app_state(State.MODULE)
            st.rerun()

        st.header(self.controller.get_current_studyplan_names()[self.lang].capitalize())
        st.title(f"{ex.title[self.lang]}")
        
        back_label = {"en": "⬅ Back to exercises", "fr": "⬅ Retour aux exercices"}
        if st.button(back_label[self.lang]):
            self.controller.set_current_exercise(None)
            self.controller.set_app_state(State.MODULE)
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
        Renderers the exercise selection page, using data from currently selected module.
        """
        module_key = self.controller.get_current_module()
        module_data = self.controller.get_exercises_list().get(module_key)

        if not module_data:
            self.controller.set_app_state(State.STUDYPLAN)
            st.rerun()

        st.header(self.controller.get_current_studyplan_names()[self.lang].capitalize())
        st.title(module_data["title"][self.lang])
        
        back_label = {"en": "⬅ Back to modules", "fr": "⬅ Retour aux modules"}
        if st.button(back_label[self.lang]):
            self.controller.set_current_module(None)
            self.controller.set_app_state(State.STUDYPLAN)
            st.rerun()

        st.divider()

        for ExerciseClass in module_data["exercises"]:
            col1, col2 = st.columns([0.8, 0.2], vertical_alignment="center")
            with col1:
                st.write(f"**{ExerciseClass.title[self.lang]}**")
            with col2:
                btn_label = {"en": "Generate", "fr": "Générer"}
                if st.button(btn_label[self.lang], key=f"btn_{ExerciseClass.id}"):
                    self.controller.set_current_exercise(ExerciseClass())
                    self.controller.set_app_state(State.EXERCISE)
                    st.rerun()

    def render_module_selection(self):
        """
        Renders the module selection page, using data from the currently selected studyplan.
        """
        if "shuffled" not in st.query_params:
            st.query_params["shuffled"] = str(False).lower()
        seed = self.controller.get_current_seed()
        shuffled = self.controller.get_studyplan_shuffle_state()
        if (not shuffled and seed is not None) or ("seed" in st.query_params and seed is None):
            self.controller.del_current_seed()
            st.rerun()
        elif shuffled and seed is None:
            self.controller.set_studyplan_shuffle_state(False)
            st.rerun()

        display_title = self.controller.get_current_studyplan_names()[self.lang].capitalize()
        st.set_page_config(page_title=f"PRIME - {display_title}", layout="centered")
        st.title(display_title)

        exercises_list = self.controller.get_exercises_list()
        if not exercises_list:
            msg = {"en": "No exercises available.", "fr": "Aucun exercice disponible."}
            st.info(msg[self.lang])
            return

        menu_title = {"en": "Select a module:", "fr": "Sélectionnez un module :"}
        st.markdown(f"### {menu_title[self.lang]}")

        col1, col2, col3 = st.columns([1/5, 1/5, 1/5], vertical_alignment="center")

        with col1:
            label = {"en": "Sort", "fr": "Trier"}
            if st.button(label[self.lang], key=f"btn_sort", use_container_width=True, disabled=not shuffled):
                self.controller.set_studyplan_shuffle_state(False)
                if "seed" in st.query_params:
                    self.controller.del_current_seed()
                st.rerun()
        with col2:
            if shuffled:
                st.markdown(f"**Seed:** `{seed}`", text_alignment="center")
        with col3:
            label = {"en": "Shuffle", "fr": "Mélanger"}
            if st.button(label[self.lang], key=f"btn_shuffle", use_container_width=True):
                new_seed = self.controller.get_new_seed()
                self.controller.set_current_seed(new_seed)
                self.controller.set_studyplan_shuffle_state(True)
                st.rerun()

        for module_key, module_data in exercises_list.items():
            module_title = module_data["title"][self.lang]
            count = len(module_data["exercises"])
            
            col1, col2 = st.columns([0.8, 0.2], vertical_alignment="center")
            with col1:
                st.markdown(f"**{module_title} ({count})**")
            with col2:
                button_label = {"en": "Access", "fr": "Accéder"}
                if st.button(button_label[self.lang], key=f"module_btn_{module_key}", use_container_width=True):
                    self.controller.set_current_module(module_key)
                    self.controller.set_app_state(State.MODULE)
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
        elif current_view == State.MODULE:
            self.render_exercise_selection()
        elif current_view == State.STUDYPLAN:
            self.render_module_selection()