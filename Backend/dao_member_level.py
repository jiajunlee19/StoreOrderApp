import mysql.connector
from Backend.db_connection import connect_mysql, select_query, generate_insert_statement, generate_update_statement
from datetime import datetime


def get_member_level(conn):
    query = """
        select BIN_TO_UUID(member_level_id) as member_level_id, member_level, bonus_points_min, bonus_points_max,
        member_level_created_date, member_level_updated_date
        from store.member_level
        order by bonus_points_min, bonus_points_max
    """
    cursor = conn.cursor()
    response = select_query(cursor, query)
    return response


def insert_member_level(conn, data_dict):
    query, data, uuid = generate_insert_statement(
        'store.member_level',
        data_dict,
        ['member_level_id'],
        'member_level_id',
        ['member_level'],
        []
    )

    print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"{uuid} is inserted"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


def update_member_level(conn, data_dict, member_level_id):
    query, data, uuid = generate_update_statement(
        'store.member_level',
        data_dict,
        [],
        [],
        'member_level_id',
        member_level_id
    )

    # print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"{uuid} is updated"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


def delete_member_level(conn, member_level_id):
    query = f"DELETE FROM store.member_level where BIN_TO_UUID(member_level_id) = '{member_level_id}';"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return f"{member_level_id} is deleted"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


if __name__ == '__main__':
    connection = connect_mysql()
    print(get_member_level(connection))

    print(
        insert_member_level(
            connection,
            {
                "member_level": "normal",
                "bonus_points_min": 0,
                "bonus_points_max": 10,
                "member_level_created_date": datetime.now(),
                "member_level_updated_date": datetime.now()
            }
        )
    )

    print(
        update_member_level(connection,
                            {
                                "bonus_points_min": 0,
                                "bonus_points_max": 10,
                                "member_level_updated_date": datetime.now()
                            },
                            '18a74e86-b9a4-512e-9bbe-c47f2ec69213'
                            )
    )

    # print(
    #     delete_member_level(connection, '18a74e86-b9a4-512e-9bbe-c47f2ec69213')
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
