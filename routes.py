from flask      import Flask, request, make_response, jsonify, send_file
from dl         import download
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def dl():
    req     = request.get_json()
    url     = req["url"]
    path    = download(url)

    return make_response(send_file(path, as_attachment=True), 200)

if __name__ == "__main__":
    app.run(debug=True)
