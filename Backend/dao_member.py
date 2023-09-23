import mysql.connector
from Backend.db_connection import (myDatabase, connect_mysql,  select_query,
                                   generate_insert_statement, generate_update_statement)
from datetime import datetime


def get_member(conn):
    query = f"""
        select BIN_TO_UUID(member_id) as member_id, member_name, BIN_TO_UUID(member_password) as member_password, 
        member_bonus_points, member_created_date, member_updated_date
        from {myDatabase}.member
    """
    cursor = conn.cursor()
    response = select_query(cursor, query)
    return response


def insert_member(conn, data_dict):

    query, data, uuid = generate_insert_statement(
        f'{myDatabase}.member',
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
        return f"Integrity error: {str(ie)}"


def update_member(conn, data_dict, member_id):

    query, data, uuid = generate_update_statement(
        f'{myDatabase}.member',
        data_dict,
        ['member_password'],
        ['member_password'],
        'member_id',
        member_id
    )

    # print(f"query = {query}, data = {data}, uuid = {uuid}")

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return f"{uuid} is updated"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


def delete_member(conn, member_id):

    query = f"DELETE FROM {myDatabase}.member where BIN_TO_UUID(member_id) = '{member_id}';"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return f"{member_id} is deleted"

    except mysql.connector.IntegrityError as ie:
        return f"Integrity error: {str(ie)}"


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

    print(
        update_member(connection,
                      {
                          "member_password": "abc123",
                          "member_bonus_points": 0,
                          "member_updated_date": datetime.now()
                      },
                      'bc0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2'
                      )
    )

    # print(
    #     delete_member(connection, 'bc0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2')
    # )

    # print(
    #     delete_member(connection, 'a3a7a769-4903-5950-8a58-d526b910cbb3')
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
