import pandas as pd

def clean_data():
    df = pd.read_csv("data/jobs_dataset.csv")

    df.drop_duplicates(inplace=True)
    df.dropna(subset=["salary_usd", "experience_level", "years_experience"], inplace=True)

    df["posting_date"] = pd.to_datetime(df["posting_date"])
    df["application_deadline"] = pd.to_datetime(df["application_deadline"])

    exp_map = {"EN": 0, "MI": 1, "SE": 2, "EX": 3}
    emp_map = {"FT": 1, "PT": 0, "CT": 0, "FL": 0}
    size_map = {"S": 0, "M": 1, "L": 2}

    df["experience_level"] = df["experience_level"].map(exp_map)
    df["employment_type"] = df["employment_type"].map(emp_map)
    df["company_size"] = df["company_size"].map(size_map)

    df.to_csv("data/cleaned_jobs_dataset.csv", index=False)
    print("Data cleaned.")

if __name__ == "__main__":
    clean_data()
