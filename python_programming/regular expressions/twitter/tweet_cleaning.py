import HTMLParser
import sys
import re
print sys.getdefaultencoding()
filetext  = open('tweet.html', 'r')
original_tweet = filetext.read()
#print original_tweet

#Decoding data Escaping HTML characters
html_parser = HTMLParser.HTMLParser()
tweet = html_parser.unescape(original_tweet.decode('utf-8'))
#print '-----------'
#print type(tweet)
#print tweet.encode('ascii', 'ignore')

#Apostrophe Lookup
APPOSTOPHES = {"'s" : " is", "'re" : " are"} ## Need a huge dictionary
words = tweet.split()
reformed = [APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words]
reformed = " ".join(reformed)

print reformed.encode('ascii', 'ignore')
cleaned = " ".join(re.findall('[A-Z][^A-Z]*', reformed))
print cleaned.encode('ascii', 'ignore')

filetext.close()
