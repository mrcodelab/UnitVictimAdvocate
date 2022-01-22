# importing the module 
import praw  
  
# initialize with appropriate values 
client_id = "" 
client_secret = "" 
username = "" 
password = "" 
user_agent = "" 
  
# creating an authorized reddit instance 
reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                     username = username,  
                     password = password, 
                     user_agent = user_agent)  
subreddit = reddit.get_subreddit('MLPLounge')
subreddit_comments = subreddit.get_comments()
for comment in subreddit_comments:
    print(comment.id)
    print(comment.body)
