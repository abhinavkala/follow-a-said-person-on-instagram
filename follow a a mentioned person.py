from InstagramAPI import InstagramAPI

# set up the Instagram API client
api = InstagramAPI(username, password)
api.login()

# define a function to follow a user
def follow_user(username):
    api.searchUsername(username)
    user_id = api.LastJson['user']['pk']
    api.follow(user_id)
    print(f"Successfully followed {username}!")

# define a function to handle incoming chat messages
def handle_message(message):
    if 'follow' in message.lower():
        # extract the username from the message
        username = message.split('follow ')[-1]
        follow_user(username)
    else:
        print("Sorry, I don't understand.")

# simulate incoming chat messages
messages = ['Can you follow @john.doe?', 'Follow @jane.smith please'] #add more of keywords
for message in messages:
    handle_message(message)
