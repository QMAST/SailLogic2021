# coding=utf-8

from sqlalchemy import Column, String

from .entity import Entity, Base, CommandEntity

from marshmallow import Schema, fields

class SailLogicCommand(Entity, Base):
    __tablename__ = 'SailLogicCommand'

    commandID = Column(String)
    commandValue = Column(String)

    def __init__(self, commandID, commandValue, created_by):
        Entity.__init__(self, created_by)
        self.commandID = commandID
        self.commandValue = commandValue
    
### Sail commands, input to boat.
class SailLogicCommandSchema(Schema):
    id = fields.Number()
    commandID = fields.Str()
    commandValue = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
