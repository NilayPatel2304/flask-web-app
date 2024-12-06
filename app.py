from flask import Flask, render_template, request
from werkzeug.urls import unquote  # Use unquote instead of url_quote

app = Flask(__name__)

@app.route('/')
def index():
    # Example of using unquote (if needed in your app)
    query_param = request.args.get('some_param', '')
    decoded_param = unquote(query_param)
    
    return render_template('index.html', decoded_param=decoded_param)

if __name__ == '__main__':
    app.run(debug=True)
