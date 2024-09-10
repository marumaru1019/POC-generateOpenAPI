from flask import Flask, request

app = Flask(__name__)

# Sample data
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.0},
    {'id': 2, 'name': 'Product 2', 'price': 20.0},
    {'id': 3, 'name': 'Product 3', 'price': 30.0}
]

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return {'products': products}

# Get a specific product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return {'message': 'Product not found'}, 404

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = {'id': data['id'], 'name': data['name'], 'price': data['price']}
    products.append(product)
    return {'message': 'Product created successfully'}, 201

# Update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    for product in products:
        if product['id'] == product_id:
            product['name'] = data['name']
            product['price'] = data['price']
            return {'message': 'Product updated successfully'}
    return {'message': 'Product not found'}, 404

# Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return {'message': 'Product deleted successfully'}
    return {'message': 'Product not found'}, 404

if __name__ == '__main__':
    app.run()