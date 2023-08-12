import requests
import random
import datetime

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    return data["content"]

def get_random_programming_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    data = response.json()
    return data["joke"]

def get_current_date():
    today = datetime.datetime.now()
    formatted_date = today.strftime("%Y.%m.%d %A")
    return formatted_date

def main():
    date = get_current_date()
    quote = get_random_quote()
    joke = get_random_programming_joke()

    print("Hi there! Good Morning\n")
    print(f"Today is {date}\n")
    print("Here is a daily quote:\n", quote)
    print("")
    print("Have a fun day with this joke ;)\n", joke)

if __name__ == "__main__":
    main()

