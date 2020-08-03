#!/usr/bin/env python3

import requests

r = requests.get('https://cat-fact.herokuapp.com/facts')   

list = []

def namecall():
    for x in r.json()["all"]:
        if x.get("user"):
            first_name = x["user"]["name"]["first"] 
            last_name = x["user"]["name"]["last"]
            print(first_name, last_name)

namecall()
