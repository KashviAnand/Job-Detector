import streamlit as st
from backend import read_resume, match_jobs, detect_role

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Job Profile Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Background */
.stApp{
background: radial-gradient(circle at 80% 20%, #ff2e55 0%, #b30021 40%, #4a000b 100%);
background-attachment:fixed;
}

/* Main Container */
.block-container{
max-width:900px;
padding-top:40px;
}

/* Upload Box */
[data-testid="stFileUploader"]{
background:rgba(255,255,255,.05);
padding:15px;
border-radius:12px;
border:1px solid rgba(255,255,255,.1);
}

/* Text Area */
textarea{
background:rgba(255,255,255,.05)!important;
color:white!important;
}

/* Button */
.stButton>button{
width:100%;
background:white;
color:#b30021;
padding:14px;
font-size:18px;
font-weight:bold;
border-radius:12px;
border:none;
transition:.3s;
}

.stButton>button:hover{
background:#ff2e55;
color:white;
}

/* Result Card */
.result-card{
background:rgba(255,255,255,.08);
padding:20px;
border-radius:15px;
margin-top:20px;
margin-bottom:20px;
border-left:5px solid #ff2e55;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<h1 style='font-size:60px;color:white;margin-bottom:5px;'>
🤖 Job Profile Chatbot
</h1>

<p style='font-size:18px;color:white;opacity:.8;'>
Upload your resume and paste job descriptions to find the best matching jobs.
</p>
""", unsafe_allow_html=True)

# ---------------- INPUTS ---------------- #

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

job_input = st.text_area(
    "📋 Paste Job Description(s) (Separate multiple JDs using ---)",
    height=220
)

analyze = st.button("🚀 Find Matching Jobs")

# ---------------- ANALYSIS ---------------- #

if analyze:

    if uploaded_file is None:
        st.error("⚠ Please upload your resume.")

    elif not job_input.strip():
        st.error("⚠ Please paste at least one Job Description.")

    else:

        with st.spinner("🔍 Analyzing Resume..."):

            resume_text = read_resume(uploaded_file)

            job_list = [
                job.strip()
                for job in job_input.split("---")
                if job.strip()
            ]

            results = match_jobs(resume_text, job_list)

        st.success("✅ Analysis Completed Successfully")

        st.markdown(
            "<h2 style='color:white;'>🎯 Top Job Matches</h2>",
            unsafe_allow_html=True
        )

        for i, (job, score) in enumerate(results[:5]):

            role = detect_role(job)

            st.markdown(f"""
            <div class='result-card'>

            <h3 style='color:white;'>
            🏆 Rank {i+1}
            </h3>

            <h2 style='color:#00ff99;'>
            {round(score * 100, 2)}% Match
            </h2>

            <h4 style='color:#FFD700;'>
            🎯 Predicted Role: {role}
            </h4>

            <p style='color:white;line-height:1.6;'>
            {job[:400]}
            </p>

            </div>
            """, unsafe_allow_html=True)

        st.balloons()
