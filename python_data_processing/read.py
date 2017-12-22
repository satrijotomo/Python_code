def load_data():
    import pandas as pd
    df = pd.read_csv("hn_stories.csv", names = ["submission_time", "upvotes", "url", "headline"])
    #print(df.head())
    #print(df)
    return df
if __name__ == "__main__":
    load_data()
    
