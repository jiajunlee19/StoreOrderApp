import os

# Rename "settings.template" to "settings.py"

# Initialize your settings below!
# myHost = "localhost"
# myDatabase = "store"
# myUsername = "dbadmin"
# myPassword = "dbadmin"

# or use environment variables
myHost = os.getenv('myHOST')
myDatabase = os.getenv('myDatabase')
myUsername = os.getenv('myUsername')
myPassword = os.getenv('myPassword')
