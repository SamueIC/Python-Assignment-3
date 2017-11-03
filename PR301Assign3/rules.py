# from validator import IFileValidator
from abc import ABCMeta, abstractmethod


class Rules(object):
    def __init__(self):
        self.rules = {'id_rule': IDRule().rule,
                      'gender_rule': GenderRule().rule,
                      'age_rule': AgeRule().rule,
                      'sales_rule': SalesRule().rule,
                      'bmi_rule': BMIRule().rule,
                      'salary_rule': SalaryRule().rule,
                      'birthday_rule': BirthdayRule().rule
                      }


# Abstract Rule Class, #

class Rule(metaclass=ABCMeta):
    def __init__(self):
        self.rule = None

    def get_rule(self):
        return self.rule

    def change_rule(self, new_rule):
        self.rule = new_rule


# Concrete Rule Classes #


class IDRule(Rule):
    def __init__(self):
        super().__init__()
        self.rule = "^[A-Z][0-9]{3}$"


class GenderRule(Rule):
    def __init__(self):
        super().__init__()
        self.rule = "^(M|F)$"


class AgeRule(Rule):
    def __init__(self):
        super().__init__()
        self.rule = "^[0-9]{2}$"


class SalesRule(Rule):
    def __init__(self):
        super().__init__()
        self.rule = "^[0-9]{3}$"


class BMIRule(Rule):
    def __init__(self):
        super().__init__()
        self.rule = "^(Normal|Overweight|Obesity|Underweight)$"


class SalaryRule(Rule):
    def __init__(self):
        super().__init__()
        self.rule = "^[0-9]{2,3}$"


class BirthdayRule(Rule):
    def __init__(self):
        super().__init__()
        self.rule = "^[1-31]-[1-12]-[0-9]{4}$"

a = Rules()
print(a)
b = a.rules
print(b)

 # Expected output: "TEST IDRULE"

# ## OLD RULES CLASS BEFORE DESIGN PATTERN ASSIGNMENT 3 ############################
# class Rules(object):
#     def __init__(self):
#         self.rules = {'id_rule': "^[A-Z][0-9]{3}$",
#                       'gender_rule': "^(M|F)$",
#                       'age_rule': "^[0-9]{2}$",
#                       'sales_rule': "^[0-9]{3}$",
#                       'bmi_rule': "^(Normal|Overweight|Obesity|Underweight)$",
#                       'salary_rule': "^[0-9]{2,3}$",
#                       'birthday_rule': "^[1-31]-[1-12]-[0-9]{4}$"
#                       }
#
#     def get_attr(self, arg):
#         return self.rules[arg]
#
#
# #    def get_attr(self, arg):
# #        return self.rules[arg]
#
# # test dictionary and it's method work correctly
# ##################################################################################
