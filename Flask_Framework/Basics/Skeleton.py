from flask import Flask 


'''
It Creates an instance of the class Flask 
Which will be your Web server gateway interface Application  
'''

app=Flask(__name__) # giving an object to the Class Flask 



@app.route("/")
def Welcome ():
    return f"Welcome to the Flask Application ! "

if __name__ == "__main__" :   # Giving a Entry point to the Application 
    app.run(debug=True,port=8080)
    
    