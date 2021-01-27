from pymongo import MongoClient
from settings import MONGO_DB
from settings import MONGODB_LINK

mdb = MongoClient(MONGODB_LINK)[MONGO_DB]

def search_or_save_user(mdb, effective_user):
    user = mdb.users.find_one({"userId": effective_user.id})  
    if not user:  
        user = {
            "userId": effective_user.id,
            "user_name": effective_user.username,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            'nick': None,
            "state": -2,
            "reviews": [],
        }
        mdb.users.insert_one(user)  
    return user

def add_review(mdb, userId, review):
    mdb.users.update_one({ 'userId' : userId }, {'$addToSet' : { 'reviews' : review }})

def get_current_state(mdb, userId):
    user = mdb.users.find_one({"userId": userId})
    if not user:  
        user = {
            "userId": userId,
            "state": -2,
            "reviews": [],
        }
        mdb.users.insert_one(user)
    return user['state']

def set_state(mdb, userId, state):
    mdb.users.update_one(
        {'userId': userId },
        {'$set': {"state": state}}
    )
     
def update_user_field(mdb, userId, fieldName, value):
    user = mdb.users.find_one( {'userId' : userId } )
    if not user:
        return None
    mdb.users.update_one( {'userId': userId}, { '$set': {fieldName: value}} )
    return

def update_coach_field(mdb, coachName, fieldName, value):
    coach = mdb.coaches.find_one( {'coachName': coachName } )
    if not coach:
        return None
    mdb.coaches.update_one( {'coachName': coachName}, { '$set': {fieldName : value}} )
    return

def update_training_field(mdb, trainId, fieldName, value):
    training = mdb.trainings.find_one( {'trainId' : trainId } )
    if not training:
        return None
    mdb.trainings.update_one( {'trainId': trainId}, { '$set': {fieldName: value}} )
    return

def update_court_field(mdb, courtId, fieldName, value):
    court = mdb.courts.find_one( {'courtId': courtId } )
    if not court:
        return None
    mdb.courts.update_one( {'courtId': courtId}, { '$set': {fieldName: value}} )
    return

def update_game_field(mdb, gameId, fieldName, value):
    game = mdb.games.find_one( {'gameId': gameId } )
    if not game:
        return None
    mdb.games.update_one( {'gameId': gameId}, { '$set': {fieldName: value}} )
    return

def update_booking_field(mdb, bookingId, fieldName, value):
    booking = mdb.bookings.find_one( {'bookingId': bookingId } )
    if not booking:
        return None
    mdb.bookings.update_one( {'bookingId': bookingId}, { '$set': {fieldName: value}} )
    return

def add_booking_to_court(mdb, courtId, booking):
    mdb.courts.update_one({'courtId': courtId}, {'$addToSet': { 'bookings': booking}})
    
def add_training_to_coach(mdb, coachName, training):
    mdb.courts.update_one({'coachName': coachName}, {'$addToSet': { 'trainings': training}})
    
def add_player_to_training(mdb, trainId, userId):
    mdb.trainings.update_one({'coachName': coachName}, {'$addToSet': { 'trainings': training}})
    
def get_court(mdb, courtId):
    court = mdb.courts.find_one({"courtId": courtId})
    if not court:
        court = {
            'courtId': courtId,
            'bookings': [],
        }
        mdb.courts.insert_one(court)
    return court
        
def get_coach(mdb, coachName):
    coach = mdb.coaches.find_one({"coachName": coachName})
    if not coach:
        coach = {
            'coachName': coachName,
            'trainings': [],
        }
        mdb.coaches.insert_one(coach)
    return coach

def get_training(mdb, trainId):
    training = mdb.trainings.find_one({"trainId": trainId})
    if not training: 
        training = {
            'trainId': trainId,
            'date': None,
            'court': None,
            'coach': None,
            'price': None,
            'level': None,
            'players': [],
            'max_players': None,
            'free_places': None,
        }
        mdb.trainings.insert_one(training)
    return training

def get_game(mdb, gameId):
    game = mdb.games.find_one({"gameId": gameId})
    if not game: 
        game = {
            'gameId': gameId,
            'date': None,
            'court': None,
            'price': None,
            'level': None,
            'players': [],
            'max_players': None,
            'free_places': None,
        }
        mdb.games.insert_one(game)
    return game
    
def get_booking(mdb, bookingId):
    booking = mdb.bookings.find_one({"bookingId": bookingId})
    if not booking: 
        booking = {
            'bookingId': bookingId,
            'start': None,
            'court': None,
            'duration': None,
            'end': None,
            'nick': None,
        }
        mdb.bookings.insert_one(booking)
    return booking 

def check_booking(mdb, bookingId):
    booking = mdb.bookings.find_one({"bookingId": bookingId})
    if not booking:
        return None
    return booking