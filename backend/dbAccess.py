import sqlite3
from Config import DB_CONNECTION
from db_models import Product, Category, Status, Commission
import json
import datetime
from flask import jsonify

#products:
def add_product(json_product_without_id):
    try:
        json_object = json.loads(json_product_without_id)
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor2 = connection.cursor()
        cursor2.execute("INSERT INTO Product(name, description, unit_price, unit_weight, category_id) VALUES" +
                        "('{}',".format(json_object["name"]) +
                        "'{}', ".format(json_object["description"]) +
                        "{}, ".format(json_object["unit_price"]) +
                        "{}, ".format(json_object["unit_weight"]) +
                        "(SELECT id FROM Category WHERE name='{}') );".format(json_object["category_name"]))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error:
        return False
def get_product_list():
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Product;")
        dbResults = []
        for line in cursor.fetchall():
            dbResults.append(line)
        connection.close()
        return dbResults
    except sqlite3.Error:
        return None
def delete_product_by_id(id):
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Product WHERE id={};".format(id))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error:
        return False
def update_product(product_id, json_product_without_id):
    try:
        json_object = json.loads(json_product_without_id)
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("UPDATE Product SET "
                       "name = '{}',".format(json_object["name"]) +
                       "description = '{}',".format(json_object["description"]) +
                       "unit_price = {}, ".format(str(json_object["unit_price"])) +
                       "unit_weight = {}, ".format(str(json_object["unit_weight"])) +
                       "category_id = (SELECT id FROM Category WHERE name='{}') ".format(str(json_object["category_name"])) +
                       "WHERE id = {};".format(product_id)
                       )
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error as to:
        print(to)
        return False
def get_product(product_id):
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Product WHERE id = {};".format(product_id))
        result = cursor.fetchone()
        connection.close()
        return result
    except sqlite3.Error:
        return None

#categories:
def get_category_list():
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Category;")
        dbResults = []
        for line in cursor.fetchall():
            dbResults.append(line)
        connection.close()
        return dbResults
    except sqlite3.Error:
        return None
def get_category_id(category_name):
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM Category WHERE name='{}';".format(category_name))
        result = cursor.fetchone()
        connection.close()
        return result[0]
    except sqlite3.Error:
        return None

#clients:
def add_client(client_id):
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Client(id) VALUES ('{}');".format(str(client_id)))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error:
        return False

def get_client(id):
    try:
        print("CALL")
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CLIENT WHERE id = '{}'".format(id))
        result = cursor.fetchone()
        print(result)
        connection.close()
        return result
    except sqlite3.Error:
        return None

def get_client_list():
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Client;")
        dbResults = []
        for line in cursor.fetchall():
            dbResults.append(line)
        connection.close()
        return dbResults
    except sqlite3.Error:
        return None
def remove_client(client_id):
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Client WHERE id = '{}';".format(str(client_id)))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error:
        return False

def update_client(client_id, json_client_without_id):
    try:
        json_object = json.loads(json_client_without_id)
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("UPDATE Client SET "
                       "phone = '{}', ".format(json_object['phone']) +
                       "address_city = '{}', ".format(json_object['address_city']) +
                       "address_street = '{}', ".format(json_object['address_street']) +
                       "address_number = '{}' ".format(json_object['address_number']) +
                       "WHERE id = '{}';".format(str(client_id))
                       )
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error:
        return False
#orders

def create_order(json_commission):
    try:
        json_object = json.loads(json_commission)
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Commission(order_date, full_address, receiver, status_id, client_id) VALUES"
                       "('{}', ".format(str(datetime.date.today())) +
                       "'{}', ".format(json_object['full_address']) +
                       "'{}', ".format(json_object['receiver_name']) +
                       "{}, ".format(str(1)) +
                       "'{}');".format(json_object['client_id']))
        cursor.close()
        cursor2 = connection.cursor()
        cursor2.execute("SELECT id FROM Commission ORDER BY id DESC limit 1;")
        result = cursor2.fetchone()
        result = result[0]
        cursor2.close()
        cursor3 = connection.cursor()
        for item in json_object["items"]:
            cursor3.execute("INSERT INTO Commission_Product(commission_id, product_id, quantity) VALUES"
                            "({}, ".format(result) +
                            "{}, ".format(item['thing'][0]) +
                            "{});".format(item['quantity']))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error:
        return False
def get_order(id): #status_name zamiast status_id
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT Commission.order_date, Commission.full_address, Commission.receiver, Status.name, Commission.client_id, Commission.id "
                       "FROM Commission "
                       "INNER JOIN Status ON Commission.status_id = Status.id "
                       "WHERE client_id = '{}';".format(id))
        result = cursor.fetchall()
        connection.close()
        return result
    except sqlite3.Error:
        return None

def canChangeStatus(id, data):
    try:
        data = json.loads(data)
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT status_id FROM Commission WHERE id={};".format(id))
        currentStatusId = cursor.fetchone()[0]
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM Status WHERE name='{}';".format(data["status"]))
        newStatus = cursor.fetchone()[0]
        if currentStatusId > newStatus:
            return False
        elif currentStatusId == newStatus:
            return 'Same'
        else:
            return True
    except sqlite3.Error:
        return False
def change_status(id, data):
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        data = json.loads(data)
        cursor = connection.cursor()
        cursor.execute("UPDATE Commission SET status_id=(SELECT id FROM Status WHERE name='{}') WHERE id={};".format(data["status"], id))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error:
        return False
def get_commission_items(id): #product name zamiast id
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT Product.name, Commission_Product.quantity, Product.unit_price FROM Commission_Product "
                       "INNER JOIN Product ON Product.id = Commission_Product.product_id "
                       "WHERE commission_id = {};".format(id))
        results = cursor.fetchall()
        connection.close()
        return results
    except sqlite3.Error:
        return None
def get_commission_list():
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT Commission.id, Commission.client_id, Status.name "
                       "FROM Commission "
                       "INNER JOIN Status ON Status.id = Commission.status_id;")
        result = cursor.fetchall()
        return result
    except:
        return None
def delete_commission(id):
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor2 = connection.cursor()
        cursor.execute("DELETE FROM Commission WHERE id = {};".format(id))
        cursor2.execute("DELETE FROM Commission_Product WHERE commission_id = {};".format(id))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error:
        return False

#status
def get_status_list():
    try:
        connection = sqlite3.connect(DB_CONNECTION.DB_LOCATION)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Status")
        result = cursor.fetchall()
        connection.close()
        return result
    except sqlite3.Error:
        return None
