from typing import List
from typing import Dict
from datetime import date
from dataclasses import dataclass
from collections import defaultdict

from step import *
from order import *
from listFuncs import *
from mail import *
from Contribution import *


@dataclass
class ContributionID:
    Order_id: int
    product_name: str
    step_name: str
    koef_value: int

def getContributionsByContributor(contributor: str, orderList: List[Order]):
    """Возвращает словарь Contribution : ContributionID"""
    dictionary = dict()
    
    for order in orderList:
        for product in order.GetProducts():
            for step in product.GetSteps():
                for contr in step.GetContr():
                    print(contr.__str__())
                    if contr.contributor == contributor:
                        dictionary[contr] = ContributionID(order.id, product.name, step.name, step.koef_value_done)
    
    return dictionary

def getKoefSum(dictionary: Dict[Contribution, ContributionID]) -> Dict[date, float]:
    """Возвращает словарь Дата : выполненные коэф-ты"""
    koef_dict = defaultdict(lambda: 0.)
    for index in dictionary.keys():
        koef_dict[index.date_of_creation] += dictionary[index].koef_value

    return koef_dict 