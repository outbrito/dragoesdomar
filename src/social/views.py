# -*- coding: utf-8 -*-
import urllib

from django.conf import settings
from django.http import HttpResponse

    
def social(request, _type):
    import tweepy
    if _type == 'facebook':
        json = urllib.urlopen(settings.FACEBOOK_JSON).read()
    elif _type == 'twitter':
        auth = tweepy.OAuthHandler(settings.TWITTER_KEY, settings.TWITTER_SECRET)
#         auth.set_access_token('', '')
        api = tweepy.API(auth)
        json = api.user_timeline(screen_name=settings.TWITTER_USERNAME, include_rts=1)
    elif _type == 'instagram':
        json = urllib.urlopen(settings.INSTAGRAM_JSON).read()
    return HttpResponse(json, mimetype="application/json")