from os import environ


from common.transformers.dictionary import ObjectToDictionary
from common.aws.dynamo import DynamoDB


class UsersTable(DynamoDB):


    def __init__(self):
        super().__init__(environ.get("USERS_TABLE_NAME"), "Id", "")

    
    def create_user(self, user):
        transformer = ObjectToDictionary()
        item = transformer.parse(user)
        self._create_item(item)


    def get_user(self, user):
        return