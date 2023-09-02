from settings import myUsername
from settings import myPassword


def get_settings():
    """
    Get Username and Password
    """
    return myUsername, myPassword

def main():
    print(myUsername, myPassword)

if __name__ == '__main__':
    main()
