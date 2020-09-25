from .entities.SailLogicCommand import SailLogicCommand, SailLogicCommandSchema

class SailLogic:
    commandID = ''
    commandValue = ''
    def __init__(self):
        #TODO
        self.establishState()
    
    def establishState(self):
        #TODO
        #We need to decide if state should be persited or not.
    
    #TODO enum out commands
    def decodeCommand(self, command):
        self.commandID =  command.commandID
        self.commandValue = command.commandValue

