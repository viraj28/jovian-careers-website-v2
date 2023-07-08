from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 1,
  'title': 'Front end Engineer',
  'location': 'Remote',
}, {
  'id': 1,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': '$ 150,000'
}]





@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/api/job/<id>")
def list_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  else:
    return render_template("jobpage.html", job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0')
