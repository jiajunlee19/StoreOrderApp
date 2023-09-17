# Store Order App

In this project, we will build a 3-tier store order management application.
1. Database: mysql
2. Backend: Python Flask
3. Front end: UI is written in HTML/CSS/Javascript



### Installation Instructions
Download mysql for windows: https://dev.mysql.com/downloads/installer/
`pip install mysql-connector-python`



# Database: mysql

I have generated a CREATE_TABLES.sql script, you can run it in mySQL Workbench and it will create everything required for this project automatically.

[CREATE_TABLE.sql](/Database/CREATE%20TABLES.sql)

To reduce data redundancy, your database structure should at least meeting third normalization level - 3NF
1. 1NF: Each table cell should contain a single value, and each record needs to be unique
2. 2NF: Each table should have a Single Column Primary Key and contains only columns related to the primary key
3. 3NF: Each column of a table should be transitive functional independent to other columns in the table

![SCHEMA_DIAGRAM.png](/Database/SCHEMA_DIAGRAM.png)



# Backend: Python Flask

Generate a Flask server, keep it running to connect backend to frontend
[server_flask.py](/Frontend/server_flask.py)

   

# Frontend 
There's two type of access level.
1. User can only manage their order/order_item
2. Admin have additional privileges to manage member/member_level/uom/product

### [Admin] Manage Member
![member.png](/Misc/member.PNG)

### [Admin] Manage Member Level
![member_level.png](/Misc/member_level.PNG)

### [Admin] Manage UOM
![uom.png](/Misc/uom.PNG)

### [Admin] Manage Product
![product.png](/Misc/product.PNG)

### Manage Order
![order.png](/Misc/order.PNG)

### Manage Order Item
![order_item.png](/Misc/order_item.PNG)