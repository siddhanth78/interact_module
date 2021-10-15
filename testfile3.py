import pandas as pd
import numpy as np
import mysql.connector as sql

mydb = sql.connect(user = "root",
                    passwd = "teju1sid",
                    host = "localhost")

if(mydb.is_connected()):
    print("Connection established.")
else:
    print("Connection failed.")