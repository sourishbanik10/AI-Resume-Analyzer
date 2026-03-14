def calculate_ats_score(resume_skills, jd_skills, resume_text, experience):

    score = 0

    # 1 Skill Match (30 points)
    if len(jd_skills) > 0:

        matched = len(set(resume_skills).intersection(set(jd_skills)))

        skill_score = (matched / len(jd_skills)) * 30

        score += skill_score


    # 2 Keyword Match (20 points)

    keywords = ["leadership","management","strategy","analysis","development"]

    keyword_matches = 0

    for word in keywords:

        if word in resume_text:
            keyword_matches += 1

    score += (keyword_matches / len(keywords)) * 20


    # 3 Resume Length (10 points)

    word_count = len(resume_text.split())

    if 300 <= word_count <= 900:
        score += 10
    elif 200 <= word_count < 300:
        score += 7
    else:
        score += 4


    # 4 Section Presence (20 points)

    sections = ["experience","education","skills","projects"]

    section_count = 0

    for section in sections:

        if section in resume_text:
            section_count += 1

    score += (section_count / len(sections)) * 20


    # 5 Experience Score (20 points)

    if experience >= 10:
        score += 20
    elif experience >= 5:
        score += 15
    elif experience >= 2:
        score += 10
    else:
        score += 5


    return round(score,2)