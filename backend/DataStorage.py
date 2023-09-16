import csv
import matplotlib
import seaborn
import pandas as pd

def interpret_and_write_data(payload: str):

    item_names = payload.split("\n")
    
    for i in item_names:
        month, item, cost = i.split(" ")[0], i.split(" ")[1], i.split(" ")[2]
        data = [month.strip(" "), item.strip(" "), cost.strip(" ")]

        with open('SpendingHistory.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    

        
    



interpret_and_write_data("April Shoes $400\nMay Clothes $200\nJune Car $1000")