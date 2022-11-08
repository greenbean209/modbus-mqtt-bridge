from abc import ABCMeta, abstractmethod

class PLC(metaclass=ABCMeta):
    
    @abstractmethod
    def get_manufacturer(self):
        return self.manufacturer

    @abstractmethod
    def get_model(self):
        return self.model

class AB_PLC(PLC):
    def __init__(self, model) -> None:
        super().__init__()
        self.manufacturer = 'Allen Bradley'
        self.model = model
    
    def get_manufacturer(self):
        return self.manufacturer
    
    def get_model(self):
        return self.model


cl_plc = AB_PLC('Compact Logix')
print(cl_plc.get_manufacturer())
print(cl_plc.get_model())
