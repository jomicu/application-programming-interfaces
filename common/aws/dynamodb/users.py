from common.utilities.utilities import object_to_dict

from dynamodb.dynamo import DynamoDB


class UsersTable(DynamoDB):

    def __init__(self):
        super().__init__("users-table")

    
    def create_user(self, user):
        item = object_to_dict(user)
        self._create_item(item)


    def get_user(self, user):
        return