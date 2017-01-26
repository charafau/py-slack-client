import colander

#TODO: add unit test for parsing
class Channel(colander.MappingSchema):
    id = colander.SchemaNode(colander.String())
    name = colander.SchemaNode(colander.String())
    is_member = colander.SchemaNode(colander.Boolean())
    is_archived = colander.SchemaNode(colander.Boolean())
    is_general = colander.SchemaNode(colander.Boolean())
    num_members = colander.SchemaNode(colander.Integer())
    # created = colander.SchemaNode(colander.Time())
