from api.models import db, User, Service1, Service2, Service3, BudgetItems


def get_merged_lists(current_user_id):
    serviceSelected = BudgetItems.query.filter_by(
        user_id=current_user_id).first()
    try:
        current_service1_id = serviceSelected.service1_id
        fav_service1 = Service1.query.filter_by(id=current_service1_id)
    except:
        fav_service1 = []
    try:
        current_service2_id = serviceSelected.service2_id
        fav_service2 = Service2.query.filter_by(id=current_service2_id)
    except:
        fav_service2 = []
    try:
        current_service3_id = serviceSelected.service3_id
        fav_service3 = Service3.query.filter_by(id=current_service3_id)
    except:
        fav_service3 = []

    favorite_service1_serial = list(
        map(lambda service1: service1.serialize(), fav_service1))
    favorite_service2_serial = list(
        map(lambda service2: service2.serialize(), fav_service2))
    favorite_service3_serial = list(
        map(lambda service3: service3.serialize(), fav_service3))
    merged_list = favorite_service1_serial + \
        favorite_service2_serial + favorite_service3_serial
    return merged_list


def update_budget_list(budget_list, current_user_id):
    try:
        oldBudget = BudgetItems.query.filter_by(
            user_id=current_user_id).first()
        db.session.delete(oldBudget)
        db.session.commit()

        newBudget = BudgetItems()
        newBudget.user_id = current_user_id
        if budget_list[0] > 0:
            newBudget.service1_id = budget_list[0] #2,3,8
        if budget_list[1] > 0:
            newBudget.service2_id = budget_list[1]
        if budget_list[2] > 0:
            newBudget.service3_id = budget_list[2]

        db.session.add(newBudget)
        db.session.commit()
        return True

    except:
        newBudget = BudgetItems()
        newBudget.user_id = current_user_id
        if budget_list[0] > 0:
            newBudget.service1_id = budget_list[0]
        if budget_list[1] > 0:
            newBudget.service2_id = budget_list[1]
        if budget_list[2] > 0:
            newBudget.service3_id = budget_list[2]

        db.session.add(newBudget)
        db.session.commit()
        return True


def update_favorites_lists(payload_from_request, current_user_id):
    budget_list = []
    for json_item in payload_from_request:
        if json_item["service1_id"]:
            budget_list.append(json_item["service1_id"])
        else:
            budget_list.append(0)
        if json_item["service2_id"]:
            budget_list.append(json_item["service2_id"])
        else:
            budget_list.append(0)
        if json_item["service3_id"]:
            budget_list.append(json_item["service3_id"])
        else:
            budget_list.append(0)

    dbStatus = update_budget_list(budget_list, current_user_id)
    if dbStatus:
        return True

def post_listservice1():
    listserv = [
        {
            "category": "Flores",
            "description": "Boquette, botonier, 10 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 750,
            "provider": "Floristeria de Costa Rica PAX 1"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 15 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 1000,
            "provider": "Floristeria de Costa Rica PAX 2"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 20 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 1500,
            "provider": "Floristeria de Costa Rica PAX 3"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 10 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 1000,
            "provider": "Flores Gala PAX 1"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 15 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 1500,
            "provider": "Flores Gala PAX 2"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 20 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 2000,
            "provider": "Flores Gala PAX 3"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 10 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 420,
            "provider": "Juno Flowers PAX 1"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 15 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 630,
            "provider": "Juno Flowers PAX 2"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 20 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 1110,
            "provider": "Juno Flowers PAX 3"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 10 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 500,
            "provider": "Nandallo PAX 1"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 15 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 750,
            "provider": "Nandallo PAX 2"
        },
        {
            "category": "Flores",
            "description": "Boquette, botonier, 20 centros de mesa, decoracion de iglesia",
            "phone": "N/A",
            "price": 1000,
            "provider": "Nandallo PAX 3"
        }]
    for i in range(len(listserv)):
        body = listserv[i]
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        service = Service1()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']
        db.session.add(service)  # agrega un servicio a la base de datos
        db.session.commit()  # guarda los cambios

