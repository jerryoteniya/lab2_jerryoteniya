import csv
import sys
import os

def load_raw_data(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

#CLEAN DATA
def clean_data(tweets):
    clean_tweets = []
    bad_rows = 0

    for tweet in tweets:
    
        if tweet['Text'] == "" or tweet['Text'] is None:
            bad_rows += 1
            continue  

    
        if tweet['Likes'] == "" or tweet['Likes'] is None:
            tweet['Likes'] = 0
            bad_rows += 1
        else:
            tweet['Likes'] = int(tweet['Likes'])

        
        if tweet['Retweets'] == "" or tweet['Retweets'] is None:
            tweet['Retweets'] = 0
            bad_rows += 1
        else:
            tweet['Retweets'] = int(tweet['Retweets'])

        clean_tweets.append(tweet)

    print(f"Cleaned dataset. Fixed {bad_rows} bad rows.\n")
    return clean_tweets

#VIRAL POST

def find_viral_post(tweets):
    highest_likes = -1
    viral_tweet = None
    
    for tweet in tweets:
        if tweet['Likes'] > highest_likes:
            highest_likes = tweet['Likes']
            viral_tweet = tweet
    

    print("BOOYAHHHH!!!! The most viral tweet is:\n")
    print(f"User: {viral_tweet['Username']}")
    print(f"Likes: {viral_tweet['Likes']}")
    print(f"Text: {viral_tweet['Text']}\n")

#Top 10 liked TWEETS
def custom_sort_by_likes(tweets, n=10):
    length = len(tweets)
    for i in range(n):
        for j in range(0, n-i-1):
            if tweets[j]['Likes'] < tweets[j+1]['Likes']:
                tweets[j], tweets[j+1] = tweets[j+1], tweets[j]
    return tweets


#CONTENT FILTER (SEARCH BAR)
def search_tweets(tweets, keyword):
    results = []

    for tweet in tweets:
        if keyword.lower() in tweet['Text'].lower():
            results.append(tweet)

    print(f"\nFound {len(results)} tweets containing '{keyword}':\n")

    for tweet in results:
        print(f"{tweet['Username']}: {tweet['Text']}\n")

    return results

#MAIN PROGRAM
if __name__ == "__main__":  
    dataset = load_raw_data('twitter_dataset.csv')
    print(f"Loaded {len(dataset)} raw tweets.\n")

    cleaned_dataset = clean_data(dataset)

    find_viral_post(cleaned_dataset)

    sorted_tweets = custom_sort_by_likes(cleaned_dataset)


    print("Top 10 most liked tweets:\n")
    for i in range(min(10, len(sorted_tweets))):
        tweet = sorted_tweets[i]
        print(f"{i+1}. {tweet['Username']} - Likes: {tweet['Likes']}\n   Text: {tweet['Text']}\n")

keyword = input("Enter a keyword to search for in tweets: ")
search_results = search_tweets(cleaned_dataset, keyword)