# will see how the custom URLs can be made 
# learn about the Jinja 2 Template Engine 


# Syntax For Jinja2 template engine 

# {} this used for the Loops 
# {%....%} this is Used for the Conditional Statements 
# {#....#} this Used for the Comments 
#{{}} this Used for the Direct Datatype 




from flask import Flask ,render_template,request,redirect,url_for




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



@app.route('/submit',methods=['GET','POST'])
def Submit ():
    if request.method=='POST':
        name=request.form.get('username')
        return render_template("success.html")
    return render_template('form.html')


@app.route('/successresult/<int:Score>')
def success_Result (Score):
    res=''
    if Score>=50:
        res='PASS'
    else:
        res='FAIL'
        
    exp={'Score':Score,"Result":res}
    
    return render_template(
        'successresult.html',
        exp=exp
    )


@app.route("/successif/<Score>")
def If_Score (Score):
    return render_template('Result.html',results=int(Score))

@app.route("/successif/<Score>")
def reScore (Score):
    return render_template('Result.html',results=int(Score)) 





@app.route('/success/<int:Score>')
def success (Score):
    res=''
    if Score>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('success.html',result=res,score=Score)

@app.route('/Fail/<int:Score>')
def Fail (Score): 
    return render_template('success.html',result=Score, score =Score)


@app.route('/submit',methods=['POST','GET'])
def get_result():
    total_marks=0
    if request.method=='POST' :
        subject_1=float(request.getresult.get('sub1'))
        subject_2=float(request.getresult.get('sub2'))
        subject_3=float(request.getresult.get('sub3'))
        subject_4=float(request.getresult.get('sub4'))
        subject_5=float(request.getresult.get('sub5'))
        
        total_marks=(subject_1+subject_2+subject_3+subject_4+subject_5)/5
        return redirect(url_for('success',score=total_marks))
        
        
        
        

        

if __name__ == "__main__":
    app.run(debug=True,port=8080)