from scripts.data_cleaning import clean_data
from scripts.eda import run_eda
from scripts.feature_engineering import engineer_features
from scripts.train_model import train_model
from scripts.predict_metrics import predict_salary

def run_pipeline():
    print("\nStarting AI Job Salary Prediction Pipeline\n")

    try:
        print("Step 1: Data Cleaning")
        clean_data()

        print("\nStep 2: Exploratory Data Analysis")
        run_eda()

        print("\nStep 3: Feature Engineering")
        engineer_features()

        print("\nStep 4: Model Training")
        train_model()

        print("\nStep 5: Salary Prediction")
        predict_salary()

        print("\nPipeline executed successfully!")

    except Exception as e:
        print("\nPipeline failed")
        print("Error:", str(e))

if __name__ == "__main__":
    run_pipeline()
