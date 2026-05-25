from flask import Flask,render_template,request,redirect


app= Flask (__name__)

@app.route('/',methods=['GET','POST'])
def home ():
    return render_template('home.html')

@app.route('/jobs',methods=['GET'])
def Jobs():
    return render_template('jobs.html')

@app.route('/saved',methods=['GET'])
def Saved ():
    return render_template('saved.html')

if __name__ == '__main__':
    app.run(debug=True,port=8060)
    