import mysql.connector
from Backend.db_connection import connect_mysql, generate_insert_statement
from datetime import datetime


def get_order(conn):
    query = """
        select BIN_TO_UUID(order_id) as order_id, order_created_date, BIN_TO_UUID(member_id) as member_id 
        from store.order
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
        return f"{str(ie)}"


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
                "order_id": "9a6029f1-ce7e-5a33-bd12-06860c3efbfd",
                "member_id": "bc0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2",
                "order_created_date": datetime.now(),
                "order_updated_date": datetime.now()
            }
        )
    )

    # print(
    #     delete_order(
    #         connection,
    #         '9a6029f1-ce7e-5a33-bd12-06860c3efbfd'
    #     )
    # )

    if connection is not None:
        connection.close()
        print("Connection closed")
