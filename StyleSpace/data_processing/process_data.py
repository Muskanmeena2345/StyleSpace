import pandas as pd

def clean_and_process(data):
    df = pd.DataFrame(data)
    df.dropna(inplace=True)
    df['trend_score'] = df['likes'] + df['shares']
    return df

if __name__ == "__main__":
    raw_data = [{'title': 'Summer Dress', 'likes': 100, 'shares': 20}, {'title': 'Winter Coat', 'likes': 150, 'shares': 30}]
    processed_data = clean_and_process(raw_data)
    print(processed_data)
