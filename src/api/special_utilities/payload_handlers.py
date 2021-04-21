from api.models import db, User, Service1, Service2, Service3, BudgetItems

def get_merged_lists(current_user_id):
    serviceSelected = BudgetItems.query.filter_by(user_id=current_user_id).first()
    try:        
        current_service1_id = serviceSelected.service1_id
        fav_service1 = Service1.query.filter_by(id=current_service1_id)  
    except:
        fav_service1=[]
    try:
        current_service2_id = serviceSelected.service2_id
        fav_service2 = Service2.query.filter_by(id=current_service2_id)
    except:
        fav_service2=[]
    try:
        current_service3_id = serviceSelected.service3_id
        fav_service3 = Service3.query.filter_by(id=current_service3_id)
    except:
        fav_service3=[]

    favorite_service1_serial = list(map(lambda service1: service1.serialize(), fav_service1))
    favorite_service2_serial = list(map(lambda service2: service2.serialize(), fav_service2))
    favorite_service3_serial = list(map(lambda service3: service3.serialize(), fav_service3))
    merged_list = favorite_service1_serial + favorite_service2_serial + favorite_service3_serial
    return merged_list

def update_budget_list (budget_list,current_user_id):
    try:
        oldBudget = BudgetItems.query.filter_by(user_id=current_user_id).first()
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
        # return newBudget 
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
        # return newBudget

def update_favorites_lists (payload_from_request,current_user_id):
    budget_list=[]
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

    dbStatus = update_budget_list (budget_list,current_user_id)
    if dbStatus:
        return True
    # return dbStatus