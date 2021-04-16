from api.models import db, Color,FavoriteColor
import requests

#*---The purpose of this method is to load any default data into the databases, usually when fetching from external API

def initial_colors_load ():
    colors=['red', 'green', 'yellow']    
    for index in range (len(colors)):
        colors_initial_values=Color(id=index,color=colors[index])
        db.session.add(colors_initial_values)
    db.session.commit()

def initial_loader():
    initial_colors_load()