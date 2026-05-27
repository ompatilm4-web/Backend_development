from flask import Flask, render_template, request, jsonify

import Core.database as db
from Core.LinkedIn_data import scrape_jobs

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        try:

            df = db.Get_Data()

            email = request.form.get('email')
            password = request.form.get('password')
            user = df[(df['EMAIL'] == email) & (df['PASSWORD'] == password)]
            if not user.empty:
                return render_template('home.html')
            else:
                return "Invalid Credentials"
        except Exception as e:
            return f"Database Error: {e}"

    return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/jobs')
def jobs():

    keyword = request.args.get(
        'keyword',
        'python'
    )

    jobs_list = scrape_jobs(keyword)

    return render_template(
        'jobs.html',
        jobs=jobs_list,
        keyword=keyword
    )



@app.route('/savedjobs')
def saved():
    return render_template('saved.html')



@app.route('/api/jobs')
def api_jobs():

    keyword = request.args.get(
        'keyword',
        'python'
    )

    jobs_list = scrape_jobs(keyword)

    return jsonify(jobs_list)



if __name__ == '__main__':

    app.run(
        debug=True,
        port=8080
    )