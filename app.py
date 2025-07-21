import streamlit as st
from utils.grammar import grammar_corrections  
from utils.style_feedback import style_improvements
from utils.resume_loader import read_docx, read_txt

st.set_page_config(page_title="AI Resume Enhancer", layout="centered")

st.image("assets/logo.png", width=80)
st.title(" AI Resume Style & Grammar Enhancement Agent")
st.markdown("Upload or paste your resume below. The AI will correct grammar and improve style")

uploaded_file = st.file_uploader(" Upload your resume (.docx or .txt)", type=["docx", "txt"])
text_input = st.text_area("Or paste your resume here:")

resume_text = ""
if uploaded_file:
    if uploaded_file.name.endswith(".docx"):
        resume_text = read_docx(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        resume_text = read_txt(uploaded_file)
elif text_input:
    resume_text = text_input

if st.button(" Analyze Resume"):
    if not resume_text.strip():
        st.warning("Please upload or paste resume content.")
    else:
        with st.spinner("Analyzing..."):
            grammar_issues = grammar_corrections(resume_text)
            style_feedback = style_improvements(resume_text)

        st.subheader("Grammar Corrections")
        if grammar_issues:
            for issue in grammar_issues:
                st.markdown(f"""
                🔸 **Incorrect:** `{issue['sentence']}`  
                🔹 **Reason:** {issue['message']}  
                ✅ **Suggestions:** {', '.join(issue['suggestion']) if issue['suggestion'] else 'No suggestion'}
                """)
        else:
            st.success("✅ No grammar issues found!")

        st.subheader("🎯 Style & Professional Feedback")
        st.markdown(style_feedback)


