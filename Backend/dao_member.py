import mysql.connector
from db_connection import connect_mysql, generate_insert_statement


def get_member(conn):
    query = "select BIN_TO_UUID(member_id) as member_id, member_name, member_bonus_points from store.member"
    cursor = conn.cursor()
    cursor.execute(query)
    response = []
    for (member_id, member_name, member_bonus_points) in cursor:
        response.append({
            'member_id': member_id,
            'member_name': member_name,
            'member_bonus_points': member_bonus_points
        })
    return response


def insert_member(conn, data_list):

    query, data, uuid = generate_insert_statement(
        'store.member',
        ['member_id', 'member_name', 'member_bonus_points'],
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


def delete_member(conn, member_id):

    query = f"DELETE FROM store.member where BIN_TO_UUID(member_id) = '{member_id}';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return f"{member_id} is deleted"


if __name__ == '__main__':
    connection = connect_mysql()
    print(get_member(connection))

    print(
        insert_member(
            connection,
            ['jiajunlee',0]
        )
    )

    print(
        delete_member(connection, 'bc0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2')
    )

    if connection is not None:
        connection.close()
        print("Connection closed")
