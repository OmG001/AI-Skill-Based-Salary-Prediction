import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

def run_eda():
    os.makedirs("outputs/charts", exist_ok=True)

    df = pd.read_csv("data/cleaned_jobs_dataset.csv")

    # ===============================
    # 1️⃣ Salary Distribution (KEEP SAME)
    # ===============================
    plt.figure(figsize=(8, 5))
    sns.histplot(df["salary_usd"], bins=30, kde=True)
    plt.title("Salary Distribution (USD)")
    plt.xlabel("Salary USD")
    plt.ylabel("Count")
    plt.savefig("outputs/charts/salary_distribution.png")
    plt.close()

    # ===============================
    # 2️⃣ Violin Plot: Experience vs Salary (BETTER THAN BOXPLOT)
    # ===============================
    plt.figure(figsize=(8, 5))
    sns.violinplot(
        x="experience_level",
        y="salary_usd",
        data=df,
        inner="quartile"
    )
    plt.title("Salary Distribution by Experience Level")
    plt.savefig("outputs/charts/salary_vs_experience_violin.png")
    plt.close()

    # ===============================
    # 3️⃣ Heatmap: Remote Ratio vs Experience
    # ===============================
    heatmap_data = (
    df.groupby(["experience_level", "remote_ratio"])["salary_usd"]
    .mean()
    .reset_index()
    .pivot(
        index="experience_level",
        columns="remote_ratio",
        values="salary_usd"
    )
)

    plt.figure(figsize=(8, 5))
    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".0f",
        cmap="coolwarm"
    )
    plt.title("Average Salary Heatmap (Experience vs Remote Ratio)")
    plt.savefig("outputs/charts/salary_heatmap_remote_experience.png")
    plt.close()

    # ===============================
    # 3️⃣ Plotly Line Chart: Salary vs Years Experience (NEW)
    # ===============================
    exp_salary = (
        df.groupby("years_experience")["salary_usd"]
        .mean()
        .reset_index()
        .sort_values("years_experience")
    )

    line_fig = px.line(
        exp_salary,
        x="years_experience",
        y="salary_usd",
        markers=True,
        title="Average Salary Trend by Years of Experience",
        labels={
            "years_experience": "Years of Experience",
            "salary_usd": "Average Salary (USD)"
        }
    )

    line_fig.write_image(
        "outputs/charts/salary_trend_years_experience.png",
        width=1000,
        height=500
    )

    # ===============================
    # 4️⃣ Plotly Dot Plot: Remote Ratio vs Salary (NEW)
    # ===============================
    dot_fig = px.strip(
        df,
        x="remote_ratio",
        y="salary_usd",
        color="remote_ratio",
        title="Salary Distribution by Remote Work Ratio",
        labels={
            "remote_ratio": "Remote Work %",
            "salary_usd": "Salary USD"
        }
    )

    dot_fig.write_image(
        "outputs/charts/salary_remote_ratio_dotplot.png",
        width=900,
        height=500
    )

    # ===============================
    # 6️⃣ Top 10 Industries by Avg Salary 
    # ===============================
    top_industries = (
        df.groupby("industry")["salary_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=top_industries.values,
        y=top_industries.index
    )
    plt.title("Top 10 Industries by Average Salary")
    plt.xlabel("Average Salary (USD)")
    plt.ylabel("Industry")
    plt.savefig("outputs/charts/top_industries_salary.png")
    plt.close()

    print("EDA completed (static + interactive charts saved)")

if __name__ == "__main__":
    run_eda()
