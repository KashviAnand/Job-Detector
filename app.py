import streamlit as st
import PyPDF2
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Job Detector", layout="wide")

# -------------------- LOAD MODEL --------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# -------------------- READ RESUME --------------------
def read_resume(uploaded_file):
    text = ""
    if uploaded_file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text()
    else:
        text = uploaded_file.read().decode("utf-8")
    return text

# -------------------- MATCHING FUNCTION --------------------
def match_jobs(resume_text, job_list):
    embeddings = model.encode([resume_text] + job_list)
    scores = cosine_similarity([embeddings[0]], embeddings[1:])[0]

    results = list(zip(job_list, scores))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# -------------------- CHAT STATE --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- UI --------------------
st.title("🤖 Job Detector")
st.write("### 👇 How to use:")
st.write("1. Upload your resume")
st.write("2. Paste job descriptions (separate using ---)")
st.write("3. Press Enter below")

# Resume upload
uploaded_file = st.file_uploader("📄 Upload your Resume", type=["pdf", "txt"])

# Show warning BEFORE chat starts (important fix)
if uploaded_file is None:
    st.info("📌 Please upload your resume to start matching")

# Chat display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("💼 Paste job descriptions separated by ---")

# -------------------- CHAT LOGIC --------------------
if user_input:

    if uploaded_file is None:
        st.warning("⚠️ Please upload your resume first")

    else:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Read resume
        resume_text = read_resume(uploaded_file)

        # Split jobs
        job_list = [j.strip() for j in user_input.split("---") if j.strip()]

        # Match jobs
        results = match_jobs(resume_text, job_list)

        # Prepare response
        response = "### 📊 Top Job Matches:\n\n"

        for i, (job, score) in enumerate(results[:5]):
            response += f"**Rank {i+1} — Match: {round(score*100,2)}%**\n"
            response += f"{job[:200]}...\n\n"

        # Save + display bot response
        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)