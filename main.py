from flask import Flask,render_template,jsonify


app = Flask(__name__)


JOBS = [
    {
        "id": 1,
        "title": "Data analyst",
        "location": "San Fransisco",
        "salary":"100$"
    },
     {
        "id": 2,
        "title": "Cloud Engineer",
        "location": "Remote",
    },

     {
        "id": 3,
        "title": "Full-Statck_Developer",
        "location": "Lagos,Nigeria",
        "salary": "260$"
    }
]

@app.route("/")

def hello_Harby():
    return render_template("index.html",jobs = JOBS,companyname = "harby")


@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)



if __name__ == "__main__":
    app.run(debug=True)