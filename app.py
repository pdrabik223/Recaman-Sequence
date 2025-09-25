from flask import Flask, make_response, render_template, request, send_file

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    dict = request.form
    # for key in dict:
    print(dict)
    return render_template("index.html")


@app.route("/svg_file", methods=["GET", "POST"])
def svg_file():
    response = make_response("assets/recman_circles.svg", 200)
    response.mimetype = "text/plain"
    # return send_file("static/assets/recman_circles.svg", mimetype="image/svg")
    return response


if __name__ == "__main__":
    app.run(debug=True)
