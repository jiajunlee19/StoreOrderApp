from flask import (Flask, request, jsonify, render_template)
import json
from Backend.db_connection import connect_mysql
from Backend import dao_member
from Backend import dao_member_level
from Backend import dao_uom
from Backend import dao_product
from Backend import dao_order
from Backend import dao_order_item

app = Flask(__name__)
app.json.sort_keys = False

connection = connect_mysql()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/getMember', methods=['GET'])
def get_member():
    response = dao_member.get_member(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getMemberLevel', methods=['GET'])
def get_member_level():
    response = dao_member_level.get_member_level(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


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


@app.route('/getOrder', methods=['GET'])
def get_order():
    response = dao_order.get_order(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getOrderItem', methods=['GET'])
def get_order_item():
    response = dao_order_item.get_order_item(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertMember', methods=['POST'])
def insert_member():
    request_payload = request.form['data']
    response = dao_member.insert_member(connection, request_payload)
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


@app.route('/deleteMember', methods=['POST'])
def delete_member():
    response = dao_member.delete_member(connection, request.form['member_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return render_template('member.html')


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
    app.run(port=5000, debug=True)
