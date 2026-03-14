import numpy as np

def recruiter_score(resume_skills, jd_skills, similarity, experience, resume_text):

    # Skill Match
    if len(jd_skills) == 0:
        skill_score = 0
    else:
        match = len(set(resume_skills) & set(jd_skills))
        skill_score = (match / len(jd_skills)) * 100

    # Experience Score
    if experience >= 10:
        exp_score = 100
    elif experience >= 5:
        exp_score = 80
    elif experience >= 2:
        exp_score = 60
    elif experience >= 1:
        exp_score = 40
    else:
        exp_score = 20

    # Similarity Score
    similarity_score = similarity

    # Resume Length Score
    words = len(resume_text.split())

    if words < 200:
        length_score = 40
    elif words < 400:
        length_score = 70
    elif words < 800:
        length_score = 100
    else:
        length_score = 80

    # Keyword Density
    keyword_score = min(len(resume_skills) * 5, 100)

    # Final weighted score
    final_score = (
        0.4 * skill_score +
        0.25 * exp_score +
        0.2 * similarity_score +
        0.1 * length_score +
        0.05 * keyword_score
    )

    return round(final_score,2), {
        "Skill Match": round(skill_score,2),
        "Experience": exp_score,
        "JD Similarity": round(similarity_score,2),
        "Resume Quality": length_score,
        "Keyword Density": keyword_score
    }