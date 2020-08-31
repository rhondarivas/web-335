#
# ======================================================
# Title:  – Querying and Creating Documents
# Author: Professor Krasso
# Modified by: Rhonda Rivas
# Date:   8-31-2020
# Description: Python Assignment 9.2
#=====================================================
#
from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {

    "first_name": "Claude",

    "last_name": "Monet",

    "email": "waterlillies@french.com",

    "employee_id": "0000877",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000877"}))
