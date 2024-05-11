class Token:
   
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __lst__(self):
        return [str(self.type), int(self.value)]
    
    def __repr__(self):
        return f"Token: {str(self.type)}, Value: {str(self.value)}"