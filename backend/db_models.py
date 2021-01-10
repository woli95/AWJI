class Product:
    def __init__(self, name=None, description=None, unit_price=None, unit_weight=None, category_name=None, from_json=False, db_object=None, **kwargs):
        if from_json is True:
            self.name = name
            self.description = description
            self.unit_price = unit_price
            self.unit_weight = unit_weight
            self.category_name = category_name
        else:
            self.id = db_object[0]
            self.name = db_object[1]
            self.description = db_object[2]
            self.unit_price = db_object[3]
            self.unit_weight = db_object[4]
            self.category_name = db_object[5]
class Category:
    def __init__(self, db_object=None):
        self.id = db_object[0]
        self.name = db_object[1]

class Status:
    def __init__(self, db_object=None):
        self.id = db_object[0]
        self.name = db_object[1]

class Commission:
    def __init__(self, db_object=None):
        self.id = db_object[0]
        self.date = db_object[1]
        self.status_id = db_object[2]
        self.client_id = db_object[3]

class Commission_Product:
    def __init__(self, db_object=None):
        self.commission_id = db_object[0]
        self.product_id = db_object[1]
        self.quantity = db_object[2]