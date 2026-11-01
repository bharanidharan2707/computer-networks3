
from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test")
def test_speed():

    try:
        st = speedtest.Speedtest()

        st.get_best_server()

        download = round(st.download() / 1_000_000, 2)
        upload = round(st.upload() / 1_000_000, 2)
        ping = round(st.results.ping, 2)

        return jsonify({
            "download": download,
            "upload": upload,
            "ping": ping
        })

    except Exception:
        return jsonify({
            "error": "Speed test failed. Check your internet connection."
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5002)
