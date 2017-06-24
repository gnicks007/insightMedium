#!/usr/bin/python3
# -*- encoding: utf-8 -*-

#Nick version

import json

import requests
from insightMedium.parser import parse_user, parse_publication, parse_post, parse_single_post
from insightMedium.constant import ROOT_URL, ACCEPT_HEADER, ESCAPE_CHARACTERS, COUNT
from insightMedium.model import Sort

#from selenium import webdriver

#exec_path = "/Applications/chromedriver"
#browser = webdriver.Chrome(exec_path)

class Medium(object):
    def __init__(self):
        pass

    def get_user_profile(self, username):
        url = "{}@{}/latest".format(ROOT_URL, username)
        return self._send_request(url, parse_user)

    def get_publication_profile(self, publication_name):
        url = "{}{}/latest".format(ROOT_URL, publication_name)
        return self._send_request(url, parse_publication)

    def get_user_posts(self, username, n=COUNT):
        return self._send_post_request(ROOT_URL + "@{0}/latest?limit={count}".format(username, count=n))

    def get_publication_posts(self, publication_name, n=COUNT):
        return self._send_post_request(ROOT_URL + "{0}/latest?limit={count}".format(publication_name, count=n))

    def get_top_posts(self, n=COUNT):
        return self._send_post_request(ROOT_URL + "browse/top?limit={count}".format(count=n))

    def get_posts_by_tag(self, tag, n=COUNT, sort=Sort.TOP):
        url = "{}tag/{tag}".format(ROOT_URL, tag=tag)
        if sort == Sort.LATEST:
            url += "/latest"
        url += "?limit={}".format(n)
        return self._send_post_request(url)


    @staticmethod
    def _send_request(url, parse_function):
        req = requests.get(url, headers=ACCEPT_HEADER) #PAYLOAD
        print(url, req.status_code)
        if req.status_code == requests.codes.ok:
            return parse_function(json.loads(req.text.replace(ESCAPE_CHARACTERS, "").strip()))
        else:
            return None

    @staticmethod
    def _send_post_request(url):
        return Medium._send_request(url, parse_post)



##### - NICK SECTION - #######    

    #Nick - added this function to return search results.
    #how to I change the number of search results returned
    #need to create my own parse function
    def get_posts_by_search(self, keyword):
        url = "{}search?q={tag}".format(ROOT_URL, tag=keyword)  #{}search/posts?q={tag}
        parsed_post_list = self._send_post_request(url) #this is after, "parse_post" is called
        return parsed_post_list
      

    #get payload for a single post
    def get_single_post(self, url):
        req = requests.get(url, headers=ACCEPT_HEADER) #PAYLOAD
        print(url, req.status_code)
        
        if req.status_code == requests.codes.ok:
            payload = json.loads(req.text.replace(ESCAPE_CHARACTERS, "").strip())
            return payload
        else:
            return None
    
    #Nick: Attempt to get all info about a single post, including highlights and blockquotes
    #Tags etc. 
    #browser_driver is a selenium webdriver. 
    #doing it this way because i'll be looping over the function get_parsed_single_post
    #don't want to open up a browser instance everytime I process a URL. Will just pass a browser reference
    
    def get_parsed_single_post(self, url, browser_driver):
        req = requests.get(url, headers=ACCEPT_HEADER) #PAYLOAD
        print(url, req.status_code)
        if req.status_code == requests.codes.ok:
            return parse_single_post(url, json.loads(req.text.replace(ESCAPE_CHARACTERS, "").strip()), browser_driver)
        else:
            return None
    
   
  ##### - ------ - #######   
