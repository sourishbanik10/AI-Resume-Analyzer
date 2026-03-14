from skill_db import skills
import re

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills:

        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, text):
            found_skills.append(skill)

    return list(set(found_skills))


def suggest_missing_skills(role, resume_skills):

    role = role.lower()

    role_skill_map = {

    "apparel":[
    "merchandising","inventory management","retail management",
    "product development","store operations"
    ],

    "information technology":[
    "python","sql","data structures","cloud computing","docker"
    ],

    "hr":[
    "recruitment","talent acquisition","hr analytics",
    "employee engagement","performance management"
    ],

    "finance":[
    "financial modeling","forecasting","valuation","risk management"
    ],

    "sales":[
    "sales strategy","crm","lead generation","revenue growth"
    ]

    }

    if role not in role_skill_map:
        return []

    missing = []

    for skill in role_skill_map[role]:

        if skill not in resume_skills:
            missing.append(skill)

    return missing