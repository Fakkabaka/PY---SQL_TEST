class User:
    _count = 0
    
    @classmethod
    def add_user_amount(cls):
        cls._count +=1
    
    def __init__(self, age):
        self.__class__.add_user_amount()
        self.__id = self.__class__._count
        self.__age = age
    
    def get_id(self):
        return self.__id
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    

