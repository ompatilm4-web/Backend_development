from flask import Flask, render_template, request, jsonify
import requests
import bs4

import Core.database as db

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        df = db.Get_Data()

        email = request.form.get('email')
        password = request.form.get('password')

        user = df[
            (df['EMAIL'] == email) &
            (df['PASSWORD'] == password)
        ]

        if not user.empty:
            return render_template('home.html')

        else:
            return "Invalid Credentials"

    return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/jobs')
def jobs():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = "https://www.linkedin.com/jobs/search/?keywords=python"

    response = requests.get(url, headers=headers)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    jobs_list = []

    # Example LinkedIn parsing
    job_cards = soup.find_all('div', class_='base-search-card')

    for job in job_cards:

        title = job.find('h3')
        company = job.find('h4')
        location = job.find('span', class_='job-search-card__location')

        jobs_list.append({
            "title": title.text.strip() if title else "N/A",
            "company": company.text.strip() if company else "N/A",
            "location": location.text.strip() if location else "N/A"
        })

    return render_template(
        'jobs.html',
        jobs=jobs_list
    )



@app.route('/savedjobs')
def saved():
    return render_template('savedjobs.html')



@app.route('/api/jobs')
def api_jobs():

    sample_jobs = [
        {
            "title": "Python Developer",
            "company": "Microsoft",
            "location": "Remote"
        }
    ]

    return jsonify(sample_jobs)



if __name__ == '__main__':
    app.run(debug=True, port=8080)