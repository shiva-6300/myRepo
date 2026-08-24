from flask import Flask, render_template, request

app = Flask(__name__)


def linear_search(array, target):

    for i in array:

        if i == target:
            return 1

    return -1


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        # Get array from HTML
        array_input = request.form["array"]

        # Convert "10,20,30,40" into [10, 20, 30, 40]
        array = [int(x) for x in array_input.split(",")]

        # Get target
        target = int(request.form["target"])

        # Call your Python function
        result = linear_search(array, target)

        if result == 1:
            result = "YOU PIG"
        else:
            result = "Sorry... Not Found"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)