import streamlit as st
from utils.groq_client import get_review
from utils.history import add_to_history
from utils.pdf_export import generate_pdf_report

def render_review_output(client, language, review_type, code, analyze):
    st.subheader("📋 AI Feedback")

    # Show loaded review from history
    if "loaded_review" in st.session_state:
        st.info("📂 Loaded from history:")
        st.markdown(st.session_state.loaded_review)
        del st.session_state.loaded_review

    if analyze:
        if code.strip() == "":
            st.warning("⚠️ Please paste or upload some code first!")
        else:
            with st.spinner("🤖 Analyzing your code..."):
                try:
                    result = get_review(client, language, review_type, code)

                    # Save to history
                    add_to_history(language, review_type, code, result)

                    # Display result
                    st.markdown(result)
                    st.success("✅ Review Complete!")

                    st.markdown("---")
                    st.markdown("### 📥 Download Report")

                    col1, col2 = st.columns(2)

                    # TXT Download
                    with col1:
                        st.download_button(
                            label="📄 Download as TXT",
                            data=result,
                            file_name="code_review_report.txt",
                            mime="text/plain",
                            use_container_width=True
                        )

                    # PDF Download
                    with col2:
                        pdf_buffer = generate_pdf_report(
                            language, review_type, code, result
                        )
                        st.download_button(
                            label="📑 Download as PDF",
                            data=pdf_buffer,
                            file_name="code_review_report.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )

                except Exception as e:
                    st.error(f"❌ Something went wrong: {str(e)}")