def post_listservice2():
    listserv = [{
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 50 personas",  
            "phone": "N/A", 
            "price": 3150, 
            "provider": "Hotel Herradura PAX 1"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 100 personas",  
            "phone": "N/A", 
            "price": 6300, 
            "provider": "Hotel Herradura PAX 2"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 150 personas",  
            "phone": "N/A", 
            "price": 9450,
            "provider": "Hotel Herradura PAX 3"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 50 personas",  
            "phone": "N/A", 
            "price": 3550,
            "provider": "Sheraton Escazu PAX 1"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 100 personas",  
            "phone": "N/A", 
            "price": 7100,
            "provider": "Sheraton Escazu PAX 2"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 150 personas",  
            "phone": "N/A", 
            "price": 10650,
            "provider": "Sheraton Escazu PAX 3"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 50 personas",  
            "phone": "N/A", 
            "price": 3500,
            "provider": "Occidental Papagayo Resort PAX 1"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 100 personas",  
            "phone": "N/A", 
            "price": 7000,
            "provider": "Occidental Papagayo Resort PAX 2"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 150 personas",  
            "phone": "N/A", 
            "price": 10500,
            "provider": "Occidental Papagayo Resort PAX 3"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 50 personas",  
            "phone": "N/A", 
            "price": 3450,
            "provider": "Swiss Travel PAX 1"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 100 personas",  
            "phone": "N/A", 
            "price": 6900,
            "provider": "Swiss Travel PAX 2"
        },
        {
            "category": "Salon y comida", 
            "description": "Incluye desayuno, almuerzo y cena (con bebida) para 150 personas",  
            "phone": "N/A", 
            "price": 10350,
            "provider": "Swiss Travel PAX 3"
        }]
    for i in range(len(listserv)):
        body = listserv[i]
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        service = Service2()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']
        db.session.add(service)  # agrega un servicio a la base de datos
        db.session.commit()  # guarda los cambios

def post_listservice3():
    listserv = [{
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (50 unidades)",  
            "phone": "N/A", 
            "price": 1200, 
            "provider": "Gabriel Anta PAX 1"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (100 unidades)",  
            "phone": "N/A", 
            "price": 1500,
            "provider": "Gabriel Anta PAX 2"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (150 unidades)",  
            "phone": "N/A", 
            "price": 1750,
            "provider": "Gabriel Anta PAX 3"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (50 unidades)",  
            "phone": "N/A", 
            "price": 1000,
            "provider": "Douglas Cedeño PAX 1"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (100 unidades)",  
            "phone": "N/A", 
            "price": 1500,
            "provider": "Douglas Cedeño PAX 2"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (150 unidades)",  
            "phone": "N/A", 
            "price": 2000,
            "provider": "Douglas Cedeño PAX 3"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (50 unidades)",  
            "phone": "N/A", 
            "price": 1000,
            "provider": "Raw Shoots PAX 1"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (100 unidades)",  
            "phone": "N/A", 
            "price": 1250,
            "provider": "Raw Shoots PAX 2"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (150 unidades)",  
            "phone": "N/A", 
            "price": 1500,
            "provider": "Raw Shoots PAX 3"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (50 unidades)",  
            "phone": "N/A", 
            "price": 1500,
            "provider": "Geoff Photography PAX 1"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (100 unidades)",  
            "phone": "N/A", 
            "price": 1750,
            "provider": "Geoff Photography PAX 2"
        },
        {
            "category": "Fotografia", 
            "description": "Fotografias, memoria digital y video (150 unidades)",  
            "phone": "N/A", 
            "price": 2000,
            "provider": "Geoff Photography PAX 3"
        }]
    for i in range(len(listserv)):
        body = listserv[i]
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        service = Service3()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']
        db.session.add(service)  # agrega un servicio a la base de datos
        db.session.commit()  # guarda los cambios