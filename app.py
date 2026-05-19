import streamlit as st
from backend import read_resume, match_jobs, detect_role

# -------------------- PAGE --------------------
st.set_page_config(page_title="Job Match Chatbot", layout="centered")
st.title("🤖 Job Profile Chatbot")

st.write("Upload your resume and paste job descriptions to find best matches.")

# -------------------- UI --------------------

uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf", "txt"])
job_input = st.text_area("💼 Paste Job Descriptions (separate using ---)")

if st.button("🔍 Find Matching Jobs"):

    if uploaded_file is None:
        st.error("Please upload your resume first")

    elif not job_input.strip():
        st.error("Please enter job descriptions")

    else:
        st.success("Analyzed")

        resume_text = read_resume(uploaded_file)
        job_list = [j.strip() for j in job_input.split("---") if j.strip()]

        results = match_jobs(resume_text, job_list)

        for i, (job, score) in enumerate(results[:5]):
            role = detect_role(job)

            st.write("DEBUG ROLE:", role)

            st.write(f"### Rank {i+1} — {round(score*100,2)}% match")
            st.write(f"🎯 Role: {role}")
            st.write(job[:300])
            st.divider()