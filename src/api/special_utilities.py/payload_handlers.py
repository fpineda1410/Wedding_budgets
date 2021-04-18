from api.models import db, User,Color,FavoriteColor

#*----The purpose of the payload handlers is to check the current state of databases and updated them when the user has submit the information

def get_merged_lists(current_user_id):
    serviceSelected = BudgetItems.query.filter_by(user_id=current_user_id)
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

def depurate_favorite_data (incoming_list,current_user_id):
     pass

def update_favorite_data (incoming_list,current_user_id):
    pass

def update_favorites_lists (payload_from_request,current_user_id):
    #*correct order of execution
    #*recommended modify payload_from_request in order to make it a list
    depurate_favorite_data(payload_from_request,current_user_id)
    update_favorite_data(payload_from_request,current_user_id)
    merge_currentUser_data(current_user_id)