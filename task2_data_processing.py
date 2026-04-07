import pandas as pd
import json

# Load JSON file
with open("data/trends_20260407.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["author"] = df["author"].fillna("unknown")
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)

# Convert types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# New column
df["engagement"] = df["score"] + df["num_comments"]

# Save to CSV
df.to_csv("data/cleaned_trends.csv", index=False)

print("Cleaned data saved successfully!")