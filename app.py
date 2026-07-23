"""拾刻记 - 每日灵感卡片 官方网站"""
from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def index():
    """首页"""
    return send_file("index.html")


@app.route("/about")
def about():
    """关于页"""
    return send_file("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
