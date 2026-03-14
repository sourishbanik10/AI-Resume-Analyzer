from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

def improve_resume(resume_text, job_description):

    prompt = f"""
Improve this resume for the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Give:
1. Better summary
2. Stronger bullet points
3. ATS keyword suggestions
"""

    result = generator(prompt, max_length=300)

    return result[0]["generated_text"]