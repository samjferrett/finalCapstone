# Stock Tracker
Capstone Project 4 for hyperion dev software engineering course

This project is a simple stock tracker for shoes written in python intended to implement python classes.
The program tracks stock in a list. Inventory can be added to the list manually or from a text file.

## inventory.txt
inventory.txt can be read in using option 1 of the menu (see inventory.py for description)
inventory.txt has entries where each line represents one item with columns being 
country, product code, product name, cost, quantity. Each column is seperated using commas.

## inventory.py
inventory.py can be ran using 
```
python3 inventory.py
```

The user is presented with a menu with the following options:
1. Add all shoes from file data
2. Enter new shoe manually
3. View all shoes in inventory
4. Restock lowest inventory shoe
5. Search shoes by code
6. Show total value per shoe
7. Put highest quantity shoe on sale
8. Quit

## requirements
inventory.py requires python3 and tabulate
