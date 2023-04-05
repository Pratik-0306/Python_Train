import mysql.connector 

config={
    "user":"root",
    "password":"password",
    "host":"localhost"
}

db=mysql.connector.connect(**config)
cursor=db.cursor()