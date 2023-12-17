from flask import Flask, jsonify, render_template

from database import get_db_connection

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
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Sample Career Website')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


@app.route('/career')
def career_opportunities():
  return render_template('career.html',
                         jobs=JOBS,
                         company_name='Sample Career Website')


@app.route('/api/books')
def index():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM books;')
  books = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('index.html', books=books)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
