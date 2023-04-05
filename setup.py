
import mysql.connector
from mysql.connector import errorcode
from mysql import cursor

Db_Name="DataBase"

TABLES = {}

TABLES["LOGS"] = (
    "CRATE TABLE 'LOGS'('ID' int(11) NOT NULL AUTO_INCREMENT,"
    "'text' varchar(250) NOT NULL,"
    "'user' varchar(250) NOT NULL,"
    "'created' datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY ('ID')"
    ") ENGINE-InnoDB"
)

def create_tables():
    cursor.execute("USE {}".format(Db_Name))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating Table ({})".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("TABLE ALREADY EXIST")
            else:
                print(err.msg)


def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXIST {} DEFAULT CHARACYTER SET ".format(Db_Name))
    print("Database{} created".format(Db_Name))

create_database()

