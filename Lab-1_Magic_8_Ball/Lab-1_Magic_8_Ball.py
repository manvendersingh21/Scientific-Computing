import random as rn
import time as tm

def magic_8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    print("Welcome to the Magic 8 Ball!", end="\r")
    tm.sleep(1)
    question = input("\nWhar is your question? ")
    print("Thinking", end="", flush=True)

    for _ in range(3):
        tm.sleep(0.5)
        print(".", end="", flush=True)
        
    tm.sleep(0.5)
    answer = rn.choice(responses)
    print("\nYour Question was: " + question)
    print(f"The Magic 8 Ball says: {answer}" )
if __name__ == "__main__":
    while True:
        magic_8_ball()