import pandas as pd
from dateutil.parser import parse

def extract_time(mytime):
    parsedtime = parse(mytime)
    return parsedtime.hour


df = pd.read_csv("hn_stories.csv", names = ["submission_time", "upvotes", "url", "headline"])
allsubtime = df['submission_time']

timehour = allsubtime.apply(extract_time)
timecount = timehour.value_counts(sort=True, ascending=False)
print(timecount) 

