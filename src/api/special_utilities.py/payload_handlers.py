from api.models import db, User,Color,FavoriteColor

#*----The purpose of the payload handlers is to check the current state of databases and updated them when the user has submit the information

def merge_currentUser_data(current_user_id):
    pass

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