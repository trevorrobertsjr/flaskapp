from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
        return """
        <!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>A Basic HTML5 Web Page</title>
  <meta name="description" content="A simple HTML5 Template.">
  <meta name="author" content="Containers AAoD">
</head>

<body>
  Hello, Containers AAoD!
</body>
</html>
        """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')