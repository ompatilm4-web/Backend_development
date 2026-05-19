# GET and POST 
from flask import Flask ,render_template,request

app=Flask(__name__) # giving an instance for the Class Flask 

@app.route('/')
def Wekcome ():
    return render_template('home.html')

@app.route("/about")
def About():
    return render_template("about.html")

@app.route('/Index')
def index ():
    return render_template("index.html")

@app.route('/form',methods=['GET','POST'])
def form ():
    if request.method=='POST':
        name=request.form.get('username')
        return render_template('sucess.html')
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def Submit ():
    if request.method=='POST':
        name=request.form.get('username')
        return render_template("success.html")
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)