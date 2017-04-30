# this code is extracts timeline from specific user
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor
import sys

def auth_user():
    consmr_key = 
    consmr_secret = 
    access_token = 
    access_token_secret = 
    auth = OAuthHandler(consmr_key,consmr_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def get_twitter_client():
    authenticated = auth_user()
    tweet_client = API(authenticated)
    return tweet_client


if __name__ == '__main__':

    user = sys.argv[1]
   
    out_text_name = "user_timeline_{}.txt".format(user) 
    file_obj = open(out_text_name, 'w', encoding='utf-8')
    client_init = get_twitter_client()

    for page in Cursor(client_init.user_timeline, screen_name = user, count = 100).pages(12):
        for status in page:
            file_obj.write(status.text + "\n")
    file_obj.close()




