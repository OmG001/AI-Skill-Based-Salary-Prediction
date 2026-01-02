import joblib
import pandas as pd

def predict_salary():
    model = joblib.load("models/salary_model.pkl")

    sample = pd.DataFrame({
        "experience_level": [2],
        "years_experience": [6],
        "employment_type": [1],
        "company_size": [2],
        "remote_ratio": [100],
        "benefits_score": [8.5],
        "job_description_length": [1800],
        "skill_count": [6]
    })

    prediction = model.predict(sample)
    print("Predicted Salary (USD):", int(prediction[0]))

if __name__ == "__main__":
    predict_salary()
