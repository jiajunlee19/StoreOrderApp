from settings import myHost, myDatabase, myUsername, myPassword
import mysql.connector
from uuid_generation import generate_uuid

__conn = None


def connect_mysql():
    """
    If connection exists, use existing mysql connection. Else, connect to new mysql connection.
    """

    # Declare conn as global variable
    global __conn

    if __conn is not None:
        return __conn

    else:
        try:
            print("Connecting to mysql...")
            __conn = mysql.connector.connect(host=myHost, database=myDatabase, user=myUsername, password=myPassword)
            print(f"Connected to host={myHost}, database={myDatabase}")
            return __conn

        except Exception as e:
            print(f"Failed to connect: {str(e)}")
            return None


def generate_insert_statement(table, column_list_all, uuid_col_index_list, data_list, primary_data_index_list):
    """
    Assuming table UUID primary key column is always in the first column!!!
    Declare all UUID type columns in uuid_col_index_list (use to replace %s into UUID_TO_BIN(%s) on query statement)
    Declare all primary columns in primary_col_index_list (use to generate uuid on data tuple)
    """

    # Generating query statement
    column_tuple = ", ".join(column_list_all)
    value_tuple_list = ['%s'] * len(column_list_all)

    # for each uuid_col_index, replace %s into UUID_TO_BIN(%s)
    if len(uuid_col_index_list) > 0:
        for uuid_col_index in uuid_col_index_list:
            value_tuple_list[uuid_col_index] = "UUID_TO_BIN(%s)"

    value_tuple = ", ".join(value_tuple_list)

    query = f"""
        INSERT INTO {table} ({column_tuple})
        VALUES ({value_tuple});
    """

    # Generating data tuple
    data_tuple = tuple(data_list)
    if len(uuid_col_index_list) > 0:
        uuid_data_list = [data_list[primary_col_index] for primary_col_index in primary_data_index_list]
        # print(uuid_data_list)
        uuid = generate_uuid(uuid_data_list)
        uuid_tuple = tuple(uuid.replace('-', '').split(" "))
        data = uuid_tuple + data_tuple
    else:
        uuid = None
        data = data_tuple

    return query, data, uuid


if __name__ == "__main__":
    connection = connect_mysql()

    Query, Data, UUID = generate_insert_statement(
        'store.product',
        ['uuid', 'name', 'gender', 'value'],
        [0],
        ['me', 'male', 100],
        [0, 1]
    )
    print(Query, Data, UUID)

    if connection is not None:
        connection.close()
        print("Connection closed")
