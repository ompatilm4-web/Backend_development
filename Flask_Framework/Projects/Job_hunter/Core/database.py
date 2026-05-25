import sqlite3 as st 
import pandas as pd



def Create ():
    connection=st.connect('/home/nova/Desktop/Backend/Backend_development/Flask_Framework/Projects/Job_hunter/user.db')
    cursor=connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS USERS (
                   EMAIL VARCHAR(50) PRIMARY KEY,
                   PASSWORD VARCHAR(50)
                   )
                   ''')
    connection.commit()
    connection.close()




def insert_users():
    # Connect to database
    connection = st.connect(
        '/home/nova/Desktop/Backend/Backend_development/Flask_Framework/Projects/Job_hunter/user.db'
    )

    cursor = connection.cursor()

    # Multiple user entries
    users = [
        ('ompatil1@gmail.com', 'Pooja@123'),
        ('ompatil2@gmail.com', 'Rahul@123'),
        ('ompatil3@gmail.com', 'Amit@123'),
        ('ompatil4@gmail.com', 'Sneha@123'),
        ('ompatil5@gmail.com', 'Rohit@123'),
        ('ompatil6@gmail.com', 'Kiran@123'),
        ('ompatil7@gmail.com', 'Priya@123'),
        ('ompatil8@gmail.com', 'Neha@123'),
        ('ompatil9@gmail.com', 'Ankit@123'),
        ('ompatil10@gmail.com', 'Pallavi@123')
    ]

    # Insert multiple records
    cursor.executemany(
        '''
        INSERT INTO USERS (EMAIL, PASSWORD)
        VALUES (?, ?)
        ''',
        users
    )

    # Save changes
    connection.commit()

    # Close connection
    connection.close()

    print("Users inserted successfully!")




def Get_Data():
    connection = st.connect('/home/nova/Desktop/Backend/Backend_development/Flask_Framework/Projects/Job_hunter/user.db')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM USERS')
    data=cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    connection.close()

    df = pd.DataFrame(data, columns=columns)
    return df 



