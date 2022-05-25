#!/usr/bin/python

import random, os
import re

path = r"/home/path/path/"


random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])

result = random_filename

TweetPrep = re.sub(r" ?\([^)]+\)", "", result)
TweetPrep = TweetPrep.replace(".tumblr", "")
TweetPrep = TweetPrep.replace("Source ", "")
TweetCaption = TweetPrep + ".tumblr.com"

with open ("pylogs.txt", "a") as f:
    f.write(f'{TweetCaption}\n')
print(TweetCaption)


    
