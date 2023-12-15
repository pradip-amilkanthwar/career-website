from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': '1',
    'title': 'Lead Engineer',
    'location': 'India Pune'
}, {
    'id': '2',
    'title': 'Data Analyst',
    'location': 'India Pune',
    'salary': '2000000'
}, {
    'id': '3',
    'title': 'Data Scientist',
    'location': 'India Pune/Mumbai',
    'salary': '2000000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Avni Infotech')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
