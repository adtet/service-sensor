import mysql.connector
import json
from datetime import datetime

def sql_connection():
    sql = mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="",
                                  database="db_ta")
    return sql

def input_data_sensor(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    db = sql_connection
    cursor = db.cursor()    
    try:
        cursor.execute("INSERT INTO `tabelsensor`(`A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `I`, `J`, `K`, `L`, `M`, `N`, `O`, `P`, `Q`, `R`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)

        
    