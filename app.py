import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- PAGE --------------------
st.set_page_config(page_title="Job Match Chatbot", layout="centered")
st.title("🤖 Job Profile Chatbot")

st.write("Upload your resume and paste job descriptions to find best matches.")

# -------------------- FUNCTIONS --------------------
def read_resume(file):
    text = ""
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    else:
        text = file.read().decode("utf-8")
    return text


def match_jobs(resume_text, job_list):
    docs = [resume_text] + job_list
    tfidf = TfidfVectorizer(stop_words="english").fit_transform(docs)
    scores = cosine_similarity(tfidf[0:1], tfidf[1:])[0]

    results = list(zip(job_list, scores))
    results.sort(key=lambda x: x[1], reverse=True)
    return results


# -------------------- UI --------------------
uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf", "txt"])
job_input = st.text_area("💼 Paste Job Descriptions (separate using ---)")

if st.button("🔍 Find Matching Jobs"):

    if uploaded_file is None:
        st.error("Please upload your resume first")

    elif not job_input.strip():
        st.error("Please enter job descriptions")

    else:
        st.success("Analyzing...")

        resume_text = read_resume(uploaded_file)
        job_list = [j.strip() for j in job_input.split("---") if j.strip()]

        results = match_jobs(resume_text, job_list)

        st.subheader("📊 Top Job Matches")

        for i, (job, score) in enumerate(results[:5]):
            st.write(f"### Rank {i+1} — {round(score*100,2)}% match")
            st.write(job[:300])
            st.divider()