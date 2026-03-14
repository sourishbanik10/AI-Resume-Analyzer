import re
from datetime import datetime

def extract_experience(text):

    text = text.lower()

    # Pattern 1: "20 years", "20+ years", "20 yrs"
    pattern = r'(\d+)\+?\s*(years|yrs)'

    matches = re.findall(pattern, text)

    if matches:
        numbers = [int(x[0]) for x in matches]
        return max(numbers)

    # Pattern 2: detect year ranges like 2005-2024
    years = re.findall(r'(19\d{2}|20\d{2})', text)

    if len(years) >= 2:

        years = [int(y) for y in years]

        min_year = min(years)
        max_year = max(years)

        current_year = datetime.now().year

        if max_year <= current_year:
            return max_year - min_year

    return 0