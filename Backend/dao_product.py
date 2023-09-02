import mysql.connector
from db_connection import connect_mysql, generate_insert_statement


def get_product(conn):

    query = ("""
        select BIN_TO_UUID(p.product_id) as product_id, p.product_name, 
        BIN_TO_UUID(p.uom_id) as uom_id, u.uom_name, p.product_unit_price,p.product_bonus_points 
        from store.product p 
        inner join store.uom u on p.uom_id=u.uom_id;
    """)

    cursor = conn.cursor()
    cursor.execute(query)
    response = []
    for (product_id, product_name, uom_id, uom_name, product_unit_price, product_bonus_points) in cursor:
        response.append(
            {'product_id': product_id, 'product_name': product_name, 'uom_id': uom_id, 'uom_name': uom_name,
             'product_unit_price': product_unit_price, 'product_bonus_points': product_bonus_points})
    return response


def insert_product(conn, data_list):

    query, data, uuid = generate_insert_statement(
        'store.product',
        ['product_id', 'product_name', 'uom_id', 'product_unit_price', 'product_bonus_points'],
        [0, 2],
        data_list,
        [0, 1]
    )

    print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"[{uuid}] data_list = {data_list} is inserted"

    except mysql.connector.IntegrityError as ie:
        return f"{str(ie)}"


def delete_product(conn, product_id):

    query = f"DELETE FROM store.product where BIN_TO_UUID(product_id) = '{product_id}';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return f"{product_id} is deleted"


if __name__ == '__main__':
    connection = connect_mysql()

    products = get_product(connection)
    print(products)

    print(
        insert_product(
            connection,
            ['pen', '8a150e8f-5cdf-5b26-b95f-87dda8889af6'.replace("-", ""), 1.5, 0.015]
        )
    )

    # print(
    #     delete_product(
    #         connection,
    #         'c05f2fa9-a4bb-5e4d-abe0-bc76ef063a6f'
    #     )
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
