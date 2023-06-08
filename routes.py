from flask      import Flask, request, make_response, jsonify, send_file
from dl         import download
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def dl():
    if request.method == "POST":
        try:
            req     = request.get_json()
            url     = req["url"]
            path    = download(url)

            return make_response(send_file(path, as_attachment=True), 200)
        except:
            return make_response(jsonify({"error": "No valid URL was given. \
Make a JSON POST request with an 'url' key with the URL of your YouTube video."}), 400)
    else:
        return make_response(jsonify({"error": "405 method not allowed. Just make POST requests."}), 405)

if __name__ == "__main__":
    app.run(debug=True)
