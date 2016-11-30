import read
from dateutil.parser import parse

def get_hour(rawdata):
    datetime = parse(rawdata)
    return(datetime.timetuple().tm_hour)

data = read.load_data()

data['submission_time'] = data['submission_time'].apply(lambda x: get_hour(x))
#print(data['submission_time'].head(1000))
print(data['submission_time'].value_counts(normalize=False, sort=True, ascending=True, bins=None, dropna=True))