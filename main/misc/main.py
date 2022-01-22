# import the modules
import praw

# initialize with appropriate values
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""

# creating an authorized reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)


# Define keywords for the bot to react to
keywords = \
    ["I was raped", "SHARP", "SARC", "UVA", "Victim Advocate", "SVC",
        "unrestricted report", "unrestricted reporting", "sexual assault",
        "rape"]
