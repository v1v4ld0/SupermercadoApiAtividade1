from flask import Flask, request

api = Flask(__name__)

products = []
users = []
departments = []
categories = []


def getNextID(lista):
    if lista:
        return max(item['id'] for item in lista) + 1
    return 1


@api.route("/")
def index():
    return ({'version': '1.0.0'}, 200)


@api.route("/products/<int:id>", methods=['GET'])
def getProductByID(id: int):
    
    for product in products:
        if product['id'] == id:
            return (product, 200)
    return ({'error': 'Produto não encontrado'}, 404)


@api.route('/products', methods=['GET', 'POST'])
def productHandle():
    if request.method == 'POST':

        json = request.get_json()

        jsonProduct = {
            'id': getNextID(products),
            'nome': json["nome"],
            }
        products.append(jsonProduct)

        return (jsonProduct, 201)
    
    elif request.method == 'GET':

        return (products, 200)
    

@api.route("/users/<int:id>", methods=['GET'])
def getUserByID(id: int):

    for user in users:
        if user['id'] == id:
            return (user, 200)
    return ({'error': 'Usuário não encontrado'}, 404)


@api.route('/users', methods=['GET', 'POST'])
def userHandle():
    if request.method == 'POST':

        json = request.get_json()

        jsonUser = {
            'id': getNextID(users),
            'nome': json["nome"], 
            }
        users.append(jsonUser)

        return (jsonUser, 201)
    
    elif request.method == 'GET':
        return (users, 200)


@api.route('/categories/<int:id>', methods=['GET'])
def getCategoryByID(id: int):
    
    for category in categories:
        if category['id'] == id:
            return (category, 200)
    return ({'error': 'Categoria não encontrada'}, 404)


@api.route('/categories', methods=['GET', 'POST'])
def categoryHandle():
    if request.method == 'POST':
        
        json = request.get_json()

        jsonCategory = {
            'id': getNextID(categories),
            'nome': json['nome']
        }

        categories.append(jsonCategory)

        return (jsonCategory, 201)
    
    elif request.method == 'GET':

        return (categories, 200)


@api.route('/departments/<int:id>', methods=['GET'])
def getDepartmentByID(id: int):
    for department in departments:
        if department['id'] == id:
            return (department, 200)
    return ({'error': 'Departamento não encontrado'}, 404)


@api.route('/departments', methods=['GET', 'POST'])
def departmentHandle():
    if request.method == 'POST':

        json = request.get_json()

        jsonDepartment = {
            'id': getNextID(departments),
            'nome': json['nome']
        }

        departments.append(jsonDepartment)

        return (jsonDepartment, 201)
    
    elif request.method == 'GET':

        return (departments, 200)
