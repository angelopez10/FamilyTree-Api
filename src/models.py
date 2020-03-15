from flask_sqlalchemy import SQLAlchemy
from random import randint

db = SQLAlchemy()

class Family:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [{
            "id": 1,
            "first_name": "John",
            "age": "25",
            "lucky_numbers": "1, 32"
        }]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member ["id"] = self._generateId()
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        self._members = list(filter(lambda member: member['id']!=id,self._members))
        return self._members

    def update_member(self, id, member):
        self._members = list(filter(lambda member: member['id']!=id,self._members))
        return None

    def get_member(self, id):
        member= next(filter(lambda member: member['id']==id,self._members),None)
        return member

  
    def get_all_members(self):
        return self._members