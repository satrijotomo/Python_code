import pandas as pd
df = pd.read_csv("hn_stories.csv", names = ["submission_time", "upvotes", "url", "headline"])
allurl = df['url']
urlcount = allurl.value_counts(sort=True, ascending=False)
print(urlcount[:100]) 