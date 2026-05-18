# We will be Integrating the Html in the flask 

from flask import Flask,render_template,request

'''
It Creates an instance of the class Flask 
Which will be your Web server gateway interface Application  
'''

app=Flask(__name__)

@app.route("/")
def Welcome():
    return "<html><H1>Welcome To The Home Page ! </H1>We will be Creating Good Web Pages From Now </html>"

@app.route("/Index")
def Index ():
    return render_template("index.html")

@app.route("/About")
def About ():
    return render_template("about.html")


@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        name = request.form.get('username')

        return f"Hello {name} Sir"

    return render_template('form.html')


if __name__ == "__main__" :
    app.run(debug=True)
    
