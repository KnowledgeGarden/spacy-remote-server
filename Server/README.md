# spacy-remote-server
Remote, multimodel SpaCy agent

## Background
This is fundamentally a JSON server driving an instance of SpaCy. Its purpose is to exercise several different models on a given {SentenceId, SentenceText} pair and return a JSON object which is the assembly of all model results on the given sentence.

A simple client.py is included from the development and testing process.

In production, the client in play lives elsewhere on a LAN and, regardless of its implementation, serves the purpose of sending sentences to this and any other agent in the ecosystem and marshalling the results for futher NLP processing.

A Java text client is included or the HTTP version (/src3)

## Reuirements
System tested on Python 3.7+
* pip3 install flask
* pip3 install spacy
* python3 -m spacy download en_core_web_lg
* pip3 install scispacy
* install the large models found [here](https://allenai.github.io/scispacy/)
  

### SciSpacy Model Shortcuts which might be inaccurate
* pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_lg-0.2.5.tar.gz
* pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_ner_craft_md-0.2.5.tar.gz
* pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_ner_jnlpba_md-0.2.5.tar.gz
* pip 3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_ner_bc5cdr_md-0.2.5.tar.gz
* pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_ner_bionlp13cg_md-0.2.5.tar.gz



## Work In Progress
Actual development work is being done in /src3; when all algorithms are worked out, code cleanup will change to a single /src directory.

## Running
TODO

