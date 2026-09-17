from numpy import size
import streamlit as st
from exercises.base_exercise import BaseExercise

def render_grade_page(grade_titles: dict[str, str], registry: dict[str, list[type[BaseExercise]]]):
    """
    Renders the page for a specific grade.

    Args:
        grade_titles (dict[str, str]): The titles for the grade in different languages.
        registry (dict[str, list[type[BaseExercise]]]): The registry of exercises for the grade.
    """
    lang = st.session_state.lang
    grade_title = grade_titles[lang]

    if "page" not in st.session_state or st.session_state.page not in grade_titles.values():
        st.session_state.page = grade_title
        st.session_state.current_exercise = None
        st.session_state.show_solution = False
        st.session_state.show_insight = False
    
    # If an exercise is loaded in the session state, show ONLY the exercise
    if "current_exercise" in st.session_state and st.session_state.current_exercise is not None:
        st.header(f"{grade_title.capitalize()}")
        st.title(f"{st.session_state.current_exercise.title[lang]}")
        back_label = {"en": "⬅ Back to list",
                      "fr": "⬅ Retour à la liste"}
        if st.button(back_label[lang]):
            st.session_state.current_exercise = None
            st.rerun()

        st.divider()

        ex = st.session_state.current_exercise
        data = ex.get_data()
        lang = st.session_state.lang
        
        st.subheader(data["title"][lang])
        st.caption(f"ID: {data['id']} | Seed: {data['seed']}")
        st.markdown(data["statement"][lang])

        for q in data["questions"]:
            st.markdown(q[lang]["question"])
            
            ins_btn = {"en": "Show Insight",
                    "fr": "Voir l'indice"}
            if st.button(ins_btn[lang], type="primary"):
                st.session_state.show_insight = True
                st.rerun()
            if st.session_state.show_insight:
                st.info(q[lang]["insight"])
            
            sol_btn = {"en": "Show Solution",
                    "fr": "Voir la solution"}
            if st.button(sol_btn[lang], type="primary"):
                st.session_state.show_solution = True
                st.rerun()
            if st.session_state.show_solution:
                st.markdown(f"**{q[lang]['answer']}**")



    # If no exercise is selected, show the chapters and buttons
    else:
        st.set_page_config(page_title=f"PRIME - {grade_title.capitalize()}", layout="centered")
        st.title(grade_title.capitalize())
        if not registry:
            msg = {"en": "No exercises available.",
                    "fr": "Aucun exercice disponible."}
            st.info(msg[lang])
            return

        for chapter_key, chapter_data in registry.items():
            chapter_title = chapter_data["title"][lang]
            exercise_list = chapter_data["exercises"]
            with st.expander(f"{chapter_title} ({len(exercise_list)})", expanded=False):
                for ExerciseClass in exercise_list:
                    btn_title = ExerciseClass.title[lang]
                    st.write(f"**{btn_title}**")
                    btn_label = {"en": "Generate", "fr": "Générer"}
                    if st.button(btn_label[lang], key=f"btn_{ExerciseClass.id}"):
                        st.session_state.current_exercise = ExerciseClass()
                        st.session_state.show_solution = False
                        st.rerun()
                    st.divider() if ExerciseClass != exercise_list[-1] else None