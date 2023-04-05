from mysql import cursor, db

def add_log(text,user):
    sql = ("INSERT INTO LOGS (text,user) VALUES (%s,%s)")
    cursor.execute(sql,(text,user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

#add_log("This is Log one","New1")
#add_log("This is Log two","New2")
#add_log("This is Log three","New3")
#add_log("This is Log four","New4")


## fetching multiple records from table
def get_logs():
    sql = ("SELECT * FROM LOGS ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
    print(row)

## getting a single record from table 
def get_log():
    sql = ("SELECT * FROM LOGS WHERE ID = %s")
    cursor.execute(sql)
    result = cursor.fetchone()
    for row in result:
    print(row)
    
#get_logs()