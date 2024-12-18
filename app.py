from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    return jsonify({'message': 'Search endpoint'})

if __name__ == '__main__':
    app.run(debug=True)