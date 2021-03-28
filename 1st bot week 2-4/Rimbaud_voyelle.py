import tweepy

import emoji

consumer_key = "*********"
consumer_secret = "**********"

access_token = "*********"
access_token_secret = "**********"

#callback_uri = 'oob'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)

redirect_url = (auth.get_authorization_url())

auth.get_access_token(verifier_value)
print (redirect_url)

Cursor = tweepy.Cursor(api.search, q="poem", tweet_mode="extendedpy ").items(1)

for tweet in Cursor:

    Compilation = []

    a_letter = 'a'
    e_letter = 'e'
    i_letter = 'i'
    u_letter = 'u'
    o_letter = 'o'

    def try_1 (character):

        for character in tweet :
            if character == a_letter :
                Compilation.append(emoji.emojize(':black_circle:'))

            elif character == e_letter :
                Compilation.append(emoji.emojize(':white_circle:'))

            elif character == i_letter :
                Compilation.append(emoji.emojize(':red_circle:'))

            elif character == u_letter :
                Compilation.append(emoji.emojize(':green_circle:'))

            elif character == o_letter :
                Compilation.append(emoji.emojize(':blue_circle:'))

            else :
                 Compilation.append(character)


    try_1(tweet)

    Final_string = ''.join (Compilation)

    print(Final_string)
