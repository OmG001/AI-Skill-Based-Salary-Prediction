import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

def train_model():
    X = pd.read_csv("data/features.csv")
    y = pd.read_csv("data/target.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())

    preds = model.predict(X_test)

    print("📊 MAE:", mean_absolute_error(y_test, preds))
    print("📈 R²:", r2_score(y_test, preds))

    joblib.dump(model, "models/salary_model.pkl")
    print("Model saved")

if __name__ == "__main__":
    train_model()
