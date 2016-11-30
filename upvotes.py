import read
from dateutil.parser import parse

def get_year(rawdata):
    datetime = parse(rawdata)
    return(datetime.timetuple().tm_year)
def get_length(text):
    return(len(str(text)))

data = read.load_data()
data['head_len'] = data['headline'].apply(lambda x: get_length(x) )
data['submission_time'] = data['submission_time'].apply(lambda x: get_year(x) )

data.sort_values(by='upvotes', axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')

print('Headline length leads to the most upvotes, top 5:')
print(data[['upvotes','headline', 'head_len']].head())
print('Submission time leads to the most upvotes, top 5:')
print(data[['upvotes','submission_time']].head())
print('Total numbers of upvotes changing over time:')
print(data['submission_time'].value_counts(normalize=False, sort=True, ascending=True, bins=None, dropna=True))