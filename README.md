# 💼 AI Skill-Based Salary Prediction Project

An **end-to-end Data Science & Machine Learning project** that analyzes job market data and predicts salaries based on **skills, experience level, remote work ratio, company size, industry, and job role**.
This project demonstrates a complete **real-world ML workflow**, from raw data processing to model training and insightful visualizations.

---

## 📌 Project Objective

The primary objectives of this project are to:

* Analyze how salaries vary with **experience, remote work, industry, and company size**
* Perform **data cleaning** and **exploratory data analysis (EDA)**
* Engineer meaningful features for machine learning
* Train a **salary prediction regression model**
* Generate clear and insightful visualizations
* Build a **modular and reproducible ML pipeline**

### 📌 Suitable For

* Academic / college projects
* Data science portfolios
* Resume projects
* Learning practical ML workflows

---

## 📂 Dataset Overview

The project uses structured job market data stored in CSV files:

* `jobs_dataset.csv` – Raw job dataset
* `cleaned_jobs_dataset.csv` – Cleaned and preprocessed data
* `features.csv` – Final engineered features used for training
* `target.csv` – Target salary values

📌 Each dataset is processed sequentially through the pipeline.

---

## 🔄 Project Workflow (Pipeline)

The complete pipeline is executed via **`main.py`**, which runs the following steps:

### 1️⃣ Data Cleaning

* Handles missing values
* Removes inconsistencies
* Standardizes data formats

### 2️⃣ Exploratory Data Analysis (EDA)

* Salary distribution analysis
* Salary vs experience trends
* Impact of remote work, industry, and company size

### 3️⃣ Feature Engineering

* Encoding categorical variables
* Feature selection
* Preparing ML-ready datasets

### 4️⃣ Model Training

* Trains a regression model to predict salaries
* Saves the trained model as a `.pkl` file

### 5️⃣ Salary Prediction & Metrics

* Generates salary predictions
* Evaluates model performance

---

## 📊 Output Visualizations

All visual outputs are stored in the `outputs/charts/` directory.

### Key Visualizations

* **Salary Distribution** – Overall salary spread and skewness
* **Salary vs Experience & Remote Ratio (Heatmap)**
* **Salary Distribution by Remote Work Ratio**
* **Salary Trend by Years of Experience**
* **Salary Distribution by Experience Level (Violin Plot)**
* **Top Industries by Average Salary**
* **Company Size vs Salary (Bubble Chart)**
* **Industry & Job Role (Sunburst Chart)**

📌 These visualizations transform raw data into **clear business and career insights**.

---

## 🛠 Tools & Technologies Used

* **Python** – Primary language for data science and ML
* **Pandas** – Data loading, cleaning, and transformation
* **NumPy** – Efficient numerical computations
* **Matplotlib & Seaborn** – Static visualizations (histograms, heatmaps, violin plots)
* **Plotly** – Interactive charts (bubble charts, sunburst diagrams)
* **Scikit-learn** – Feature processing, model training, and evaluation
* **Joblib** – Saving and loading trained ML models
* **Virtual Environment (venv)** – Dependency isolation and reproducibility

---

## 📁 Final Project Structure

```bash
PROJECT 2 - AI SKILL BASED SALARY PREDICTION
│
├── data/
│   ├── jobs_dataset.csv
│   ├── cleaned_jobs_dataset.csv
│   ├── features.csv
│   └── target.csv
│
├── models/
│   └── salary_model.pkl
│
├── outputs/
│   └── charts/
│       ├── salary_distribution.png
│       ├── salary_heatmap_remote_experience.png
│       ├── salary_remote_ratio_dotplot.png
│       ├── salary_trend_years_experience.png
│       ├── salary_vs_experience_violin.png
│       ├── top_industries_salary.png
│       ├── company_size_salary_bubble.html
│       └── industry_jobrole_sunburst.html
│
├── scripts/
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── predict_metrics.py
│
├── venv/
├── main.py
└── requirements.txt
```

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate Virtual Environment

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Complete Pipeline

```bash
python main.py
```

This will:

* Clean the data
* Generate EDA visualizations
* Train the salary prediction model
* Save outputs and trained model

---

## ✅ Key Insights

* Salaries increase significantly with **experience**
* Senior and executive roles have **wider salary ranges**
* Remote roles often offer **competitive or higher pay**
* Industry and company size strongly influence salaries
* Data visualization is critical for salary analysis

---

## 🚀 Future Enhancements

* Implement advanced ML models (e.g., Random Forest, XGBoost)
* Hyperparameter tuning
* Web app for live salary prediction
* API deployment using FastAPI or Flask
* Real-time job data ingestion

---

## 📄 License

This project is intended for **educational and learning purposes**.

---
