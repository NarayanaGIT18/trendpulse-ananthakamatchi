import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned_trends.csv")

# --------------------------
# 1. Posts per Category
# --------------------------
category_counts = df["category"].value_counts()

category_counts.plot(kind="bar")
plt.title("Posts per Category")
plt.xlabel("Category")
plt.ylabel("Number of Posts")
plt.xticks(rotation=45)
plt.show()

# --------------------------
# 2. Average Score
# --------------------------
avg_score = df.groupby("category")["score"].mean()

avg_score.plot(kind="bar")
plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.show()

# --------------------------
# 3. Engagement
# --------------------------
avg_engagement = df.groupby("category")["engagement"].mean()

avg_engagement.plot(kind="bar")
plt.title("Average Engagement per Category")
plt.xlabel("Category")
plt.ylabel("Engagement")
plt.xticks(rotation=45)
plt.show()