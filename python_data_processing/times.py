import pandas as pd
from dateutil.parser import parse

def extract_time(mytime):
    parsedtime = parse(mytime)
    return parsedtime


df = pd.read_csv("hn_stories.csv", names = ["submission_time", "upvotes", "url", "headline"])
allsubtime = df['submission_time']
for row in allsubtime:
    print(extract_time(row))

