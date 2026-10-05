from registry import registry
from views.render import render_grade_page
import streamlit as st

title = {"fr": "seconde", "en": "10th grade"}
path = "D:/Fichiers/_IMPORTANT/Etudes/Superieur/BAC+3/Cours/premiere"
render_grade_page(title, registry(path))