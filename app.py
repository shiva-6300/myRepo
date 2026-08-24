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

        if "," not in array_input:
            result = "Invalid format! Please enter numbers separated by commas. Example: 10,20,30,40"

        else:
            try:
                array = [int(x.strip()) for x in array_input.split(",")]

                target = int(request.form["target"])

                result = linear_search(array, target)

                if result == 1:
                    result = "Element Found In The List"
                else:
                    result = "Sorry... Element Not Found"

            except ValueError:
                result = "invalid input! Please enter numbers only."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
