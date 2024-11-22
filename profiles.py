from database import personal_data_collection, notes_collection

def get_values(_id):
    return {
        "_id": _id,
        "general": {
            "name": "",
            "age": 51,
            "weight": 66,
            "height": 162,
            "activity_level": "Select an activity level",
            "menopause_symptoms": "Choose As Many That Apply"
        },
        "goals": ["Muscle Gain"],
        "nutrition": {
            "calories": 2000,
            "protein": 140,
            "fat": 20,
            "carbs": 100,
        },
    }
    
def create_profile(_id):
    profile_values = get_values(_id)
    result = personal_data_collection.insert_one(profile_values)
    return result.inserted_id, result

def get_profile(_id):
    return personal_data_collection.find_one({"_id": {"$eq": _id}})

def get_notes(_id):
    return list(notes_collection.find({"user_id": {"$eq": _id}}))