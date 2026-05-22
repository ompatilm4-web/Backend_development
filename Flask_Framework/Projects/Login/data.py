import sqlite3 as st 

def CreateTable():
    connection=st.connect("/home/om/Desktop/Backend/Flask_Framework/Projects/Login/UserData.db")
    cursor=connection.cursor()
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS UserData(
                       NAME VARCHAR (50) ,
                       EMAIL VARCHAR (50) PRIMARY KEY ,
                       PASSWORD VARCHAR (12)
                       )
                   ''')
    connection.commit()
    connection.close()
    
    
# CreateTable()

def InsertData(name,email,password):
    connection=st.connect("/home/om/Desktop/Backend/Flask_Framework/Projects/Login/UserData.db")
    cursor=connection.cursor()
    
    cursor.execute('''
                   INSERT INTO UserData (NAME,EMAIL,PASSWORD) VALUES (?,?,?)
                   ''',(name,email,password))
    connection.commit()
    connection.close()
    
    
    
def fetch_Data():
    connection = st.connect("/home/om/Desktop/Backend/Flask_Framework/Projects/Login/UserData.db")
    cursor =connection.cursor()
    cursor.execute('''
                   SELECT * FROM UserData
                   ''')
    data=cursor.fetchall()
    connection.close()
    return data



    