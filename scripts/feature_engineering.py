import pandas as pd

def engineer_features():
    df = pd.read_csv("data/cleaned_jobs_dataset.csv")

    df["skill_count"] = df["required_skills"].apply(
        lambda x: len(str(x).split(","))
    )

    features = df[
        [
            "experience_level",
            "years_experience",
            "employment_type",
            "company_size",
            "remote_ratio",
            "benefits_score",
            "job_description_length",
            "skill_count"
        ]
    ]

    target = df["salary_usd"]

    features.to_csv("data/features.csv", index=False)
    target.to_csv("data/target.csv", index=False)

    print("Features engineering done.")

if __name__ == "__main__":
    engineer_features()
