from config import *
from api import api_bp


@app.route("/")
@app.route("/index")
def default_route():
    return render_template("index.html"), 200


# Sync Job
@scheduler.task('interval', id='sync_job', seconds=60, misfire_grace_time=900)
def sync_job():
    print('Job 1 executed')


if __name__ == "__main__":
    app.register_blueprint(api_bp)
    app.run(host="0.0.0.0", port="8080")
