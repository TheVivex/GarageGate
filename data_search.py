import mysql.connector
def SQL_request(request):
    try:

        mydb = mysql.connector.connect(
                host="192.168.232.127",
                user="gate",
                password="gate",
                database="gate"
                )
        mycursor = mydb.cursor()
        mycursor.execute(request)
        myresult = mycursor.fetchall()
        back = list(myresult)
        if len(back) == 0:
            x = ("test", 0)
        else:
            x = back[0]
        return x
    except:
        print("Cannot connect with database")