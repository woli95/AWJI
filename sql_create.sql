CREATE TABLE Product(
	id INTEGER PRIMARY KEY,
  	name TEXT NOT NULL,
  	description TEXT,
  	unit_price REAL NOT NULL,
  	unit_weight REAL NOT NULL,
  	category_id INT NOT NULL,
  	FOREIGN KEY (category_id) REFERENCES Category(id)
  	);

CREATE TABLE Category(
    id INTEGER PRIMARY KEY,
    name TEXT
    );

CREATE TABLE Client(
    id TEXT PRIMARY KEY,
    phone TEXT,
    address_city TEXT,
    address_street TEXT,
    address_number TEXT
);

CREATE TABLE Status(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE Commission(
    id INTEGER PRIMARY KEY,
    order_date TEXT NOT NULL,
    full_address TEXT NOT NULL,
    receiver TEXT NOT NULL,
    status_id INTEGER NOT NULL,
    client_id TEXT NOT NULL,
    FOREIGN KEY (status_id) REFERENCES Status(id),
    FOREIGN KEY (client_id) REFERENCES Client(id)
);

CREATE TABLE Commission_Product(
    commission_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (commission_id) REFERENCES Commission(id),
    FOREIGN KEY (product_id) REFERENCES Product(id),
    PRIMARY KEY(commission_id, product_id)
);
