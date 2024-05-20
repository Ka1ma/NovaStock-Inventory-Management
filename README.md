NovaStock Inventory Management System
=====================================

NovaStock is a simple inventory management system built using Python and MySQL. It provides a user-friendly interface to add, view, delete, and reset items in the inventory.

Screenshots
-----------

-   Homepage:
-   ![image](https://github.com/Ka1ma/NovaStock-Inventory-Management/assets/89065349/33b14925-bf14-4b8c-bbf6-92b11d6957c2)

-   Add Item:
-   ![image](https://github.com/Ka1ma/NovaStock-Inventory-Management/assets/89065349/ee99bb40-bfe0-47d8-9453-0481e8c94028)

-   View Items:
-   ![image](https://github.com/Ka1ma/NovaStock-Inventory-Management/assets/89065349/2f6ef39b-25d3-4512-bf71-868e92f1a805)

Features
--------

-   Add new items to the inventory with name, quantity, and price details.
-   View all items in the inventory along with their details.
-   Delete individual items from the inventory.
-   Reset the entire inventory.

Requirements
------------

-   Python 3.x
-   MySQL Server
-   XAMPP (for local MySQL server)

Installation
------------

1.  Clone the repository to your local machine:

    `git clone https://github.com/yourusername/novastock.git`

2.  Install the required Python packages:

    `pip install mysql-connector-python`

Setup
-----

1.  Install and start XAMPP to run the local MySQL server.

2.  Make sure you have MySQL server installed and running on your XAMPP.

3.  Create a new MySQL database for NovaStock:

    `CREATE DATABASE inventory;`

4.  Import the provided SQL file `inventory.sql` to create the necessary table:

    `mysql -u your_username -p inventory < inventory.sql`

5.  Open the `novastock.py` file and replace the following values with your XAMPP MySQL server details:

    `novastock = NovaStock(host="localhost", user="your_username", password="your_password", database="inventory")`

Usage
-----

1.  Run the `novastock.py` file:

    `python novastock.py`

2.  The NovaStock GUI will open. You can then add, view, delete, or reset items in the inventory using the provided buttons.

Authors
-------

-   Mychal Redoblado
-   Chloe Dela Cruz
-   James Bacas
-   CJ Alcantara

University
----------

Xavier University - Ateneo De Cagayan

Department
----------

College of Computer Studies

License
-------

Xavier University - Ateneo De Cagayan College of Computer Studies
