# Store Order App
In this project, we will build a 3-tier store order management application.
1. Database: mysql
2. Backend: Python and Flask
3. Front end: UI is written in HTML/CSS/Javascript/Bootstrap



![](homepage.JPG)

### Installation Instructions
Download mysql for windows: https://dev.mysql.com/downloads/installer/
`pip install mysql-connector-python`



# Let's start working on the first part -> Database: mysql

Step 1: Design database structure in https://erd.dbdesigner.net/

This step allows you to configure/design your database structure (setting primary keys/foreign key relation, etc.) before creating it in mysql database environment.

To reduce data redundancy, your database structure should at least meeting third normalization level - 3NF (Ref: https://www.guru99.com/database-normalization.html)
1NF: Each table cell should contain a single value, and each record needs to be unique
2NF: Each table should have a Single Column Primary Key and contains only columns related to the primary key
3NF: Each column of a table should be transitive functional independent to other columns in the table

<db_design image>

Step 2: Export design into mysql script and run it in mysql workbench. // or you can create the tables manually thru mySQL workbench.
<Ref script here>

Step 3: Insert some relevant records to the table
<table snapshots>


# Once database is ready, let's jump into backend design using Python

Step 1: Connect to your mySQL using python mysql-connector
db_connection.py

Step 2: For each base table, write queries (select,insert,delete) into backend database-object script
products_dao.py, orders_dao.py, uom_dao.py....

These dao are used to interact with front end UI later.

Step 3: Create views that is needed to show in UI
?



### Exercise 

The grocery management system that we built is functional but after we give it to users for use, we got following feedback. The exercise for you to address this feedback and implement these features in the application,
1. **Products Module**: In products page that lists current products, add an edit button next to delete button that allows to edit current product
2. **Products Module**: Implement a new form that allows you to add new UOM in the application. For example you want to add **Cubic Meter** as a new UOM as the grocery store decided to start selling **wood** as well. This requies changing backend (python server) and front end (UI) both.
3. **Orders Module**: When you place an order it doesn't have any validation. For example one can enter an order with empty customer name. You need to add validation for customer name and invalid item name or not specifying a quantity etc. This is only front end UI work.
4. **Orders Module**: In new order page there is a bug. When you manually change total price of an item it doesn't change the grand total. You need to fix this issue.
5. **Orders Module**: In the grid where orders are listed, add a view button in the last column. On clicking this button it should show you order details where individual items in that order are listed along with their price/quantity etc.

Reference link:
Scrum - https://scrumtrainingseries.com/