import streamlit as st
from utils.groq_client import get_client

def render_compare(client):
    st.subheader("🔁 Compare Two Code Versions")
    st.write("Paste your old and new code to see what changed and which is better!")

    # Two columns for old and new code
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📜 Old Code")
        old_code = st.text_area("Paste old code here:", height=300, key="old_code")
        if old_code.strip() != "":
            st.code(old_code, language="python")

    with col2:
        st.markdown("### ✨ New Code")
        new_code = st.text_area("Paste new code here:", height=300, key="new_code")
        if new_code.strip() != "":
            st.code(new_code, language="python")

    compare = st.button("🔍 Compare Versions", use_container_width=True)

    if compare:
        if old_code.strip() == "" or new_code.strip() == "":
            st.warning("⚠️ Please paste both old and new code!")
        else:
            with st.spinner("🤖 Comparing code versions..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": """You are an expert code reviewer.
                            Compare two versions of code and provide feedback in these sections:
                            📝 Summary of Changes (what changed between versions)
                            ✅ Improvements Made (what got better)
                            ❌ Regressions Found (what got worse)
                            🏆 Which Version is Better and Why
                            💡 Further Suggestions to improve the new version"""
                        },
                        {
                            "role": "user",
                            "content": f"Old Code:\n{old_code}\n\nNew Code:\n{new_code}"
                        }
                    ]
                )
                result = response.choices[0].message.content
                st.markdown("### 📊 Comparison Results:")
                st.markdown(result)
                st.success("✅ Comparison Complete!")

                # Download Button
                st.download_button(
                    label="📥 Download Comparison Report",
                    data=result,
                    file_name="comparison_report.txt",
                    mime="text/plain",
                    use_container_width=True
                )