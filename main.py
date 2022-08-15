from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<h1>Hello World</h1>"

    @app.route("/uoa")
    def show_uoapage():
        return render_template("index.html")

    @app.route("/<name>")
    def show_name(name: str):
        page = render_template("hello.html", user_name=name)
        return page

    @app.route("/result/<mark>")
    def show_grade(mark: str):
        try:
            mark = int(float(mark))
        except ValueError:
            return "<h3>Invalid mark!</h3>"
        if mark >= 90:
            grade = "A+"
        elif 85 <= mark < 90:
            grade = "A"
        elif 80 <= mark < 85:
            grade = "A-"
        elif 75 <= mark < 80:
            grade = "B+"
        else:
            grade = "[D-, B]"
        result_page = render_template("result.html", user_grade=grade)
        return result_page

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, port=8000)

