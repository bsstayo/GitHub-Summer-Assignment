import requests
import os
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

    path = "./log"
    if not os.path.exists(path):
        os.makedirs(path)

    current_date = datetime.datetime.now().strftime('%Y_%m_%d')
    file_path = os.path.join(path, f"{current_date}_log.txt")
    file_content = []

    file_content.append("Hi there! Good Morning\n")
    file_content.append(f"Today is {date}\n")
    file_content.append("Here is a daily quote:")
    file_content.append(quote)
    file_content.append("")
    file_content.append("Have a fun day with this joke ;)")
    file_content.append(joke)

    with open(file_path, 'w') as file:
        for fc in file_content:
            file.write(fc + '\n')
            print(fc)

if __name__ == "__main__":
    main()
