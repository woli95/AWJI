from main import app
from firebase_admin import auth, exceptions
from flask import jsonify, request
import dbAccess


@app.route('/products', methods=['POST', 'GET'])
def add_new_product():
    if request.method == 'POST':
        result = dbAccess.add_product(request.data)
        if result is True:
            return jsonify('OK'), 200
        else:
            return jsonify('FAILURE')
    elif request.method == 'GET':
        result = dbAccess.get_product_list()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400

@app.route('/products/<id>', methods=['POST', 'PUT', 'GET'])
def get_or_update_or_delete_product(id=None):
    if request.method == 'POST':
        if dbAccess.delete_product_by_id(id) is True:
            return jsonify('OK'), 200
        else:
            return jsonify("FAILURE")
    elif request.method == 'PUT':
        if dbAccess.update_product(id, request.data) is True:
            return jsonify('OK'), 200
        else:
            return jsonify('FAILURE')
    elif request.method == 'GET':
        result = dbAccess.get_product(id)
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400


@app.route('/categories', methods=['GET'])
def get_category_list():
    if request.method == 'GET':
        result = dbAccess.get_category_list()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400

@app.route('/categories/<category_name>', methods=['GET'])
def get_category_id(category_name=None):
    if request.method == 'GET':
        result = dbAccess.get_category_id(category_name)
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400

@app.route('/clients', methods=['GET'])
def get_client_list():
    if request.method == 'GET':
        result = dbAccess.get_client_list()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400

@app.route('/clients/<id>', methods=['POST', 'PUT', 'GET'])
def update_or_create_client(id=None):
    if request.method == 'POST':
        decoded = request.data.decode('utf-8')
        if "create" in decoded:
            if dbAccess.add_client(id) is True:
                return jsonify('OK'), 200
            else:
                return jsonify('FAILURE')
        elif "delete" in decoded:
            if dbAccess.remove_client(id) is True:
                auth.delete_user(uid=id)
                try:
                    auth.get_user(uid=id)
                    return jsonify('FAILURE')
                except exceptions.FirebaseError:
                    return jsonify('OK'), 200
            else:
                return jsonify('FAILURE')
    elif request.method == 'PUT':
        if dbAccess.update_client(id, request.data) is True:
            return jsonify('OK'), 200
        else:
            return jsonify('FAILURE')
    elif request.method == 'GET':
        result = dbAccess.get_client(id)
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400

@app.route('/orders', methods=['GET', 'POST'])
def create_commission_or_get_commission_list():
    if request.method == 'POST':
        result = dbAccess.create_order(request.data)
        if result is True:
            return jsonify('OK'), 200
        else:
            return jsonify('FAILURE')
    elif request.method == 'GET':
        result = dbAccess.get_commission_list()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400

@app.route('/orders/<id>', methods=['GET', 'POST', 'PUT'])
def get_products_for_order_or_update_status_or_delete_order(id=None):
    if request.method == 'GET':
        result = dbAccess.get_commission_items(id)
        if result is not None:
            print(result)
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    elif request.method == 'POST':
        if dbAccess.delete_commission(id) is True:
            return jsonify('OK'), 200
        else:
            return jsonify('FAILURE')
    elif request.method == 'PUT':
        if dbAccess.canChangeStatus(id, request.data) is True:
            if dbAccess.change_status(id, request.data) is True:
                return jsonify('OK'), 200
            else:
                return jsonify('FAILURE'), 200
        elif dbAccess.canChangeStatus(id, request.data) == 'Same':
            return jsonify('Values are the same'), 200
        else:
            return jsonify('Backward try'), 200
    else:
        return jsonify('Bad request method'), 400

@app.route('/clients/<id>/orders', methods=['GET'])
def get_client_orders(id=None):
    if request.method == 'GET':
        result = dbAccess.get_order(id)
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400

@app.route('/status', methods=['GET'])
def get_status_list():
    if request.method == 'GET':
        result = dbAccess.get_status_list()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify('FAILURE')
    else:
        return jsonify('Bad request method'), 400
