from flask import Flask, render_template, request, jsonify
from services.dbpedia_service import DBPediaService

app = Flask(__name__)
dbpedia_service = DBPediaService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    try:
        results = dbpedia_service.search_entity(query)
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 700

if __name__ == '__main__':
    app.run(debug=True)