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
            newBudget.service1_id = budget_list[0]
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
    list_test = Service1.getAllService()
    if len(list_test) == 0:        
        listserv = [
            {
                "category": "Flores",
                "description": "Boquette, botonier, 10 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 750,
                "provider": "Floristeria de Costa Rica Paq.1",
                "url": "https://cdn.shopify.com/s/files/1/0445/3692/2277/products/Arreglorosarosacaja22.500_540x.jpg?v=1595985154"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 15 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 1000,
                "provider": "Floristeria de Costa Rica Paq.2",
                "url": "https://cdn.shopify.com/s/files/1/0445/3692/2277/products/ArreglocajaRosarosada22.500_1024x1024@2x.jpg?v=1595901004"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 20 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 1500,
                "provider": "Floristeria de Costa Rica Paq.3",
                "url": "https://cdn.shopify.com/s/files/1/0445/3692/2277/products/PicsArt_03-07-10.22.23_720x.jpg?v=1615348879"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 10 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 1000,
                "provider": "Flores Gala Paq.1",
                "url": "https://floresgala.com/wp-content/uploads/2018/06/DBFG-0008.jpg"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 15 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 1500,
                "provider": "Flores Gala Paq.2",
                "url": "https://floresgala.com/wp-content/uploads/2018/06/DBFG-0004.jpg"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 20 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 2000,
                "provider": "Flores Gala Paq.3",
                "url": "https://floresgala.com/wp-content/uploads/2018/06/DBFG-0009.jpg"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 10 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 420,
                "provider": "Juno Flowers Paq.1",
                "url": "https://cdn.shopify.com/s/files/1/0268/6595/8935/products/20200811_111957-02_8debca13-0b9e-423f-ae3c-b4214e3c7acc_720x.jpg?v=1605909434"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 15 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 630,
                "provider": "Juno Flowers Paq.2",
                "url": "https://cdn.shopify.com/s/files/1/0268/6595/8935/products/20201110_081340-02-01_360x.jpg?v=1605834915"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 20 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 1110,
                "provider": "Juno Flowers Paq.3",
                "url": "https://cdn.shopify.com/s/files/1/0268/6595/8935/products/20201116_085559-01_360x.jpg?v=1605834549"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 10 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 500,
                "provider": "Nandallo Paq.1",
                "url": "https://i.pinimg.com/originals/e4/64/07/e4640736b7ba5f240eb1e9447c030b50.jpg"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 15 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 750,
                "provider": "Nandallo Paq.2",
                "url": "https://lasbodasoriginales.com/wp-content/uploads/2018/02/Ramo-de-novia-con-peon%C3%ADas-en-rosa-y-blanco.jpg"
            },
            {
                "category": "Flores",
                "description": "Boquette, botonier, 20 centros de mesa, decoracion de iglesia",
                "phone": "N/A",
                "price": 1000,
                "provider": "Nandallo Paq.3",
                "url": "https://i.pinimg.com/originals/c1/c8/87/c1c8874822d8b96ac2a8b56d7f35b4ec.png"
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
            if 'url' not in body:
                return "You need to specify the url", 400
            service = Service1()
            service.category = body['category']
            service.description = body['description']
            service.provider = body['provider']
            service.phone = body['phone']
            service.price = body['price']
            service.url = body['url']
            db.session.add(service)  # agrega un servicio a la base de datos
            db.session.commit()  # guarda los cambios

def post_listservice2():
    list_test = Service2.getAllService()
    if len(list_test) == 0:
        listserv = [{
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 50 personas",  
                "phone": "N/A", 
                "price": 3150, 
                "provider": "Hotel Herradura Paq.1",
                "url": "https://s.ineventos.com/cr/2015/10/116494/hotel-wyndham-san-jose-herradura-178709-i-640w.jpg"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 100 personas",  
                "phone": "N/A", 
                "price": 6300, 
                "provider": "Hotel Herradura Paq.2",
                "url": "https://revistasumma.com/wp-content/uploads/2017/04/unnamed-3-2.jpg"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 150 personas",  
                "phone": "N/A", 
                "price": 9450,
                "provider": "Hotel Herradura Paq.3",
                "url": "https://livingandtravel.com.mx/wp-content/uploads/2018/01/OCV-aguascalientes.jpg"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 50 personas",  
                "phone": "N/A", 
                "price": 3550,
                "provider": "Sheraton Escazu Paq.1",
                "url": "https://cdnh.octanio.com/hotel-Sheraton-San-Jose-Costa-Rica-FG800_134320_15.jpg"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 100 personas",  
                "phone": "N/A", 
                "price": 7100,
                "provider": "Sheraton Escazu Paq.2",
                "url": "https://d2poxrheyfxwbo.cloudfront.net/resize/780x500/filters:quality(65):max_age(2604800)/s3/hotel/905a63bb-0a32-4442-abd4-db9ada27c361"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 150 personas",  
                "phone": "N/A", 
                "price": 10650,
                "provider": "Sheraton Escazu Paq.3",
                "url": "https://d2poxrheyfxwbo.cloudfront.net/resize/780x500/filters:quality(65):max_age(2604800)/s3/hotel/15ab5afa-43aa-4538-8cea-9b1b8e8ab597"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 50 personas",  
                "phone": "N/A", 
                "price": 3500,
                "provider": "Occidental Papagayo Resort Paq.1",
                "url": "https://static.barcelo.com/content/dam/bhg/master/es/hoteles/costa-rica/golfo-papagayo/occidental-papagayo-adults-only/gastronomia/OPAP_GAST_11.jpg.bhgimg.square1100.jpg/1604612609735.jpg"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 100 personas",  
                "phone": "N/A", 
                "price": 7000,
                "provider": "Occidental Papagayo Resort Paq.2",
                "url": "https://www.oyster.com/wp-content/uploads/sites/35/2019/05/buffet-v15200549-1440-1024x683.jpg"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 150 personas",  
                "phone": "N/A", 
                "price": 10500,
                "provider": "Occidental Papagayo Resort Paq.3",
                "url": "https://static.barcelo.com/content/dam/bhg/master/es/hoteles/costa-rica/golfo-papagayo/occidental-papagayo-adults-only/gastronomia/OPAP_GAST_12.jpg.bhgimg.square1100.jpg/1604612521691.jpg"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 50 personas",  
                "phone": "N/A", 
                "price": 3450,
                "provider": "Swiss Travel Paq.1",
                "url": "https://lh3.googleusercontent.com/proxy/lZRsfR2wwD1h4oNWqAOni3OM367Mbp32KwLRm84To2usYti4xEATAOnueO1pR-XkKib9QFVj-DY7sTAq7dPfkwWTDMM3OrmOHU2A_TKUODA_EipxLSKihBL65GGSp9ToLeU5xctjKkI"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 100 personas",  
                "phone": "N/A", 
                "price": 6900,
                "provider": "Swiss Travel Paq.2",
                "url": "https://lh3.googleusercontent.com/proxy/D9FHnnADOR8Z9Yf5pnTfv6paXw6hGadn22O1vQJWByA7LWWmy8GlM1wqpsyXQ05xsYVr3Mc10dxtflTC8dkadJOw10kvyKLHO-hZZaF7pyd9KceN_iafnA5K"
            },
            {
                "category": "Salon y comida", 
                "description": "Incluye desayuno, almuerzo y cena (con bebida) para 150 personas",  
                "phone": "N/A", 
                "price": 10350,
                "provider": "Swiss Travel Paq.3",
                "url": "https://lh3.googleusercontent.com/proxy/rO9SOY33Yn6uSegAVZB-zur-zbOfNO7Av6BGcyYg6l_-q5SIlOgxNRqIDcC9coOetloOhmaFYw2IiUycDJr-grvmHSYMbI7lUfUvHxpRz73k4doKj89VbnK2"
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
            if 'url' not in body:
                return "You need to specify the url", 400
            service = Service2()
            service.category = body['category']
            service.description = body['description']
            service.provider = body['provider']
            service.phone = body['phone']
            service.price = body['price']
            service.url = body['url']
            db.session.add(service)  # agrega un servicio a la base de datos
            db.session.commit()  # guarda los cambios

def post_listservice3():
    list_test = Service3.getAllService()
    if len(list_test) == 0:
        listserv = [{
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (50 unidades)",  
                "phone": "N/A", 
                "price": 1200, 
                "provider": "Gabriel Anta Paq.1",
                "url": "https://gabrielanta.com/wp-content/uploads/2016/09/01-IMG_0804-1.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (100 unidades)",  
                "phone": "N/A", 
                "price": 1500,
                "provider": "Gabriel Anta Paq.2",
                "url": "https://gabrielanta.com/wp-content/uploads/2017/02/bodas-en-cahuita-puerto-viejo.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (150 unidades)",  
                "phone": "N/A", 
                "price": 1750,
                "provider": "Gabriel Anta Paq.3",
                "url": "https://gabrielanta.com/wp-content/uploads/2016/09/fotografo-bodas-matrimonio-puerto-viejo-punta-uva-costa-rica-02-1024x767.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (50 unidades)",  
                "phone": "N/A", 
                "price": 1000,
                "provider": "Douglas Cedeño Paq.1",
                "url": "https://www.douglascedeno.com/wp-content/uploads/2021/02/fotografos-de-bodas-costa-rica-decoracion-para-bodas-salon-de-eventos-costa-rica-bodas-costa-rica-paquetes-de-boda-economicos-costa-rica-pictures-91.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (100 unidades)",  
                "phone": "N/A", 
                "price": 1500,
                "provider": "Douglas Cedeño Paq.2",
                "url": "https://www.douglascedeno.com/wp-content/uploads/2021/02/Bodas-marriott-costa-rica-fotografo-de-bodas-costa-rica-fotografo-profesional-pictures-19.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (150 unidades)",  
                "phone": "N/A", 
                "price": 2000,
                "provider": "Douglas Cedeño Paq.3",
                "url": "https://www.douglascedeno.com/wp-content/uploads/2021/02/fotografos-de-bodas-costa-rica-decoracion-para-bodas-salon-de-eventos-costa-rica-bodas-costa-rica-paquetes-de-boda-economicos-costa-rica-pictures-85-1.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (50 unidades)",  
                "phone": "N/A", 
                "price": 1000,
                "provider": "Raw Shoots Paq.1",
                "url": "https://www.rawshoots.com/wp-content/uploads/2020/02/WEB-566-e1585708060883-1238x696.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (100 unidades)",  
                "phone": "N/A", 
                "price": 1250,
                "provider": "Raw Shoots Paq.2",
                "url": "https://www.rawshoots.com/wp-content/uploads/2020/02/WEB-285-3-1238x884.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (150 unidades)",  
                "phone": "N/A", 
                "price": 1500,
                "provider": "Raw Shoots Paq.3",
                "url": "https://www.rawshoots.com/wp-content/uploads/2020/04/SNEAKPEEK_EM-30-1238x825.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (50 unidades)",  
                "phone": "N/A", 
                "price": 1500,
                "provider": "Geoff Photography Paq.1",
                "url": "https://s.ineventos.com/cr/2017/07/121569/geoffphotography-235919-i-640w.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (100 unidades)",  
                "phone": "N/A", 
                "price": 1750,
                "provider": "Geoff Photography Paq.2",
                "url": "https://s.ineventos.com/cr/2017/07/121569/geoffphotography-235080-i-640w.jpg"
            },
            {
                "category": "Fotografia", 
                "description": "Fotografias, memoria digital y video (150 unidades)",  
                "phone": "N/A", 
                "price": 2000,
                "provider": "Geoff Photography Paq.3",
                "url": "https://s.ineventos.com/cr/2017/07/121569/geoffphotography-235921-i-1080w.jpg"
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
            if 'url' not in body:
                return "You need to specify the url", 400
            service = Service3()
            service.category = body['category']
            service.description = body['description']
            service.provider = body['provider']
            service.phone = body['phone']
            service.price = body['price']
            service.url = body['url']
            db.session.add(service)  # agrega un servicio a la base de datos
            db.session.commit()  # guarda los cambios