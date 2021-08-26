from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


# http://localhost:5000/platform/0.1/vyshnav/69/
@app.route(rule="/<float:platform_version>/<user_name>/<int:user_id>/")
def user_login(platform_version, user_name, user_id):
    return f"Welcome to platform({platform_version}): {user_name}: {user_id}"


# http://localhost:5000/platform/0.1/admin/1
@app.route(rule="/<float:platform_version>/admin/")
def admin_login(platform_version):
    return f"Welcome to platform({platform_version}): Admin"


@app.route(rule="/platform/<float:platform_version>/<user_name>/<int:user_id>/")
def platform(platform_version, user_name, user_id):
    if user_name == "admin":
        return redirect(url_for(endpoint="admin_login", platform_version=platform_version))
    else:
        return redirect(
            url_for(endpoint="user_login", platform_version=platform_version, user_name=user_name, user_id=user_id))


@app.route(rule="/login", methods=["POST", "GET"])
def login():
    # result = request.form
    # return render_template("result.html", result=result)
    if request.method == "POST":
        platform_version = request.form["platform_version"]
        user_name = request.form["user_name"]
        user_id = request.form["user_id"]
        return redirect(url_for(endpoint="platform", user_name=user_name, platform_version=platform_version, user_id=user_id))
    else:
        platform_version = request.args.get("platform_version")
        user_name = request.args.get("user_name")
        user_id = request.args.get("user_id")
        return redirect(url_for("platform", user_name=user_name, platform_version=platform_version, user_id=user_id))


@app.route(rule="/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000, debug=True)
