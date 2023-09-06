import mysql.connector
from Backend.db_connection import connect_mysql, generate_insert_statement
from datetime import datetime


def get_product(conn):

    query = ("""
        select BIN_TO_UUID(p.product_id) as product_id, p.product_name, 
        BIN_TO_UUID(p.uom_id) as uom_id, u.uom_name, p.product_unit_price,p.product_bonus_points 
        from store.product p 
        inner join store.uom u on p.uom_id=u.uom_id;
    """)

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


def insert_product(conn, data_dict):

    query, data, uuid = generate_insert_statement(
        'store.product',
        data_dict,
        ['product_id', 'uom_id'],
        'product_id',
        ['product_name', 'uom_id'],
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
            {
                "product_name": "pen",
                "uom_id": "8a150e8f-5cdf-5b26-b95f-87dda8889af6",
                "product_unit_price": 0,
                "product_bonus_points": 0.015,
                "product_created_date": datetime.now(),
                "product_updated_date": datetime.now()
            }
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
