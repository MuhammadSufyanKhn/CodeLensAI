import streamlit as st
import json
from utils.groq_client import get_quality_metrics

def render_dashboard(client):
    st.subheader("📊 Code Quality Dashboard")
    st.write("Get a visual breakdown of your code quality!")

    # Language Selector
    language = st.selectbox("Programming Language:", [
        "Python", "JavaScript", "Java", "C++", "C#", "Other"
    ], key="dashboard_language")

    # Code Input
    code = st.text_area("Paste your code here:", height=250, key="dashboard_code")

    analyze = st.button("📊 Analyze Code Quality", use_container_width=True)

    if analyze:
        if code.strip() == "":
            st.warning("⚠️ Please paste some code first!")
        else:
            with st.spinner("🤖 Analyzing code quality..."):
                metrics = get_quality_metrics(client, language, code)

                if metrics:
                    st.markdown("---")
                    st.markdown("### 📊 Quality Metrics")

                    # Row 1 - Score Cards
                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.metric(
                            label="Overall Score",
                            value=f"{metrics.get('overall', 0)}/10",
                        )
                    with col2:
                        st.metric(
                            label="Readability",
                            value=f"{metrics.get('readability', 0)}/10",
                        )
                    with col3:
                        st.metric(
                            label="Performance",
                            value=f"{metrics.get('performance', 0)}/10",
                        )
                    with col4:
                        st.metric(
                            label="Security",
                            value=f"{metrics.get('security', 0)}/10",
                        )

                    st.markdown("---")

                    # Row 2 - More Metrics
                    col5, col6, col7 = st.columns(3)

                    with col5:
                        st.metric(
                            label="Maintainability",
                            value=f"{metrics.get('maintainability', 0)}/10",
                        )
                    with col6:
                        st.metric(
                            label="Best Practices",
                            value=f"{metrics.get('best_practices', 0)}/10",
                        )
                    with col7:
                        st.metric(
                            label="Documentation",
                            value=f"{metrics.get('documentation', 0)}/10",
                        )

                    st.markdown("---")

                    # Summary
                    st.markdown("### 📝 Summary")
                    st.info(metrics.get("summary", "No summary available"))

                    # Recommendations
                    st.markdown("### 💡 Top Recommendations")
                    recommendations = metrics.get("recommendations", [])
                    for i, rec in enumerate(recommendations):
                        st.write(f"{i+1}. {rec}")