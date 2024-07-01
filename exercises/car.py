class Car():
    body_type = ['suv', 'crossover', 'hatchback', 'sport']
    engine_type = ['electric', 'gas', 'diesel', 'hybrid']
    
    def __init__(self, body_type, engine_type):
        if body_type not in self.body_type:
            raise ValueError("Invalid body type.")
        if engine_type not in self.engine_type:
            raise ValueError("Invalid engine type.")
        self.body_type = body_type
        self.engine_type = engine_type
        
    def describe_car(self):
        return(f"{self.body_type} {self.engine_type}")
    
class Subaru(Car):
    def __init__(self, body_type, engine_type, year, model, trim = None):
        self.year = year #could make raise statements here
        self.model = model
        self.trim = trim
        Car.__init__(self, body_type, engine_type)
        
    def describe(self):
        return f"{self.year} {self.model} {self.trim} {self.describe_car()}"