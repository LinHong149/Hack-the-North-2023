import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

USERNAME = "Aaveg"
BOT_NAME = "Luna"


def generate_response(prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=3126,
        n=1,
        stop=None
    )
    return response["choices"][0]["text"]


def categorizer(input_str: str):

    print()
    print()
    conversation = ""
    command = "Can you categorize these items based on whether or not they are financial wants or financial needs with names in list form? Also provide totals for each category. \n"
    conversation += command + input_str

    response = generate_response(conversation)
    return response


def item_list_to_string(lst: list):
    return_str = ""
    
    for i in lst:
        return_str += i + '\n'
    
    return return_str


def financial_advisor(income, expenditure, items):

    conversation = ""
    command = "Assume you are a financial advisor. My monthly income is " + str(income) + " and my monthly expenditure is" + str(expenditure) + ".\n"
    command += "Based on all my purchases this month, where could I have saved money? \n"
    command += "The purchases are as follows: \n"
    all_items = item_list_to_string(items)
    command += all_items
    conversation += command

    response = generate_response(conversation)
    print(response)


def determine_expenditure(lst_of_purchases: list):

    pass


def create_goal(item: str, item_cost: float, time_frame: str, lst_of_purchases: list, income: str):

    conversation = ""
    command = f"My income is {income}. If I want to be able to afford a ${item_cost} {item} in a time frame of {time_frame}, where could I cut my spending from my list of purchases listed as follows to be able to afford that? Please be descriptive. Can you also remake my list of purchases with reasonable spending?\n {item_list_to_string(lst_of_purchases)}"
    conversation += command

    response = generate_response(conversation)
    print(response)


lst_of_items = []
continue_sequence = "y"

while continue_sequence == "y":
    item = input(f"Enter the items and its price (Chatime $15...Press n to exit): $")
    lst_of_items.append(item)

    if item == 'n':
        continue_sequence = 'n'

print(categorizer(item_list_to_string(lst_of_items)))
print()
print()
financial_advisor(3000, 2000, lst_of_items)
print()
print()
create_goal("Laptop", 2000, "2 months", lst_of_items, 3000)
