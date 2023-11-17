
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = []

 
    def generate_Id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        
        if not "id" in member:
            id = self.generate_Id()
            member["id"] = id
        self._members.append(member)

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
        return self._members

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member

    def all_members(self):
        return self._members
