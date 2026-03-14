def generate_suggestions(resume_text, resume_skills, jd_skills):

    suggestions = []

    text = resume_text.lower()

    # Resume length check
    word_count = len(text.split())

    if word_count < 300:
        suggestions.append("Resume is too short. Add more details about achievements and responsibilities.")

    if word_count > 900:
        suggestions.append("Resume is too long. Try to keep it within 1-2 pages.")

    # Section checks
    if "projects" not in text:
        suggestions.append("Add a Projects section to showcase practical work.")

    if "certification" not in text:
        suggestions.append("Add Certifications to strengthen your profile.")

    if "skills" not in text:
        suggestions.append("Include a dedicated Skills section.")

    # Missing keywords from job description
    missing_keywords = list(set(jd_skills) - set(resume_skills))

    if len(missing_keywords) > 0:
        suggestions.append(
            "Consider adding these keywords from the job description: " + ", ".join(missing_keywords[:5])
        )

    # Achievement check
    if "%" not in text and "increase" not in text and "improved" not in text:
        suggestions.append("Add measurable achievements (e.g., 'Increased sales by 20%').")

    if len(suggestions) == 0:
        suggestions.append("Your resume looks strong for this job!")

    return suggestions