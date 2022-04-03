from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr


from common.enums.naming_conventions import NamingConventions
from common.transformers.dictionary import DictionaryTransformer


class DynamoDB(object):


    def __init__(self, table_name: str, hash_key: str, sort_key: str):
        dynamodb = resource("dynamodb")
        self._table = dynamodb.Table(table_name)
        self._hash_key = hash_key
        self._sort_key = sort_key


    def _create_document(self, item: dict):
        item = DictionaryTransformer.update_naming_convention(item, NamingConventions.SNAKE, NamingConventions.PASCAL)
        self._table.put_item(Item=item)


    def _get_document_by_hash_key(self, hash_key: str):
        return self._table.query(KeyConditionExpression=Key(self._hash_key).eq(hash_key))

    
    def _update_document(self, item: dict, hash_key: str, sort_key: str):
        update_expression: str = self.build_update_expression(item, self._hash_key)
        update_attributes: str = self.build_expression_attribute_values(item, self._hash_key)
        update_key: dict = { self._hash_key: hash_key, self._sort_key: sort_key }

        return self._table.update_item(
            Key=update_key,
            UpdateExpression=update_expression,
            ExpressionAttributesValues=update_attributes,
            ReturnValue="UPDATE_NEW"
        )

    
    def __scan(self, filter_expression: str, limit: int, exclusive_start_key: str = None):
        return self._table.scan(
            FilterExpression=filter_expression,
            ExclusiveStartKey=exclusive_start_key,
            Limit=limit
        )


    def _scan_full(self, filter_expression: str, limit: int = pow(2, 32)):
        result = self.__scan(filter_expression, limit=limit)
        last_evaluated_key = result.get("LastEvaluatedKey")
        items = result["Items"]

        while last_evaluated_key is not None:
            result = self.__scan(filter_expression, last_evaluated_key, limit)
            items.extend(result["Items"])
            last_evaluated_key = result.get("LastEvaluatedKey")

        result["Items"] = items
        result["Count"] = len(items)

        return result

    
    @staticmethod
    def build_update_expression(item, hash_key: str) -> str:
        return "set {}".format(
            ",".join(f"{k}=:{k}" for k in item if k != hash_key)
        )

    
    @staticmethod
    def build_expression_attribute_values(item, hash_key: str) -> dict:
        return {f":{k}": v for k, v in item.items() if k != hash_key}

