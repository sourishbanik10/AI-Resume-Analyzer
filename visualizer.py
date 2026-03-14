import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def keyword_heatmap(resume_skills, jd_skills):

    if len(jd_skills) == 0:
        return None

    data = []

    for skill in jd_skills:

        present = 1 if skill in resume_skills else 0

        data.append({"Skill": skill, "Present": present})

    df = pd.DataFrame(data)

    if df.empty:
        return None

    plt.figure(figsize=(6,4))

    sns.heatmap(
        df.set_index("Skill"),
        annot=True,
        cmap="coolwarm",
        cbar=False
    )

    plt.title("Resume vs Job Skill Match")

    return plt