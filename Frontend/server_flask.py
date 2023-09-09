from flask import (Flask, request, jsonify, render_template)
from datetime import datetime
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
def index():
    return render_template('index.html')


@app.route('/member', methods=['GET'])
def member():
    return render_template('member.html')


@app.route('/member_level', methods=['GET'])
def member_level():
    return render_template('member_level.html')


@app.route('/uom', methods=['GET'])
def uom():
    return render_template('uom.html')


@app.route('/product', methods=['GET'])
def product():
    return render_template('product.html')


@app.route('/order', methods=['GET'])
def order():
    return render_template('order.html')


@app.route('/order_item', methods=['GET'])
def order_item():
    return render_template('order_item.html')


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
    data_dict = {
        "member_name": request.form['member_name'],
        "member_password": request.form['member_password'],
        "member_bonus_points": request.form['member_bonus_points'],
        "member_created_date": datetime.now(),
        "member_updated_date": datetime.now()
    }
    response = dao_member.insert_member(connection, data_dict)
    if 'error' in response:
        return response
    else:
        return render_template('member.html')


@app.route('/updateMember', methods=['POST'])
def update_member():
    data_dict = {
        "member_password": request.form['member_password'],
        "member_bonus_points": request.form['member_bonus_points'],
        "member_updated_date": datetime.now()
    }
    member_id = request.form['member_id']
    response = dao_member.update_member(connection, data_dict, member_id)
    if 'error' in response:
        return response
    else:
        return render_template('member.html')


@app.route('/deleteMember', methods=['POST'])
def delete_member():
    response = dao_member.delete_member(connection, request.form['member_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return render_template('member.html')


if __name__ == "__main__":
    print("Starting Python Flask Server For Store Order Management Application...")
    app.run(port=5000, debug=True)
