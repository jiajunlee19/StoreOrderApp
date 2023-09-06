import mysql.connector
from Backend.db_connection import connect_mysql, generate_insert_statement
from datetime import datetime


def get_order_item(conn):
    query = """
        select BIN_TO_UUID(order_item_id) as order_item_id, BIN_TO_UUID(order_id) as order_id, 
        BIN_TO_UUID(product_id) as product_id, order_item_quantity 
        from store.order_item
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    columns = cursor.description
    response = []

    if result is not None:
        row_dict = {}
        for i, column in enumerate(result):
            row_dict[columns[i][0]] = column
        response.append(row_dict)

    return response


def insert_order_item(conn, data_dict):

    query, data, uuid = generate_insert_statement(
        'store.order_item',
        data_dict,
        ['order_item_id', 'order_id', 'product_id'],
        'order_item_id',
        ['order_id', 'product_id'],
        []
    )

    # print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"{uuid} is inserted"

    except mysql.connector.IntegrityError as ie:
        return f"{str(ie)}"


def delete_order_item(conn, order_item_id):

    query = f"DELETE FROM store.order_item where BIN_TO_UUID(order_item_id) = '{order_item_id}';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return f"{order_item_id} is deleted"


if __name__ == '__main__':
    connection = connect_mysql()
    print(get_order_item(connection))

    print(
        insert_order_item(
            connection,
            {
                "order_id": "9a6029f1-ce7e-5a33-bd12-06860c3efbfd",
                "product_id": "c05f2fa9-a4bb-5e4d-abe0-bc76ef063a6f",
                "order_item_quantity": 10,
                "order_item_created_date": datetime.now(),
                "order_item_updated_date": datetime.now()
            }
        )
    )

    # print(
    #     delete_order_item(
    #         connection,
    #         'b76b5838-c32d-58fe-a8d2-9199043c639b'
    #     )
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
