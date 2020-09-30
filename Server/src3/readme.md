# src3 directory

A revision of the http app to a different design spec in which the system simply loads all models, and runs against a given sentence

## Running this
terminal inside /src3

export FLASK_APP=app.py
flask run

## FirstTest.json

This is the output printed by SimpleSpacyClient running against SpacyClient which loaded the same model twice as a simulation of a multi-model exercise.

Since one knows the model load order built into SimpleSpacyClient init, then the ordering of those results maps directly to which model produced each result.
