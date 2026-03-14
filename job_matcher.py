from job_roles import job_roles

def recommend_jobs(resume_skills):

    results = []

    for role, skills in job_roles.items():

        match = len(set(resume_skills).intersection(set(skills)))

        score = (match / len(skills)) * 100

        results.append((role, round(score,2)))

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:4]