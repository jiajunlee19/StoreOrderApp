import mysql.connector
from Backend.db_connection import connect_mysql, generate_insert_statement
from datetime import datetime


def get_member(conn):
    query = """
        select BIN_TO_UUID(member_id) as member_id, BIN_TO_UUID(member_password) as member_password, 
        member_bonus_points, member_created_date, member_updated_date
        from store.member
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


def insert_member(conn, data_dict):

    query, data, uuid = generate_insert_statement(
        'store.member',
        data_dict,
        ['member_id', 'member_password'],
        'member_id',
        ['member_name'],
        ['member_password']
    )

    # print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"{uuid} is inserted"

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
            {
                "member_name": "jiajunlee",
                "member_password": "abc123",
                "member_bonus_points": 0,
                "member_created_date": datetime.now(),
                "member_updated_date": datetime.now()
            }
        )
    )

    # print(
    #     delete_member(connection, 'bc0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2')
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
