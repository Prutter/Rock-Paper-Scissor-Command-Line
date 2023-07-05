import random
import requests

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!", "user"
    else:
        return "Computer wins!", "computer"

def generate_computer_response():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_chatgpt_response(message):
    # Make a request to the ChatGPT API
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    data = {
        "prompt": message,
        "max_tokens": 50,
        "temperature": 0.8
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    choices = response_json["choices"]
    if choices:
        return choices[0]["text"].strip()
    else:
        return "I'm sorry, I couldn't generate a response."

def play_game():
    user_wins = 0
    computer_wins = 0

    user_choice = input("Choose rock, paper, or scissors (or enter a number to exit): ").lower()
    
    while user_choice in ["rock", "paper", "scissors"]:
        computer_choice = generate_computer_response()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result, winner = determine_winner(user_choice, computer_choice)
        print(result)
        
        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
        
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
        
        # Get response from ChatGPT API
        response = get_chatgpt_response(computer_choice)
        print("Computer's response: " + response)
        
        user_choice = input("\nChoose rock, paper, or scissors (or enter a number to exit): ").lower()

play_game()



