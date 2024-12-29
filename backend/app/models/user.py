class User:
    def __init__(self, db):
        self.collection = db.users

    def create_user(self, user_data):
        return self.collection.insert_one(user_data)

    def find_user_by_email(self, email):
        return self.collection.find_one({"email": email})
