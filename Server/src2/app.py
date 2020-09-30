from flask import Flask, redirect, render_template, request, Response

from spacyclient import get_client, DEFAULT_MODEL

app = Flask(__name__)
app.config['FLASK_DEBUG'] = True


@app.route("/")
def home(): 
    return redirect(f'/{DEFAULT_MODEL}', status=302)


@app.route("/<model>", methods=['GET'])
def form(model):
    client = get_client(model)
    if not client:
        return Response(status=500)
    return Response("""<http>
    <head></head>
    <body>
    <form method='POST'>
    <textarea id='text' name='text'></textarea>
    <button id='submit' name='submit'>Submit</button>
    </form>
    </body>
    </http>""")


@app.route("/<model>", methods=['POST'])
def analyze(model):
    client = get_client(model)
    if not client:
        return Response(status=500)
    text = request.form['text']
    result = client.process_text(text)
    if not result:
        return Response(status=400)
    return result  # auto-jsonified
