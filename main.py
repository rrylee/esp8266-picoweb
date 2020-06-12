import picoweb

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("I can show you a table of <a href='squares'>squares</a>.")


@app.route("/json")
def squares(req, resp):
    yield from picoweb.jsonify(resp, {"key": "name"})


app.run(debug=True, host="0.0.0.0")
