from settings import myHost, myDatabase, myUsername, myPassword
import mysql.connector
from Backend.uuid_generation import generate_uuid

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


def generate_insert_statement(table: str, data_dict: dict, uuid_col_list: list, generate_uuid_col_name: str,
                              primary_col_list: list):
    """
    Usage:
    1) Define table to be inserted
    2) data_dict keys should match the table column name, and primary_UUID column should be excluded here
    3) All uuid-type column MUST be defined in uuid_col_list for UUID_TO_BIN conversion!
    4) If a primary UUID needs to be generated, define primary_col_list used to generate the primary UUID
        it will be named as generate_uuid_col_name!

    5)Return insert statement like :
    INSERT INTO schema.table (person_uuid, name, gender_uuid, height)
    VALUES (UUID_TO_BIN(%s), %s, UUID_TO_BIN(%s), %s);
    ('554260d7887657ac9233f300c1c2cda3', 'jiajunlee', 'ab0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2', 170)
    """

    # Split data_dict by key list and value list
    column_list = list(data_dict.keys())  # ['name', 'gender_uuid', 'height']
    value_list = list(data_dict.values())  # ['jiajunlee', 'bc0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2', 170]

    # column_tuple =  "person_uuid, name, gender_uuid, height"
    if len(uuid_col_list) > 0 and len(generate_uuid_col_name) > 0:
        column_list.insert(0, generate_uuid_col_name)  # ['person_uuid', 'name', 'gender_uuid', 'height']
    column_tuple = ", ".join(column_list)

    # value_tuple = "UUID_TO_BIN(%s), %s, UUID_TO_BIN(%s), %s"
    value_tuple_list = ['%s'] * len(column_list)
    if len(uuid_col_list) > 0:
        for uuid_col in uuid_col_list:
            uuid_col_index = column_list.index(uuid_col)
            value_tuple_list[uuid_col_index] = "UUID_TO_BIN(%s)"
    value_tuple = ", ".join(value_tuple_list)

    # data_tuple = ('jiajunlee','ab0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2',170)
    if len(uuid_col_list) > 0 and len(generate_uuid_col_name) > 0:
        # primary_value_list = ['jiajunlee', 'bc0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2']
        primary_value_list = [data_dict[primary_col] for primary_col in primary_col_list]
        uuid = generate_uuid(primary_value_list)
        data_tuple = tuple(uuid.replace('-', '').split(" ")) + tuple(value_list)
    else:
        uuid = None
        data_tuple = tuple(value_list)

    # Generating query statement
    query = f"""
        INSERT INTO {table} ({column_tuple})
        VALUES ({value_tuple});
    """

    return query, data_tuple, uuid


if __name__ == "__main__":
    connection = connect_mysql()

    Query, Data, UUID = generate_insert_statement(
        'schema.table',
        {
            "name": "jiajunlee",
            "gender_uuid": "ab0c0bbc-fcbe-5d85-8a5c-5f603aecbeb2",
            "height": 170
        },
        ['person_uuid', 'gender_uuid'],
        'person_uuid',
        ['name', 'gender_uuid']
    )
    print(Query, Data, UUID)

    if connection is not None:
        connection.close()
        print("Connection closed")
