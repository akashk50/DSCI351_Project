import pandas as pd
from pymongo import MongoClient


def loadMongo():
    questions_df = pd.read_csv("questions.csv")
    
    client = MongoClient('localhost', 27017)
    db = client['dsci351-project']
    db.questions.insert_many(questions_df.to_dict('records'))


def main():
    substring = ""
    regex_pattern = {'$regex': substring, '$options': 'i'}
    client = MongoClient('localhost', 27017)
    db = client['dsci351-project']
    questions = db.questions
    for a in questions.find({"Question": regex_pattern, "Difficulty": 2}):
        print(a)

main()

def deleteDB():
    client = MongoClient('localhost', 27017)
    client.drop_database('questions')
    client.drop_database('dsci351-project')