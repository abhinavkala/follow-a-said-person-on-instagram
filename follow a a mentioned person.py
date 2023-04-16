from InstagramAPI import InstagramAPI
import random

# set up the Instagram API client
api = InstagramAPI(username, password)
api.login()

# define a function to follow a user
def follow_user(username):
    api.searchUsername(username)
    user_id = api.LastJson['user']['pk']
    api.follow(user_id)
    return f"Successfully followed {username} on Instagram!"

# define a function to handle user input
def handle_message(message):
    # generate a random response
    responses = ["I'm sorry, I don't understand.",
                 "Sure, I can follow that person for you.",
                 "Please provide a valid username."]
    response = random.choice(responses)

    # check if the message contains the word "follow"
    if 'follow' in message.lower():
        # extract the username from the message
        username = message.split('follow ')[-1]
        response = follow_user(username)

    return response

# simulate a conversation with the chatbot
while True:
    # get user input
    message = input("You: ")

    # handle user input
    response = handle_message(message)

    # print chatbot response
    print("Chatbot:", response)
