# A simple example to use Flasl

This is a simple example that I use to explain how to build a Flask application.

Installation with virtualenv:

```bash
python3 -m venv v
source v/bin/activate
pip3 install -r requirements.txt
FLASK_APP=main:app FLASK_DEBUG=1 flask run
```
