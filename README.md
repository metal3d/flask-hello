# A simple example to use Flasl

This is a simple example that I use to explain how to build a Flask application.

Installation with virtualenv:

```bash
python3 -m venv v
source v/bin/activate
pip3 install -r requirements.txt
FLASK_APP=main:app FLASK_DEBUG=1 flask run
```

Install "httpie" package from your Unix(Like) distribution.

Then in another terminal:
```bash
$ http :5000
$ http :5000/greeting/Jon

# test json {"name": "Jon"}
$ http :5000/echo name=Jon

# test with fogotten "name" key should give an error
$ http :5000/echo foo=bar
```
