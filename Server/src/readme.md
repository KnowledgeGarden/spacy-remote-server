# src directory

This is the full platform code after many experiments.
This is code now tested with this curl:

`curl -d '{"models":["en_ner_jnlpba_md","en_ner_bc5cdr_md","en_ner_bionlp13cg_md","en_ner_craft_md","en_core_web_lg","en_core_sci_lg"],"text":"CO2 causes climate change"}' -H "Content-Type: application/json" -X POST http://localhost:5000/all`

Note that all of the models listed are those which were pre-installed.

## Virtual Environment

Use this directory for a venv. Given we are using Python 3+:
* Create: python -m venv venv
* Activate: . venv/bin/activate

## Running
From the Flask instructions
export FLASK_APP=app.py
flask run --host=0.0.0.0

