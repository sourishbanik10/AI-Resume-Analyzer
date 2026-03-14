from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_skill_gap(resume_skills, jd_skills):

    gaps = []

    if len(resume_skills) == 0 or len(jd_skills) == 0:
        return []

    resume_embeddings = model.encode(resume_skills, convert_to_tensor=True)
    jd_embeddings = model.encode(jd_skills, convert_to_tensor=True)

    for i, jd_skill in enumerate(jd_skills):

        scores = util.cos_sim(jd_embeddings[i], resume_embeddings)

        max_score = scores.max().item()

        if max_score < 0.5:
            gaps.append(jd_skill)

    return gaps