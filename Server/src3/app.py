from flask import Flask, redirect, render_template, request, Response

from spacyclient import SpacyClient
client = SpacyClient()

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


@app.route("/analyze/", methods=['POST'])
def analyze():
    jsonObject = request.json
    print('A', jsonObject)
    text = jsonObject['text']
    print('B', text)
    result = client.process_text(text)   
    if not result:
        return Response(status=400)
    print('C', result)
    return result  # auto-jsonified
