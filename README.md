🤖 AI Resume Analyzer

Live app link:
https://ai-resume-analyzer-hruzgdtrkrndxrlkybfbaz.streamlit.app/

An AI-powered Resume Analysis and Job Matching System that evaluates resumes against job descriptions using Natural Language Processing (NLP), Machine Learning, and Vector Similarity.

The application provides ATS scores, skill gap analysis, salary estimation, job recommendations, and AI-driven resume improvement suggestions.

Built with Python, Streamlit, NLP models, and semantic embeddings.

🚀 Features
📄 Resume Parsing

Upload resumes in PDF format

Extracts and processes resume text automatically

🧠 Skill Extraction

Detects technical and professional skills from the resume

Extracts skills from job descriptions

📊 ATS Score Calculation

Simulates an Applicant Tracking System (ATS) by evaluating:

Skill match

Resume content quality

Experience

Job description similarity

🎯 Role Prediction

Uses Machine Learning to predict the most relevant job role for the candidate.

💰 Salary Estimation (India)

Estimates expected salary range based on:

Predicted role

Years of experience

📉 Skill Gap Analysis

Identifies missing skills required for the target job role.

🔎 Job Recommendation System

Provides best matching job roles based on resume skills.

Includes:

Skill-based matching

Vector similarity search

📈 Recruiter AI Score

Generates an overall resume evaluation score similar to a recruiter screening process.

✨ AI Resume Improvement

Uses LLM-based feedback to suggest improvements in:

Resume content

Keywords

Structure

Impact statements

📊 Visual Skill Heatmap

Displays skill match visualization between resume and job description.

🛠 Tech Stack
Programming

Python

Web Framework

Streamlit

NLP & Machine Learning

Scikit-learn

Sentence Transformers

TF-IDF Vectorization

Vector Search

FAISS

Data Processing

Pandas

NumPy

Visualization

Matplotlib

Seaborn

PDF Parsing

pdfplumber

AI Integration

OpenAI API (optional)

📂 Project Structure
AI-Resume-Analyzer
│
├── app.py
├── style.css
│
├── parser.py
├── skills.py
├── similarity.py
├── ats.py
├── salary.py
├── role_predictor.py
├── experience.py
├── suggestions.py
├── resume_rewriter.py
├── recruiter_score.py
├── skill_gap.py
├── visualizer.py
├── job_matcher.py
├── vector_job_matcher.py
├── job_data_loader.py
├── llm_resume_improver.py
│
├── data
│   ├── UpdatedResumeDataSet.csv
│   └── jobs_dataset.csv
│
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py
📄 How to Use

1️⃣ Upload a resume (PDF)
2️⃣ Paste the job description
3️⃣ Click Analyze Resume

The system will generate:

ATS Score

Predicted Job Role

Experience Detection

Skill Match Score

Missing Skills

Salary Estimate

Job Recommendations

Resume Improvement Suggestions

📊 Example Output

The analyzer provides:

Predicted Role: Machine Learning Engineer
Experience: 2 years
ATS Score: 82/100
Expected Salary: ₹8L – ₹14L
Missing Skills: Docker, Deep Learning, Git
🌐 Future Improvements

Planned enhancements:

Resume chatbot using RAG

Large-scale job matching using vector databases

Resume ranking across multiple job listings

Advanced recruiter dashboard

Multi-language resume support

👨‍💻 Author

Sourish Banik

B.Tech Computer Science (AI & ML)
IEM KOLKATA (NEW TOWN CAMPUS)
