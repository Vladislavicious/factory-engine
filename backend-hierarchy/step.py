import json

class simpleEncoder(json.JSONEncoder):
    """Нужен для нормального перевода класса в JSON"""
    def default(self, o):
        return o.__dict__

class Step:
    def __init__(self, name: str, isDone=False, contributor="No-one") -> None:
        self.__isDone = isDone
        self.__contributor = contributor

        self.__name = name.lower()
    
    def __str__(self) -> str:
        if self.__isDone:
            return f"Шаг {self.__name}. Исполнитель: {self.__contributor}"
        return f"Шаг {self.__name} не выполнен"

    def MarkAsDone(self, contributor: str) -> None:
        self.__isDone = True
        self.__contributor = contributor.capitalize() 
    
    def toJSON(self):
        return json.dumps(self, cls=simpleEncoder, sort_keys=True, indent=4, ensure_ascii=False)

    @classmethod
    def fromJSON(cls, jsonString):
        """Возвращает объект класса Step из строки(формата JSON)"""
        info = json.loads(jsonString)
        
        return Step(info["_Step__name"], info["_Step__isDone"], info["_Step__contributor"])

    
boba = Step("Подкраска")

print(Step.fromJSON(boba.toJSON()))