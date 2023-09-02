import mysql.connector
from db_connection import connect_mysql, generate_insert_statement


def get_uom(conn):
    query = "select BIN_TO_UUID(uom_id) as uom_id, uom_name from store.uom"
    cursor = conn.cursor()
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


def insert_uom(conn, data_list):

    query, data, uuid = generate_insert_statement(
        'store.uom',
        ['uom_id', 'uom_name'],
        [0],
        data_list,
        [0]
    )

    print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"[{uuid}] data_list = {data_list} is inserted"

    except mysql.connector.IntegrityError as ie:
        return f"{str(ie)}"


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
            ['each']
        )
    )

    print(
        delete_uom(
            connection,
            '8a150e8f-5cdf-5b26-b95f-87dda8889af6'
        )
    )

    if connection is not None:
        connection.close()
        print("Connection closed")
