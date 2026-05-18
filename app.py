import streamlit as st
from components.sidebar import render_sidebar
from components.code_input import render_code_input
from components.review_output import render_review_output
from components.compare import render_compare
from components.chat import render_chat
from components.dashboard import render_dashboard
from utils.groq_client import get_client
from utils.history import init_history
from utils.translations import get_translation

# Page Config
st.set_page_config(
    page_title="CodeLens AI",
    page_icon="🔍",
    layout="wide"
)

# Initialize History
init_history()

# Initialize Language
if "lang" not in st.session_state:
    st.session_state.lang = "English"

# Render Sidebar & get API Key
api_key = render_sidebar()

# Translation helper
t = lambda key: get_translation(st.session_state.lang, key)

# Stop if no API key
if not api_key:
    st.warning(t("api_warning"))
    st.stop()

# Setup Groq Client
client = get_client(api_key)

# Header
st.title(t("app_title"))
st.write(t("app_subtitle"))
st.markdown("---")

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    t("tab_review"),
    t("tab_compare"),
    t("tab_chat"),
    t("tab_dashboard")
])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        language, review_type, code, analyze = render_code_input()
    with col2:
        render_review_output(client, language, review_type, code, analyze)

with tab2:
    render_compare(client)

with tab3:
    render_chat(client)

with tab4:
    render_dashboard(client)