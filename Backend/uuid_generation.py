import uuid


def generate_uuid(string_list):
    """Generate UUID based on string_list, used for database primary key"""
    sep = " #|# "
    string_list = map(str, string_list)
    string = sep.join(string_list)
    namespace = uuid.uuid5(uuid.NAMESPACE_DNS, 'jiajunlee.com')
    uuid5 = uuid.uuid5(namespace, string)
    return str(uuid5)


if __name__ == "__main__":
    for i in range(0, 2):
        myUUID = generate_uuid(["abc", 123])
        print(f"UUID_{i} is {myUUID}")
