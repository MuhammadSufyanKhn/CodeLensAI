import streamlit as st
from utils.history import get_history, clear_history
from utils.translations import get_translation

def render_sidebar():
    lang = st.sidebar.selectbox("🌍 Language / زبان", ["English", "اردو"])
    st.session_state.lang = lang
    t = lambda key: get_translation(lang, key)

    st.sidebar.title(t("settings"))

    # Automatically load API key from Streamlit secrets
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        api_key = ""

    # Show warning if key not found
    if not api_key:
        st.sidebar.warning("⚠️ API Key not found in secrets!")

    st.sidebar.markdown("---")

    # History Section
    st.sidebar.title(t("review_history"))
    history = get_history()

    if len(history) == 0:
        st.sidebar.info(t("no_reviews"))
    else:
        for i, item in enumerate(reversed(history)):
            with st.sidebar.expander(f"🕒 {item['time']} — {item['language']}"):
                st.write(f"**Type:** {item['review_type']}")
                st.code(item['code'][:100] + "...", language=item['language'].lower())
                if st.button(f"Load Review #{len(history) - i}", key=f"load_{i}"):
                    st.session_state.loaded_review = item['result']

        st.sidebar.markdown("---")
        if st.sidebar.button(t("clear_history"), use_container_width=True):
            clear_history()

    return api_key