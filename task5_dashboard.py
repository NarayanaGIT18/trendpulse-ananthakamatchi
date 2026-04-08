import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load the data
df = pd.read_csv("data/cleaned_trends.csv")

# 2. Create outputs/ folder if it doesn't exist
if not os.path.exists("outputs"):
    os.makedirs("outputs")

print("Data loaded. Outputs folder ready.")
# Sort top 10 by score
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles
top10["short_title"] = top10["title"].apply(lambda x: x if len(x) <= 50 else x[:50] + "...")

# Plot horizontal bar chart
plt.figure(figsize=(10,6))
plt.barh(top10["short_title"], top10["score"], color='skyblue')
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()  # Highest score on top
plt.tight_layout()

# Save the chart
plt.savefig("outputs/chart1_top_stories.png")
plt.show()
# Count stories per category
category_counts = df['category'].value_counts()

plt.figure(figsize=(8,5))
category_counts.plot(kind='bar', color=['skyblue', 'orange', 'green', 'red', 'purple'])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()

# Separate popular vs non-popular

# Create is_popular column
df['is_popular'] = df['engagement'] > 300

popular = df[df['is_popular'] == True]
non_popular = df[df['is_popular'] == False]

plt.figure(figsize=(8,6))
plt.scatter(popular['score'], popular['num_comments'], color='red', label='Popular')
plt.scatter(non_popular['score'], non_popular['num_comments'], color='blue', label='Non-Popular')
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(20,6))

# Chart 1
axes[0].barh(top10["short_title"], top10["score"], color='skyblue')
axes[0].set_title("Top 10 Stories by Score")
axes[0].invert_yaxis()

# Chart 2
axes[1].bar(category_counts.index, category_counts.values, color=['skyblue', 'orange', 'green', 'red', 'purple'])
axes[1].set_title("Stories per Category")

# Chart 3
axes[2].scatter(popular['score'], popular['num_comments'], color='red', label='Popular')
axes[2].scatter(non_popular['score'], non_popular['num_comments'], color='blue', label='Non-Popular')
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Num Comments")
axes[2].set_title("Score vs Comments")
axes[2].legend()

fig.suptitle("TrendPulse Dashboard", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("outputs/dashboard.png")
plt.show()