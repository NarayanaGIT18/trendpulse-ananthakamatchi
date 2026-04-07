import requests
import time
import json
import os
from datetime import datetime

# API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

# Categories
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm", "app", "internet"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global", "news"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "match"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "experiment"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming", "tv"]
}

collected_data = []
category_count = {cat: 0 for cat in categories}

# Create folder
if not os.path.exists("data"):
    os.makedirs("data")

# Fetch IDs
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:500]
except:
    print("Error fetching story IDs")
    story_ids = []

# Loop categories
for category, keywords in categories.items():
    print("Processing:", category)

    for story_id in story_ids:
        if category_count[category] >= 25:
            break

        try:
            res = requests.get(ITEM_URL.format(story_id), headers=headers)
            story = res.json()

            if not story or "title" not in story:
                continue

            title = story["title"].lower()

            if any(keyword in title for keyword in keywords):

                data = {
                    "post_id": story.get("id"),
                    "title": story.get("title"),
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", "unknown"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                collected_data.append(data)
                category_count[category] += 1

        except:
            print("Error with story:", story_id)
            continue

    time.sleep(2)

# Save file
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(collected_data, f, indent=4)

print("Collected", len(collected_data), "stories")
print("Saved to", filename)