import mysql.connector
from Backend.db_connection import connect_mysql, select_query, generate_insert_statement, generate_update_statement
from datetime import datetime


def get_order(conn):
    query = """
        select BIN_TO_UUID(order_id) as order_id, order_created_date, BIN_TO_UUID(member_id) as member_id 
        from store.order
    """
    cursor = conn.cursor()
    response = select_query(cursor, query)
    return response


def insert_order(conn, data_dict):
    query, data, uuid = generate_insert_statement(
        'store.order',
        data_dict,
        ['order_id', 'member_id'],
        'order_id',
        ['member_id', 'order_created_date'],
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


def update_order(conn, data_dict, order_id):
    query, data, uuid = generate_update_statement(
        'store.order',
        data_dict,
        [],
        [],
        'order_id',
        order_id
    )

    # print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"{uuid} is updated"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


def delete_order(conn, order_id):
    query = f"DELETE FROM store.order where BIN_TO_UUID(order_id) = '{order_id}';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return f"{order_id} is deleted"


if __name__ == '__main__':
    connection = connect_mysql()
    print(get_order(connection))

    print(
        insert_order(
            connection,
            {
                "member_id": "bc0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2",
                "order_created_date": datetime.now(),
                "order_updated_date": datetime.now()
            }
        )
    )

    print(
        update_order(connection,
                     {
                         "order_updated_date": datetime.now()
                     },
                     'ec82671a-5cdd-535d-bf95-7d3ec98c1918'
                     )
    )

    # print(
    #     delete_order(
    #         connection,
    #         'ec82671a-5cdd-535d-bf95-7d3ec98c1918'
    #     )
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
