import streamlit as st
from utils.groq_client import get_chat_response

def render_chat(client):
    st.subheader("💬 Chat with your Code")
    st.write("Paste your code and ask any questions about it!")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "chat_code" not in st.session_state:
        st.session_state.chat_code = ""

    # Code Input
    code = st.text_area(
        "Paste your code here:",
        height=200,
        value=st.session_state.chat_code,
        key="chat_code_input"
    )

    if code.strip() != "":
        st.session_state.chat_code = code
        st.code(code, language="python")

    st.markdown("---")

    # Display chat history
    if len(st.session_state.chat_history) == 0:
        st.info("👋 Paste your code above and start asking questions!")
    else:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                with st.chat_message("user"):
                    st.markdown(msg["content"])
            else:
                with st.chat_message("assistant"):
                    st.markdown(msg["content"])

    # Chat Input
    user_message = st.chat_input("Ask anything about your code...")

    if user_message:
        if st.session_state.chat_code.strip() == "":
            st.warning("⚠️ Please paste your code first!")
        else:
            # Add user message to history
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_message
            })

            with st.spinner("🤖 Thinking..."):
                response = get_chat_response(
                    client,
                    st.session_state.chat_code,
                    st.session_state.chat_history[:-1],
                    user_message
                )

            # Add assistant response to history
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response
            })

            st.rerun()

    # Clear Chat Button
    if len(st.session_state.chat_history) > 0:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()