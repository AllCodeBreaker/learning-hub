from flask import Flask, render_template, abort
import learn
from learn import ALLOWED_DEPARTMENTS, get_jobs, get_job, get_placements, get_placement

app = Flask(__name__, static_folder="static")


@app.get("/")
def home():
    # landing page showing departments and options
    placements = get_placements()
    return render_template("index.html", departments=ALLOWED_DEPARTMENTS, placements=placements)


@app.get("/<dept>")
def department(dept: str):
    dept_key = dept.lower()
    if dept_key not in ALLOWED_DEPARTMENTS:
        return render_template("404.html"), 404
    # Render the department overview with choices (learning / jobs)
    return render_template("department.html", dept=ALLOWED_DEPARTMENTS[dept_key], dept_key=dept_key, option=None)


@app.get("/<dept>/<option>")
def department_option(dept: str, option: str):
    dept_key = dept.lower()
    opt = option.lower()
    if dept_key not in ALLOWED_DEPARTMENTS:
        return render_template("404.html"), 404
    if opt not in ("learning", "jobs"):
        return render_template("404.html"), 404
    return render_template("department.html", dept=ALLOWED_DEPARTMENTS[dept_key], dept_key=dept_key, option=opt)


@app.get("/<dept>/jobs")
def department_jobs(dept: str):
    dept_key = dept.lower()
    if dept_key not in ALLOWED_DEPARTMENTS:
        return render_template("404.html"), 404
    jobs = get_jobs(dept_key) or []
    return render_template("jobs.html", dept=ALLOWED_DEPARTMENTS[dept_key], dept_key=dept_key, jobs=jobs)


@app.get("/<dept>/jobs/<job_id>")
def department_job_detail(dept: str, job_id: str):
    dept_key = dept.lower()
    if dept_key not in ALLOWED_DEPARTMENTS:
        return render_template("404.html"), 404
    job = get_job(dept_key, job_id)
    if not job:
        return render_template("404.html"), 404
    return render_template("job_detail.html", dept=ALLOWED_DEPARTMENTS[dept_key], dept_key=dept_key, job=job)


@app.get("/<dept>/placements")
def department_placements(dept: str):
    dept_key = dept.lower()
    if dept_key not in ALLOWED_DEPARTMENTS:
        return render_template("404.html"), 404
    placements = get_placements(dept_key) or []
    return render_template("placements.html", dept=ALLOWED_DEPARTMENTS[dept_key], dept_key=dept_key, placements=placements)


@app.get("/<dept>/placements/<placement_id>")
def department_placement_detail(dept: str, placement_id: str):
    dept_key = dept.lower()
    if dept_key not in ALLOWED_DEPARTMENTS:
        return render_template("404.html"), 404
    placement = get_placement(dept_key, placement_id)
    if not placement:
        return render_template("404.html"), 404
    return render_template("placement_detail.html", dept=ALLOWED_DEPARTMENTS[dept_key], dept_key=dept_key, placement=placement)


if __name__ == "__main__":
    app.run(debug=True)

