# import the modules
import praw

# initialize with appropriate values
client_id = ""
client_secret = ""
username = "acft_bot"
password = "lzT_KkCRlGVrEZYRckcHsbPRzqaCJg"
user_agent = ""

# creating an authorized reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)
