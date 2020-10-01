from flask import Flask, redirect, request, Response

from spacyclient import get_client, DEFAULT_MODEL, CLIENTS

app = Flask(__name__)
app.config['FLASK_DEBUG'] = True


@app.route("/")
def home(): 
    return redirect(f'/{DEFAULT_MODEL}')


@app.route("/<model>", methods=['GET'])
def form(model):
    client = get_client(model)
    if not client:
        return Response(status=404)
    return Response("""<http>
    <head></head>
    <body>
    <form method='POST'>
    <textarea id='text' name='text'></textarea>
    <button id='submit' name='submit'>Submit</button>
    </form>
    </body>
    </http>""")


def process_request(client, request):
    if request.json:
        return client.process_json(request.json)
    elif request.form:
        text = request.form['text']
        return client.process_text(text)


@app.route("/<model>", methods=['POST'])
def analyze(model):
    client = get_client(model)
    if not client:
        return Response(status=404)
    result = None
    try:
        result = process_request(client, request)
        assert result
    except Exception as e:
        return Response(str(e), status=500)
    return result  # auto-jsonified


@app.route("/all", methods=['POST'])
def analyze_all():
    result = {}
    models = []
    if request.json:
        models = request.json.get('models', [])
    elif request.forms:
        models = request.forms.get('models', [])
    for model in models:
        get_client(model)
    for name, client in CLIENTS.items():
        if not client:
            continue
        result[name] = process_request(client, request)
    return result
