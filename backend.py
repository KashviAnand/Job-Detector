from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Resume reader
def read_resume(file):
    text = ""
    reader = PdfReader(file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Job matching
def match_jobs(resume_text, job_list):
    docs = [resume_text] + job_list
    tfidf = TfidfVectorizer(stop_words="english").fit_transform(docs)
    scores = cosine_similarity(tfidf[0:1], tfidf[1:])[0]
    return list(zip(job_list, scores))

# Role detection
def detect_role(text):
    text = text.lower()

    if any(word in text for word in ["brd", "frd", "requirement", "user stories", "rtm"]):
        return "Business Analyst"

    elif any(word in text for word in ["selenium", "testing", "qa"]):
        return "QA Engineer"

    elif any(word in text for word in ["sql", "power bi", "data"]):
        return "Data Analyst"
    
    elif any(word in text for word in ["python", "ai ml", "scikit learn"]):
         return "AI ML engineer"

    elif any(word in text for word in ["python", "Probability", "Excel",""]):
         return "Data Science"

    else:
        return "General Role"