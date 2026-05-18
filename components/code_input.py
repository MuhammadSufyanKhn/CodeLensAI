import streamlit as st
from utils.github import fetch_github_code, is_github_url

def render_code_input():
    st.subheader("📝 Your Code")

    # Language Selector
    language = st.selectbox("Programming Language:", [
        "Python", "JavaScript", "Java", "C++", "C#", "Other"
    ])

    # Review Type
    review_type = st.selectbox("What do you want?", [
        "Full Review",
        "Find Bugs",
        "Suggest Improvements",
        "Generate Documentation",
        "Security Vulnerability Scan"
    ])

    # Input Method Tabs
    tab1, tab2, tab3 = st.tabs(["📝 Paste Code", "📂 Upload File", "🌐 GitHub URL"])

    code = ""

    with tab1:
        code_input = st.text_area("Paste your code here:", height=250)
        if code_input.strip() != "":
            code = code_input
            st.markdown("### 👀 Syntax Highlighted Preview:")
            st.code(code, language=language.lower())

    with tab2:
        uploaded_file = st.file_uploader(
            "Upload a code file:",
            type=["py", "js", "java", "cpp", "cs", "txt"]
        )
        if uploaded_file is not None:
            code = uploaded_file.read().decode("utf-8")
            st.markdown("### 👀 Preview:")
            st.code(code, language=language.lower())

    with tab3:
        github_url = st.text_input(
            "Paste GitHub file URL:",
            placeholder="https://github.com/user/repo/blob/main/file.py"
        )
        if github_url.strip() != "":
            if is_github_url(github_url):
                with st.spinner("🔄 Fetching code from GitHub..."):
                    fetched_code, error = fetch_github_code(github_url)
                    if error:
                        st.error(error)
                    else:
                        code = fetched_code
                        st.success("✅ Code fetched successfully!")
                        st.markdown("### 👀 Preview:")
                        st.code(code, language=language.lower())
            else:
                st.error("❌ Please enter a valid GitHub URL!")

    # Analyze Button
    analyze = st.button("🚀 Review My Code", use_container_width=True)

    return language, review_type, code, analyze