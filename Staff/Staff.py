from datetime import datetime
import csv


class Staff:

    __id = 100

    def __init__(self, name, wage_rate, given_id=0):
        self._name = name  # str
        Staff.__id += 1
        if given_id == 0: # no arg was passed, so let auto generate
            self._id = self.__id  # int
        else:
            self._id = given_id
        self._wage_rate = wage_rate
        self._date_hired = datetime.now().strftime("%d/%m/%y")
        self._hours_worked = 0  # Float
        self._overtime_hours = 0  # Float
        self._sick_days_available = 0  # Float
        self._is_manager = False

    # Getters
    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_wage_rate(self):
        return self._wage_rate

    def get_date_hired(self):
        return self._date_hired

    def get_hours_worked(self):
        return self._hours_worked

    def get_overtime_hours(self):
        return self._overtime_hours

    def get_sick_days(self):
        return self._sick_days_available

    def get_is_manager(self):
        return self._is_manager

    # Setters
    def set_name(self, new_name):
        self._name = new_name

    def set_id(self, new_id):
        self._id = new_id

    def set_wage_rate(self, new_wage_rate):
        self._wage_rate = new_wage_rate

    def set_date_hired(self, new_date_hired):
        self._date_hired = new_date_hired

    def set_hours_worked(self, new_hours_worked):
        self._hours_worked = new_hours_worked

    def set_overtime_hours(self, new_overtime_hours):
        self._overtime_hours = new_overtime_hours

    def get_sick_days(self):
        return self._sick_days_available

    def set_is_manager(self, is_manager):
        self._is_manager = is_manager

    def clock_hours_worked(self, hours):
        """
        Use this method to add hours every day that an employee works.
        :param hours:
        :return:
        """
        self._hours_worked += hours

    def __str__(self):
        return f"id# {self._id}, {self._name}"
