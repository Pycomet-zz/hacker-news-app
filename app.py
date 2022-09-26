from config import *
from utils import *
from forms import SearchForm
from api import api_bp


@app.route("/", methods=["GET", "POST"])
def index():

    form = SearchForm(request.form)
    if request.method == "POST":

        keys = [r for r in request.form.keys() if r not in ["csrf_token", "search"]]

        types = ",".join(keys)
        search = request.form.get("search") or ""

        fetch_req = requests.post(
            "http://127.0.0.1:8080/api/v1/news",
            json={"search": search, "types": types},
        ).json()

    else:
        fetch_req = requests.get("http://127.0.0.1:8080/api/v1/news").json()

    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="per_page", per_page=10
    )
    total = len(fetch_req["data"])

    next_stop = offset + per_page
    pagination_data = fetch_req["data"][offset:next_stop]

    pagination = Pagination(
        page=page, per_page=per_page, total=total, css_framework="materialize"
    )

    return (
        render_template(
            "index.html",
            data=pagination_data,
            page=page,
            per_page=10,
            pagination=pagination,
            form=form,
        ),
        200,
    )


# Sync Job
@scheduler.task("interval", id="sync_job", seconds=300, misfire_grace_time=500)
def sync_job():
    print("Job 1 executed")
    start = time.time()

    new_stories = requests.get(
        "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
    ).json()[:100]

    for uid in new_stories:

        status = asyncio.run(sync_HN_to_DB(uid=uid))

    stop = time.time()
    speed = stop - start
    print(f"Completed {len(new_stories)} Sync In - {speed}")


if __name__ == "__main__":
    app.register_blueprint(api_bp)
    app.run(host="0.0.0.0", port="8080")
