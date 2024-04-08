import psycopg2 as pc
from config import *
import usercls

try:
        connection = pc.connect(host = host, user = user, password = password) 
        connection.autocommit = True


        with connection.cursor() as cursor:
            cursor.execute(
                "Create table infouser (id BIGINT NOT NULL PRIMARY KEY, age BIGINT NOT NULL);"
                )
            
            print("TABLE IS created ")

except Exception as ex:
        print("ERROR SQL: ",ex)
        pass
finally:
        connection.close()



def reguser(age):
    _ = usercls.User(age)

    connection = pc.connect(host = host, user = user, password = password) 
    connection.autocommit = True

    try:
        
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO infouser(id, age) values ({_.get_id()}, {_.get_age()})"
                )
            print("Succesfuly registered!")

    except Exception as ex:
        print("ERROR SQL: ",ex)
    finally:
        connection.close()

reguser(19);
reguser(21);
reguser(48);


def getuser(id):
    connection = pc.connect(host = host, user = user, password = password) 
    connection.autocommit = True

    try:
        
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM infouser WHERE id = {id};"
                )
            _ = cursor.fetchone()
            print("USER INFO: id = ", _[0], " age = ", _[1])

    except Exception as ex:
        print("ERROR SQL: ",ex)
    finally:
        connection.close()

getuser(2);