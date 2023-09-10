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


@app.route('/orderItem/<order_id>', methods=['GET'])
def order_item(order_id):
    return render_template('order_item.html', order_id=order_id)


@app.route('/getMember', methods=['GET'])
def get_member():
    connection = connect_mysql()
    response = dao_member.get_member(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return response


@app.route('/getMemberLevel', methods=['GET'])
def get_member_level():
    connection = connect_mysql()
    response = dao_member_level.get_member_level(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return response


@app.route('/getUOM', methods=['GET'])
def get_uom():
    connection = connect_mysql()
    response = dao_uom.get_uom(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return response


@app.route('/getProduct', methods=['GET'])
def get_product():
    connection = connect_mysql()
    response = dao_product.get_product(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return response


@app.route('/getOrder', methods=['GET'])
def get_order():
    connection = connect_mysql()
    response = dao_order.get_order(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return response


@app.route('/getOrderItem/<order_id>', methods=['GET'])
def get_order_item(order_id):
    connection = connect_mysql()
    data = tuple([order_id])
    response = dao_order_item.get_order_item(connection, data)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return response


@app.route('/insertMember', methods=['POST'])
def insert_member():
    connection = connect_mysql()
    data_dict = {
        "member_name": request.form['member_name'],
        "member_password": request.form['member_password'],
        "member_bonus_points": request.form['member_bonus_points'],
        "member_created_date": datetime.now(),
        "member_updated_date": datetime.now()
    }
    response = dao_member.insert_member(connection, data_dict)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('member.html')


@app.route('/insertMemberLevel', methods=['POST'])
def insert_member_level():
    connection = connect_mysql()
    data_dict = {
        "member_level": request.form['member_level'],
        "bonus_points_min": request.form['bonus_points_min'],
        "bonus_points_max": request.form['bonus_points_max'],
        "member_level_created_date": datetime.now(),
        "member_level_updated_date": datetime.now()
    }
    response = dao_member_level.insert_member_level(connection, data_dict)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('member_level.html')


@app.route('/insertUOM', methods=['POST'])
def insert_uom():
    connection = connect_mysql()
    data_dict = {
        "uom_name": request.form['uom_name'],
        "uom_created_date": datetime.now(),
        "uom_updated_date": datetime.now()
    }
    response = dao_uom.insert_uom(connection, data_dict)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('uom.html')


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    connection = connect_mysql()
    data_dict = {
        "product_name": request.form['product_name'],
        "uom_id": request.form['uom_id'],
        "product_unit_price": request.form['product_unit_price'],
        "product_bonus_points": request.form['product_bonus_points'],
        "product_created_date": datetime.now(),
        "product_updated_date": datetime.now()
    }
    response = dao_product.insert_product(connection, data_dict)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('product.html')


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    connection = connect_mysql()
    data_dict = {
        "member_id": request.form['member_id'],
        "order_created_date": datetime.now(),
        "order_updated_date": datetime.now()
    }
    response = dao_order.insert_order(connection, data_dict)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('index.html')


@app.route('/insertOrderItem', methods=['POST'])
def insert_order_item():
    connection = connect_mysql()
    data_dict = {
        "order_id": request.form['order_id'],
        "product_id": request.form['product_id'],
        "uom_id": request.form['uom_id'],
        "order_item_quantity": request.form['order_item_quantity'],
        "order_item_created_date": datetime.now(),
        "order_item_updated_date": datetime.now()
    }
    response = dao_order_item.insert_order_item(connection, data_dict)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('order_item.html')


@app.route('/updateMember', methods=['POST'])
def update_member():
    connection = connect_mysql()
    data_dict = {
        "member_password": request.form['member_password'],
        "member_bonus_points": request.form['member_bonus_points'],
        "member_updated_date": datetime.now()
    }
    member_id = request.form['member_id']
    response = dao_member.update_member(connection, data_dict, member_id)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('member.html')


@app.route('/updateMemberLevel', methods=['POST'])
def update_member_level():
    connection = connect_mysql()
    data_dict = {
        "bonus_points_min": request.form['bonus_points_min'],
        "bonus_points_min_max": request.form['bonus_points_min'],
        "member_level_updated_date": datetime.now()
    }
    member_level_id = request.form['member_level_id']
    response = dao_member_level.update_member_level(connection, data_dict, member_level_id)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('member_level.html')


@app.route('/updateUOM', methods=['POST'])
def update_uom():
    connection = connect_mysql()
    data_dict = {
        "uom_updated_date": datetime.now()
    }
    uom_id = request.form['uom_id']
    response = dao_uom.update_uom(connection, data_dict, uom_id)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('uom.html')


@app.route('/updateProduct', methods=['POST'])
def update_product():
    connection = connect_mysql()
    data_dict = {
        "product_unit_price": request.form['product_unit_price'],
        "product_bonus_points": request.form['product_bonus_points'],
        "product_updated_date": datetime.now()
    }
    product_id = request.form['product_id']
    response = dao_product.update_product(connection, data_dict, product_id)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('product.html')


@app.route('/updateOrder', methods=['POST'])
def update_order():
    connection = connect_mysql()
    data_dict = {
        "order_updated_date": datetime.now()
    }
    order_id = request.form['order_id']
    response = dao_order.update_order(connection, data_dict, order_id)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('index.html')


@app.route('/updateOrderItem', methods=['POST'])
def update_order_item():
    connection = connect_mysql()
    data_dict = {
        "order_item_quantity": request.form['order_item_quantity'],
        "order_item_updated_date": datetime.now()
    }
    order_item_id = request.form['order_item_id']
    response = dao_order_item.update_order_item(connection, data_dict, order_item_id)
    if connection is not None:
        connection.close()
        print("Connection closed")
    if 'error' in response:
        return response
    else:
        return render_template('order_item.html')


@app.route('/deleteMember', methods=['POST'])
def delete_member():
    connection = connect_mysql()
    response = dao_member.delete_member(connection, request.form['member_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return render_template('member.html')


@app.route('/deleteMemberLevel', methods=['POST'])
def delete_member_level():
    connection = connect_mysql()
    response = dao_member_level.delete_member_level(connection, request.form['member_level_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return render_template('member_level.html')


@app.route('/deleteUOM', methods=['POST'])
def delete_uom():
    connection = connect_mysql()
    response = dao_uom.delete_uom(connection, request.form['uom_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return render_template('uom.html')


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    connection = connect_mysql()
    response = dao_product.delete_product(connection, request.form['product_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return render_template('product.html')


@app.route('/deleteOrder', methods=['POST'])
def delete_order():
    connection = connect_mysql()
    response = dao_order.delete_order(connection, request.form['order_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return render_template('index.html')


@app.route('/deleteOrderItem', methods=['POST'])
def delete_order_item():
    connection = connect_mysql()
    response = dao_order_item.delete_order_item(connection, request.form['order_item_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if connection is not None:
        connection.close()
        print("Connection closed")
    return render_template('order_item.html')


if __name__ == "__main__":
    print("Starting Python Flask Server For Store Order Management Application...")
    app.run(port=5000, debug=True)
