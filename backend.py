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

def predict_role(text):
    text = text.lower()

    roles = {

        "Business Analyst": [
            "brd","frd","srs","rtm","user stories","requirement",
            "agile","scrum","jira","visio","business analysis","uml"
        ],

        "Project Manager": [
            "project management","jira","scrum","kanban",
            "stakeholder","risk management","planning","pmp"
        ],

        "Product Manager": [
            "product management","roadmap","product strategy",
            "market research","customer journey","backlog"
        ],

        "Scrum Master": [
            "scrum","agile","sprint","retrospective",
            "daily standup","product backlog"
        ],

        "QA Engineer": [
            "selenium","testing","automation","manual testing",
            "qa","test case","testng","junit",
            "cypress","playwright","postman"
        ],

        "Python Developer": [
            "python","django","flask","fastapi",
            "rest api","sqlalchemy","celery"
        ],

        "Java Developer": [
            "java","spring","spring boot",
            "hibernate","maven","gradle","jsp"
        ],

        "C++ Developer":[
            "c++","stl","boost","multithreading"
        ],

        "C Developer":[
            "c programming","embedded c","pointers"
        ],

        "C# Developer":[
            "c#",".net","asp.net","entity framework","mvc"
        ],

        ".NET Developer":[
            ".net","asp.net","mvc","blazor",
            "entity framework","web api"
        ],

        "PHP Developer":[
            "php","laravel","codeigniter","symfony"
        ],

        "Ruby Developer":[
            "ruby","ruby on rails","rails"
        ],

        "Go Developer":[
            "golang","go","gin","goroutines"
        ],

        "Rust Developer":[
            "rust","cargo","tokio"
        ],

        "Frontend Developer":[
            "html","css","javascript",
            "typescript","react","next.js",
            "angular","vue","tailwind",
            "bootstrap","redux"
        ],

        "Backend Developer":[
            "django","node.js","express",
            "spring boot","flask","fastapi",
            "microservices","rest api","graphql"
        ],

        "Full Stack Developer":[
            "full stack","mern","mean",
            "django","react","next.js",
            "node.js","mongodb","mysql",
            "postgresql","express"
        ],

        "React Developer":[
            "react","redux","hooks","jsx","next.js"
        ],

        "Angular Developer":[
            "angular","rxjs","typescript"
        ],

        "Vue Developer":[
            "vue","vuex","nuxt"
        ],

        "Node.js Developer":[
            "node","express","npm","nestjs"
        ],

        "Android Developer":[
            "android","kotlin","java",
            "android studio","jetpack compose"
        ],

        "iOS Developer":[
            "ios","swift","xcode",
            "swiftui","objective c"
        ],

        "Flutter Developer":[
            "flutter","dart","firebase"
        ],

        "React Native Developer":[
            "react native","expo","mobile app"
        ],

        "Data Analyst":[
            "sql","power bi","tableau",
            "excel","dashboard","data analysis",
            "etl","reporting","pivot table"
        ],

        "Business Intelligence Developer":[
            "power bi","tableau","ssis",
            "ssrs","ssas","bi developer"
        ],

        "Data Engineer":[
            "spark","hadoop","kafka",
            "etl","airflow","databricks",
            "snowflake","redshift","data pipeline"
        ],

        "Big Data Engineer":[
            "hadoop","spark","hive",
            "pig","kafka","scala"
        ],

        "Data Scientist":[
            "python","numpy","pandas","statistics",
            "probability","matplotlib",
            "seaborn","feature engineering"
        ],

        "Machine Learning Engineer":[
            "machine learning","scikit-learn",
            "tensorflow","keras","pytorch"
        ],

        "AI Engineer":[
            "artificial intelligence",
            "deep learning","cnn","rnn",
            "transformers","llm"
        ],

        "Generative AI Engineer":[
            "generative ai","gpt","llm",
            "langchain","langgraph",
            "huggingface","rag","prompt engineering"
        ],

        "NLP Engineer":[
            "nlp","bert","spacy",
            "nltk","transformers"
        ],

        "Computer Vision Engineer":[
            "opencv","yolo","cnn",
            "image processing","computer vision"
        ],

        "MLOps Engineer":[
            "mlflow","kubeflow","airflow",
            "docker","kubernetes","mlops"
        ],

        "DevOps Engineer":[
            "docker","kubernetes","jenkins",
            "terraform","ansible",
            "ci/cd","linux","helm"
        ],

        "Cloud Engineer":[
            "aws","azure","gcp",
            "ec2","lambda","s3",
            "cloudformation"
        ],

        "AWS Engineer":[
            "aws","ec2","s3","lambda",
            "iam","cloudwatch"
        ],

        "Azure Engineer":[
            "azure","azure devops",
            "azure functions","aks"
        ],

        "GCP Engineer":[
            "gcp","bigquery","cloud run",
            "pubsub","cloud functions"
        ],

        "Site Reliability Engineer":[
            "sre","observability",
            "prometheus","grafana","monitoring"
        ],

        "Database Administrator":[
            "oracle","mysql","postgresql",
            "mongodb","sql server"
        ],

        "Cyber Security Engineer":[
            "owasp","burp suite","wireshark",
            "penetration testing","ethical hacking",
            "soc","siem","nmap"
        ],

        "Network Engineer":[
            "ccna","routing","switching",
            "vpn","tcp/ip","firewall"
        ],

        "System Administrator":[
            "linux","windows server",
            "active directory","shell scripting"
        ],

        "Blockchain Developer":[
            "solidity","ethereum",
            "web3","smart contract"
        ],

        "Game Developer":[
            "unity","unreal","game development"
        ],

        "Embedded Systems Engineer":[
            "embedded","microcontroller",
            "arduino","raspberry pi","rtos"
        ],

        "IoT Developer":[
            "iot","mqtt","esp32","arduino"
        ],

        "Robotics Engineer":[
            "ros","robotics","gazebo"
        ],

        "UI UX Designer":[
            "figma","adobe xd",
            "wireframe","prototype",
            "user experience","user interface"
        ],

        "Graphic Designer":[
            "photoshop","illustrator",
            "after effects","indesign"
        ],

        "Salesforce Developer":[
            "salesforce","apex",
            "lightning","visualforce"
        ],

        "SAP Consultant":[
            "sap","sap fico",
            "sap mm","sap abap"
        ],

        "ServiceNow Developer":[
            "servicenow","itsm","workflow"
        ],

        "Technical Support Engineer":[
            "technical support","ticketing",
            "troubleshooting","helpdesk"
        ],

        "Software Engineer":[
            "algorithms","data structures",
            "oop","software development",
            "design patterns"
        ],

        "Software Architect":[
            "system design","architecture",
            "microservices","design patterns"
        ]
    }

    # Calculate score for each role
    scores = {}

    for role, keywords in roles.items():
        score = 0
        for keyword in keywords:
            if keyword in text:
                score += 1
        scores[role] = score

    # Best matching role
    best_role = max(scores, key=scores.get)

    if scores[best_role] > 0:
        return best_role
    else:
        return "Unknown"
