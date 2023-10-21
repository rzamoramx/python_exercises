
from graphene import ObjectType, String, Schema


class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name + ' from GraphQL!'


schema = Schema(query=Query)

