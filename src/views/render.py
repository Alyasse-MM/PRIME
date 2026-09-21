import streamlit as st
import matplotlib.figure as Figure
from exercises.base_exercise import BaseExercise

def render_content_block(items: list):
    """Iterates through a list of mixed media and renders them appropriately."""
    for item in items:
        if isinstance(item, str):
            st.markdown(item)
        elif isinstance(item, Figure.Figure):
            st.pyplot(item)

def render_grade_page(grade_titles: dict[str, str], registry: dict):
    """
    Renders the page for a specific grade.

    Args:
        grade_titles (dict[str, str]): The titles for the grade in different languages.
        registry (dict): The registry of exercises for the grade.
    """
    lang = st.session_state.lang
    grade_title = grade_titles[lang]

    if "page" not in st.session_state or st.session_state.page not in grade_titles.values():
        st.session_state.page = grade_title
        st.session_state.current_chapter = None
        st.session_state.current_exercise = None
        st.session_state.show_solution = False
        st.session_state.show_insight = False
    
    # EXERCISE VIEW
    if st.session_state.current_exercise is not None:
        st.header(f"{grade_title.capitalize()}")
        st.title(f"{st.session_state.current_exercise.title[lang]}")
        
        back_label = {"en": "⬅ Back to exercises", "fr": "⬅ Retour aux exercices"}
        if st.button(back_label[lang]):
            st.session_state.current_exercise = None
            st.rerun()

        st.divider()

        ex = st.session_state.current_exercise
        data = ex.get_data()
        
        st.subheader(data["title"][lang])
        st.caption(f"ID: {data['id']} | Seed: {data['seed']}")
        render_content_block(data["statement"][lang])

        for i, q in enumerate(data["questions"]):
            st.markdown(f"Question {i+1}")
            render_content_block(q[lang]['question'])
            
            ins_btn = {"en": "Show Insight", "fr": "Voir l'indice"}
            with st.expander(ins_btn[lang]):
                render_content_block(q[lang]['insight'])
            
            sol_btn = {"en": "Show Solution", "fr": "Voir la solution"}
            with st.expander(sol_btn[lang]):
                render_content_block(q[lang]['answer'])

    # CHAPTER VIEW
    elif st.session_state.current_chapter is not None:
        chapter_key = st.session_state.current_chapter
        chapter_data = registry.get(chapter_key)
        chapter_title = chapter_data["title"][lang]
        exercise_list = chapter_data["exercises"]

        st.header(f"{grade_title.capitalize()}")
        st.title(chapter_title)
        
        back_label = {"en": "⬅ Back to chapters", "fr": "⬅ Retour aux chapitres"}
        if st.button(back_label[lang]):
            st.session_state.current_chapter = None
            st.rerun()

        st.divider()

        for ExerciseClass in exercise_list:
            col1, col2 = st.columns([0.8, 0.2], vertical_alignment="center")
            with col1:
                btn_title = ExerciseClass.title[lang]
                st.write(f"**{btn_title}**")
            with col2:
                btn_label = {"en": "Generate", "fr": "Générer"}
                if st.button(btn_label[lang], key=f"btn_{ExerciseClass.id}"):
                    st.session_state.current_exercise = ExerciseClass()
                    st.session_state.show_solution = False
                    st.rerun()

    # GRADE VIEW (CHAPTER LIST)
    else:
        st.set_page_config(page_title=f"PRIME - {grade_title.capitalize()}", layout="centered")
        st.title(grade_title.capitalize())
        
        if not registry:
            msg = {"en": "No exercises available.", "fr": "Aucun exercice disponible."}
            st.info(msg[lang])
            return

        menu_title = {"en": "Select a chapter:", "fr": "Sélectionnez un chapitre :"}
        st.markdown(f"### {menu_title[lang]}")

        for chapter_key, chapter_data in registry.items():
            chapter_title = chapter_data["title"][lang]
            count = len(chapter_data["exercises"])
            
            col1, col2 = st.columns([0.8, 0.2], vertical_alignment="center")
            
            with col1:
                st.markdown(f"**{chapter_title} ({count})**")
                
            with col2:
                button_label = {"en": "Access", "fr": "Accéder"}
                if st.button(f"{button_label[lang]}", key=f"chap_btn_{chapter_key}", use_container_width=True):
                    st.session_state.current_chapter = chapter_key
                    st.rerun()