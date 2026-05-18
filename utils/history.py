import streamlit as st
from datetime import datetime

def init_history():
    if "history" not in st.session_state:
        st.session_state.history = []

def add_to_history(language, review_type, code, result):
    st.session_state.history.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "language": language,
        "review_type": review_type,
        "code": code,
        "result": result
    })

def clear_history():
    st.session_state.history = []
    st.rerun()

def get_history():
    return st.session_state.history