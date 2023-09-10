import mysql.connector
from Backend.db_connection import connect_mysql, select_query, generate_insert_statement, generate_update_statement
from datetime import datetime


def get_uom(conn):
    query = "select BIN_TO_UUID(uom_id) as uom_id, uom_name from store.uom"
    cursor = conn.cursor()
    response = select_query(cursor, query)
    return response


def insert_uom(conn, data_dict):
    query, data, uuid = generate_insert_statement(
        'store.uom',
        data_dict,
        ['uom_id'],
        'uom_id',
        ['uom_name'],
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


def update_uom(conn, data_dict, uom_id):
    query, data, uuid = generate_update_statement(
        'store.uom',
        data_dict,
        [],
        [],
        'uom_id',
        uom_id
    )

    # print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"{uuid} is updated"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


def delete_uom(conn, uom_id):
    query = f"DELETE FROM store.uom where BIN_TO_UUID(uom_id) = '{uom_id}';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return f"{uom_id} is deleted"


if __name__ == '__main__':
    connection = connect_mysql()
    print(get_uom(connection))

    print(
        insert_uom(
            connection,
            {
                "uom_name": "each",
                "uom_created_date": datetime.now(),
                "uom_updated_date": datetime.now()
            }
        )
    )

    print(
        update_uom(connection,
                   {
                       "uom_updated_date": datetime.now()
                   },
                   '8a150e8f-5cdf-5b26-b95f-87dda8889af6'
                   )
    )

    # print(
    #     delete_uom(
    #         connection,
    #         '8a150e8f-5cdf-5b26-b95f-87dda8889af6'
    #     )
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
