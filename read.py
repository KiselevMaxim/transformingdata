import pandas
def load_data():
    hn_stories = pandas.read_csv("hn_stories.csv")
    hn_stories.columns = ["submission_time", "upvotes", "url", "headline"]
    return(hn_stories)

if __name__ == "__main__":
    thedata = load_data()
    print(thedata.head(2))