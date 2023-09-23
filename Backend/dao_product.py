import mysql.connector
from Backend.db_connection import (myDatabase, connect_mysql,  select_query,
                                   generate_insert_statement, generate_update_statement)
from datetime import datetime


def get_product(conn):
    query = f"""
        select BIN_TO_UUID(p.product_id) as product_id, p.product_name, 
        BIN_TO_UUID(p.uom_id) as uom_id, u.uom_name, p.product_unit_price,p.product_bonus_points 
        from {myDatabase}.product p 
        inner join {myDatabase}.uom u on p.uom_id=u.uom_id;
    """
    cursor = conn.cursor()
    response = select_query(cursor, query)
    return response


def get_uom_by_product_name(conn, data):
    query = f"""
        select BIN_TO_UUID(p.product_id) as product_id, p.product_name, 
        BIN_TO_UUID(p.uom_id) as uom_id, u.uom_name, p.product_unit_price,p.product_bonus_points 
        from {myDatabase}.product p 
        inner join {myDatabase}.uom u on p.uom_id=u.uom_id
        where p.product_name = %s;
    """
    cursor = conn.cursor()
    response = select_query(cursor, query, data)
    return response


def insert_product(conn, data_dict):
    query, data, uuid = generate_insert_statement(
        f'{myDatabase}.product',
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
        return f"Integrity error: {str(ie)}"


def update_product(conn, data_dict, product_id):
    query, data, uuid = generate_update_statement(
        f'{myDatabase}.product',
        data_dict,
        [],
        [],
        'product_id',
        product_id
    )

    # print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"{uuid} is updated"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


def delete_product(conn, product_id):
    query = f"DELETE FROM {myDatabase}.product where BIN_TO_UUID(product_id) = '{product_id}';"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return f"{product_id} is deleted"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


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

    print(
        update_product(connection,
                       {
                           "product_unit_price": 0,
                           "product_bonus_points": 0.015,
                           "product_updated_date": datetime.now()
                       },
                       'c05f2fa9-a4bb-5e4d-abe0-bc76ef063a6f'
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
