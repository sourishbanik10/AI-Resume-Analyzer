salary_data = {

"information technology": "6 – 18 LPA",
"engineering": "6 – 20 LPA",
"data science": "8 – 22 LPA",

"hr": "4 – 12 LPA",
"finance": "5 – 14 LPA",
"advocate": "4 – 10 LPA",

"sales": "5 – 18 LPA",
"marketing": "5 – 16 LPA",

"apparel": "4 – 12 LPA",
"designer": "5 – 14 LPA"

}

def expected_salary(role, experience):

    role = role.lower()

    for key in salary_data:

        if key in role:

            base_salary = salary_data[key]

            if experience < 2:
                return "3 – 6 LPA"

            elif experience < 5:
                return base_salary

            else:
                return "10 – 25 LPA"

    return "4 – 10 LPA"