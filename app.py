import streamlit as st
from resume_rewriter import rewrite_resume
from recruiter_score import recruiter_score
from vector_job_matcher import recommend_jobs_vector
from visualizer import keyword_heatmap
from skill_gap import semantic_skill_gap
from job_matcher import recommend_jobs
from llm_resume_improver import improve_resume
from suggestions import generate_suggestions
from parser import extract_text_from_pdf
from skills import extract_skills, suggest_missing_skills
from similarity import calculate_similarity
from ats import calculate_ats_score
from salary import expected_salary
from role_predictor import predict_role
from experience import extract_experience


# ---------------- PAGE CONFIG ---------------- #

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")
st.markdown(
"""
Upload a resume and compare it with a job description to get:

✔ ATS Score  
✔ Skill Gap Analysis  
✔ Job Matches  
✔ Salary Prediction  
✔ AI Resume Suggestions  
"""
)


# ---------------- INPUT SECTION ---------------- #

col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader("📄 Upload Resume", type=["pdf"])

with col2:
    job_description = st.text_area("🧾 Paste Job Description")


# ---------------- ANALYSIS BUTTON ---------------- #

if st.button("🚀 Analyze Resume"):

    if resume is not None:

        with st.spinner("Analyzing Resume with AI..."):

            # Extract resume text
            resume_text = extract_text_from_pdf(resume)

            # Extract skills
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(job_description)

            # Predict role
            role = predict_role(resume_text)

            # Extract experience
            experience = extract_experience(resume_text)

            # Similarity score
            similarity = calculate_similarity(resume_text, job_description)

            # ATS score
            ats_score = calculate_ats_score(resume_skills, jd_skills, resume_text, experience)

            # Recruiter score
            final_score, breakdown = recruiter_score(
                resume_skills,
                jd_skills,
                similarity,
                experience,
                resume_text
            )

            # Salary prediction
            salary = expected_salary(role, experience)

            # Resume rewriting suggestions
            rewritten = rewrite_resume(resume_text)

            # Missing skills
            missing = suggest_missing_skills(role, resume_skills)

            # Resume improvement suggestions
            suggestions = generate_suggestions(resume_text, resume_skills, jd_skills)

            # AI feedback
            ai_feedback = improve_resume(resume_text, job_description)

            # Job matches (rule based)
            job_matches = recommend_jobs(resume_skills)

            # Semantic skill gap
            skill_gaps = semantic_skill_gap(resume_skills, jd_skills)

            # Heatmap
            heatmap = keyword_heatmap(resume_skills, jd_skills)

            # Vector job search
            vector_jobs = recommend_jobs_vector(resume_text)


        # ---------------- DASHBOARD METRICS ---------------- #

        st.subheader("📊 Resume Analysis Summary")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("ATS Score", f"{ats_score}")
        col2.metric("Match Score", f"{similarity}%")
        col3.metric("Experience", f"{experience} yrs")
        col4.metric("Recruiter Score", f"{final_score}/100")


        # ---------------- BASIC INFO ---------------- #

        st.subheader("🎯 Predicted Role")
        st.write(role)

        st.subheader("💰 Expected Salary (India)")
        st.write(salary)


        # ---------------- SKILLS ---------------- #

        st.subheader("🧠 Resume Skills")

        for skill in resume_skills:
            st.markdown(f"✅ {skill}")

        st.subheader("❌ Missing Skills")

        for skill in missing:
            st.markdown(f"❌ {skill}")


        # ---------------- HEATMAP ---------------- #

        st.subheader("📊 Skill Match Heatmap")

        if heatmap:
            st.pyplot(heatmap)
        else:
            st.write("Not enough job description skills to generate heatmap.")


        # ---------------- JOB MATCHES ---------------- #

        st.subheader("💼 Best Job Matches")

        for role, score in job_matches:
            st.write(f"{role} — {score}% match")


        # ---------------- VECTOR JOB SEARCH ---------------- #

        st.subheader("🤖 AI Vector Job Recommendations")

        for job in vector_jobs:
            st.write("•", job)


        # ---------------- SKILL GAP ---------------- #

        st.subheader("📉 AI Skill Gap Analysis")

        st.write(skill_gaps)


        # ---------------- SUGGESTIONS ---------------- #

        st.subheader("📌 Resume Improvement Suggestions")

        for s in suggestions:
            st.write("•", s)


        # ---------------- AI COACH ---------------- #

        st.subheader("🤖 AI Resume Coach")

        st.write(ai_feedback)


        # ---------------- REWRITTEN BULLETS ---------------- #

        st.subheader("✨ AI Resume Rewriting Suggestions")

        for line in rewritten:
            st.write("•", line)


        # ---------------- RECRUITER SCORE ---------------- #

        st.subheader("🧑‍💼 Recruiter AI Score Breakdown")

        for key, value in breakdown.items():
            st.write(f"{key}: {value}")


    else:
        st.warning("⚠ Please upload a resume.")