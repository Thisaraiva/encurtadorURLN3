import redis
import pyshorteners
from flask import Flask, jsonify, request
from pymongo import MongoClient


# Configurações
app = Flask(__name__)

app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300
app.config['API_KEY'] = 'abc123xyz'

# Cria uma instância do Redis
redis_client = redis.Redis(host='localhost', port=6379)

# Cria uma instância do Flask
app = Flask(__name__)

# Cria uma instância do cliente MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')

# Seleciona o banco de dados do MongoDB
db = mongo_client['encurtador_db']

# Seleciona a coleção para armazenar as URLs encurtadas
url_collection = db['urls']

@app.route('/encurtar', methods=['POST'])
def encurtar():
    url = request.json.get('url')

    # Verifica se a URL está presente no cache
    cached_url = redis_client.get(url)
    if cached_url:
        print("URL encontrada no cache.")
        return jsonify({'url_encurtada': cached_url.decode('utf-8')})

    # Verifica se a URL está presente no banco de dados
    db_result = url_collection.find_one({'url': url})
    if db_result:
        print("URL encontrada no banco de dados.")
        return jsonify({'url_encurtada': db_result['url_encurtada']})

    try:
        # Cria uma instância do encurtador
        shortener = pyshorteners.Shortener()

        # Encurta a URL usando o TinyURL
        short_url = shortener.tinyurl.short(url)

        # Armazena a URL encurtada no cache
        redis_client.set(url, short_url)

        # Armazena a URL encurtada no banco de dados
        url_collection.insert_one({'url': url, 'url_encurtada': short_url})

        # Retorna a URL encurtada
        return jsonify({'url_encurtada': short_url})
    except pyshorteners.exceptions.ShorteningErrorException:
        return jsonify({'error': 'Ocorreu um erro ao encurtar a URL.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
