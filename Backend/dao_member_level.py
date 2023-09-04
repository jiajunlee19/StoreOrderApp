import mysql.connector
from Backend.db_connection import connect_mysql, generate_insert_statement


def get_member_level(conn):
    query = """
        select BIN_TO_UUID(member_level_id) as member_level_id, member_level, bonus_points_min, bonus_points_max 
        from store.member_level
    """
    cursor = conn.cursor()
    cursor.execute(query)
    response = []
    for (member_level_id, member_level, bonus_points_min, bonus_points_max) in cursor:
        response.append({
            'member_level_id': member_level_id,
            'member_level': member_level,
            'bonus_points_min': bonus_points_min,
            'bonus_points_max': bonus_points_max
        })
    return response


def insert_member_level(conn, data_list):

    query, data, uuid = generate_insert_statement(
        'store.member_level',
        ['member_level_id', 'member_level', 'bonus_points_min', 'bonus_points_max'],
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


def delete_member_level(conn, member_level_id):

    query = f"DELETE FROM store.member_level where BIN_TO_UUID(member_level_id) = '{member_level_id}';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return f"{member_level_id} is deleted"


if __name__ == '__main__':
    connection = connect_mysql()
    print(get_member_level(connection))

    print(
        insert_member_level(
            connection,
            ['normal', 0, 10]
        )
    )

    # print(
    #     delete_member_level(connection, '18a74e86-b9a4-512e-9bbe-c47f2ec69213')
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
