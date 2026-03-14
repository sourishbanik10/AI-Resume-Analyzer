import re

def rewrite_resume(resume_text):

    bullet_points = re.split(r"\n|•|-", resume_text)

    improved = []

    for line in bullet_points:

        line = line.strip()

        if len(line) < 20:
            continue

        # Replace weak phrases
        replacements = {
            "worked on": "developed and implemented",
            "responsible for": "led and managed",
            "helped": "collaborated to deliver",
            "did": "executed",
            "made": "designed and built"
        }

        for key,val in replacements.items():
            line = line.replace(key,val)

        # Add action verbs if missing
        if not re.match(r"(developed|managed|implemented|designed|optimized|built)", line.lower()):
            line = "Successfully " + line

        improved.append(line)

    return improved[:10]