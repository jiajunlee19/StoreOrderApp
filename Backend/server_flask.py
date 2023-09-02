from flask import Flask, request, jsonify
import json
from db_connection import connect_mysql
import dao_uom
import dao_product

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


connection = connect_mysql()


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = dao_uom.get_uom(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getProduct', methods=['GET'])
def get_product():
    response = dao_product.get_product(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = dao_product.insert_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = dao_product.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Store Order Management Application...")
    app.run(port=5000)
