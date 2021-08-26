from flask import Flask, redirect, url_for

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
# rule = represents URL binding with the function.
# options = list of parameters to be forwarded to the underlying Rule object.
@app.route(rule="/")
def home():
    return "Home"


# http://localhost:5000/home_1
@app.route(rule="/home_1")
def home_1():
    return "Welcome to home_1"


# http://localhost:5000/home_2
def home_2():
    return "Welcome to home_2"


app.add_url_rule("/home_2/", "home_2", home_2)


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
        return redirect(url_for(endpoint="user_login", platform_version=platform_version, user_name=user_name, user_id=user_id))


if __name__ == "__main__":

    app.debug = True
    app.run(host="localhost", port=5000, debug=True)
