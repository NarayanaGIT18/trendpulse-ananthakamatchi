import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned_trends.csv")

print("Data Preview:")
print(df.head())

# --------------------------
# ANALYSIS
# --------------------------

# 1. Total posts per category
category_counts = df["category"].value_counts()
print("\nPosts per Category:")
print(category_counts)

# 2. Average score per category
avg_score = df.groupby("category")["score"].mean()
print("\nAverage Score per Category:")
print(avg_score)

# 3. Average engagement per category
avg_engagement = df.groupby("category")["engagement"].mean()
print("\nAverage Engagement per Category:")
print(avg_engagement)

# 4. Top 5 highest scoring posts
top_posts = df.sort_values(by="score", ascending=False).head(5)
print("\nTop 5 Posts:")
print(top_posts[["title", "score", "category"]])

# 5. Most active author
top_author = df["author"].value_counts().head(1)
print("\nMost Active Author:")
print(top_author)