import re
from collections import defaultdict

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ----------------------------
# Resume Reader
# ----------------------------
def read_resume(file):
    text = ""
    reader = PdfReader(file)

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# ----------------------------
# Text Cleaning
# ----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ----------------------------
# Job Matching
# ----------------------------
def match_jobs(resume_text, job_list):
    docs = [resume_text] + job_list

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(docs)

    scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )[0]

    results = list(zip(job_list, scores))

    return sorted(
        results,
        key=lambda x: x[1],
        reverse=True
    )


# ----------------------------
# Role Prediction
# ----------------------------
def predict_role(text, top_n=3):
    text = clean_text(text)

    roles = {
        "Business Analyst": [
            "brd", "frd", "srs", "rtm",
            "user stories", "requirement",
            "agile", "scrum", "jira",
            "business analysis", "uml"
        ],

        "Project Manager": [
            "project management", "jira",
            "scrum", "kanban", "stakeholder",
            "risk management", "planning", "pmp"
        ],

        "Product Manager": [
            "product management", "roadmap",
            "product strategy", "market research",
            "customer journey", "backlog"
        ],

        "Scrum Master": [
            "scrum", "agile", "sprint",
            "retrospective", "daily standup",
            "product backlog"
        ],

        "QA Engineer": [
            "selenium", "testing",
            "automation", "manual testing",
            "qa", "test case",
            "testng", "junit",
            "cypress", "playwright",
            "postman"
        ],

        "Python Developer": [
            "python", "django",
            "flask", "fastapi",
            "rest api", "sqlalchemy",
            "celery"
        ],

        "Java Developer": [
            "java", "spring",
            "spring boot",
            "hibernate", "maven",
            "gradle"
        ],

        "Frontend Developer": [
            "html", "css",
            "javascript", "typescript",
            "react", "next js",
            "angular", "vue",
            "tailwind", "redux"
        ],

        "Backend Developer": [
            "django", "node js",
            "express", "spring boot",
            "flask", "fastapi",
            "microservices",
            "rest api",
            "graphql"
        ],

        "Full Stack Developer": [
            "full stack",
            "mern", "mean",
            "django", "react",
            "next js",
            "node js",
            "mongodb",
            "mysql",
            "postgresql",
            "express"
        ],

        "Data Analyst": [
            "sql", "power bi",
            "tableau", "excel",
            "dashboard",
            "data analysis",
            "etl", "reporting"
        ],

        "Data Engineer": [
            "spark", "hadoop",
            "kafka", "etl",
            "airflow", "databricks",
            "snowflake",
            "data pipeline"
        ],

        "Data Scientist": [
            "python", "numpy",
            "pandas", "statistics",
            "matplotlib",
            "feature engineering"
        ],

        "Machine Learning Engineer": [
            "machine learning",
            "scikit learn",
            "tensorflow",
            "keras",
            "pytorch"
        ],

        "AI Engineer": [
            "artificial intelligence",
            "deep learning",
            "cnn", "rnn",
            "transformers",
            "llm"
        ],

        "Generative AI Engineer": [
            "generative ai",
            "gpt", "llm",
            "langchain",
            "langgraph",
            "huggingface",
            "rag",
            "prompt engineering"
        ],

        "DevOps Engineer": [
            "docker",
            "kubernetes",
            "jenkins",
            "terraform",
            "ansible",
            "ci cd",
            "linux"
        ],

        "Cloud Engineer": [
            "aws",
            "azure",
            "gcp",
            "ec2",
            "lambda",
            "s3"
        ],

        "Network Engineer": [
            "ccna",
            "routing",
            "switching",
            "vpn",
            "tcp ip",
            "firewall"
        ],

        "UI UX Designer": [
            "figma",
            "adobe xd",
            "wireframe",
            "prototype",
            "user experience",
            "user interface"
        ],

        "Salesforce Developer": [
            "salesforce",
            "apex",
            "lightning",
            "visualforce"
        ],

        "Technical Support Engineer": [
            "technical support",
            "ticketing",
            "troubleshooting",
            "helpdesk"
        ],

        "Software Engineer": [
            "algorithms",
            "data structures",
            "oop",
            "software development",
            "design patterns"
        ]
    }

    scores = defaultdict(int)

    for role, keywords in roles.items():
        for keyword in keywords:
            pattern = r"\b" + re.escape(keyword) + r"\b"
            matches = re.findall(pattern, text)
            scores[role] += len(matches)

    ranked_roles = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_roles[:top_n]


# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":

    resume_text = read_resume("resume.pdf")

    jobs = [
        "Business Analyst with BRD, FRD, Agile, Jira",
        "QA Engineer with Selenium, API Testing, Postman",
        "Python Developer with Django and FastAPI"
    ]

    print("\nTop Matching Jobs:")
    for job, score in match_jobs(resume_text, jobs):
        print(f"{job} --> {score:.2f}")

    print("\nPredicted Roles:")

    def detect_role(text):
    result = predict_role(text)

    if isinstance(result, list):
        return result[0][0]

    return result
    print(predict_role(resume_text))
```
