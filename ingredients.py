# inventory manager will manage these classes

class Ingredients():
    """
    The ingredients class will be a super class to specific classes of ingredients.
    """
    def __init__(self, name, amount):
        """
        Creates an instance of an ingredient.

        Param: 1 string, ingredient name
        Param: 1 int, ingredient amount
        """
        self._name = name
        self._amount = amount

    def set_amount(self, new_amount):
        """
        Sets the amount of the ingredient in int

        Param: int, the new ingredient amount
        """
        self._amount = new_amount

    def get_amount(self):
        """
        Gets the amount of the ingredient.

        Returns: int, the ingredient amount.
        """
        return self._amount

    def __str__(self):
        """
        The to_string method of this class.

        Returns: an identifying string with the ingredient name and amount.
        """
        return "Ingredient: {}, Amount: {}".format(self._name, self._amount)


class DryGoods(Ingredients):
    """
    A child of the Ingredients class.
    Will increase it's amount for each instance added of this same name.
    No expiration.
    """
    def __init__(self, type, grams):
        """
        Creates an instance of a drygood ingredient.
        Each name is an instance of an ingredient

        Param: 1 string, ingredient name
        Param: an int, ingredient amount in grams
        """
        super().__init__(type, grams)

    def increase_amt(self, grams):
        """
        Increases the amount of the current dry good.
        Instead of having multiple instances of the same dry good, the new amount is added to the old.

        Param: 1 int, grams of item added.
        """
        super().set_amount(super().get_amount() + grams)

    def __str__(self):
        return (super(DryGoods, self).__str__() + " grams")

class Liquids(Ingredients):
    """
    A child of the Ingredients class.
    Each instance is different with its own expiration date.
    """
    def __init__(self, bottle, ounces, expiration):
        """
        Creates an instance of a liquid ingredient.

        Param: 1 string, ingredient name of bottle
        Param: 1 integer of ounces in the item
        Param: 1 string of expiration date
        """
        super().__init__(bottle, ounces)
        self._expiration = expiration

    def get_expiration(self):
        return self._expiration

    def __str__(self):
        return (super(Liquids, self).__str__() + " ounces, Expiration Date: " + self._expiration)

class Meats(Ingredients):
    """
    A child of the Ingredients class.
    """
    def __init__(self, meat, ounces, date):
        """
        Creates an instance of a raw meat ingredient.
        Expires after 3 days
        This will be simplified and assume each month has 30 days.

        Param: 1 string, meat name
        Param: 1 int, ounces of meat
        Param: 1 string, date of purchase in the format "DD/MM/YY"
        """
        super().__init__(meat, ounces)
        self._expiration = self.set_expiration(date)

    def set_expiration(self, purchase_date):
        if (int(purchase_date[0] + purchase_date[1]) < 28):
            return (str(int(purchase_date[0] + purchase_date[1]) + 3) + purchase_date[2:])
        elif (int(purchase_date[3:5]) == 12):
            (str((int(purchase_date[0] + purchase_date[1]) + 3)%30) + "/01/" + str(int(purchase_date[6:]) +1))
        else:
            return (str((int(purchase_date[0] + purchase_date[1]) + 3)%30) + "/" + str(int(purchase_date[3:5]) + 1) + purchase_date[5:])

    def get_expiration(self):
        return self._expiration

    def __str__(self):
        return (super(Meats, self).__str__() + " ounces, Expiration Date: " + self._expiration)

class Produce(Ingredients):
    """
    A child of the Ingredients class.
    """
    def __init__(self, name, grams, date):
        """
        Creates an instance of a produce ingredient.
        Expires after 1 week.

        Param: 1 string, produce name
        Param: 1 int, produce amount in grams
        Param: 1 string, purchase date in the format "DD/MM/YY"
        """
        super().__init__(name, grams)
        self._expiration = self.set_expiration(date)

    def set_expiration(self, purchase_date):
        if (int(purchase_date[0] + purchase_date[1]) < 24):
            return (str(int(purchase_date[0] + purchase_date[1]) + 7) + purchase_date[2:])
        elif (int(purchase_date[3:5]) == 12):
            (str((int(purchase_date[0] + purchase_date[1]) + 7)%30) + "/01/" + str(int(purchase_date[6:]) +1))
        else:
            return (str((int(purchase_date[0] + purchase_date[1]) + 7)%30) + "/" + str(int(purchase_date[3:5]) + 1) + purchase_date[5:])

    def get_expiration(self):
        return self._expiration

    def __str__(self):
        return (super(Produce, self).__str__() + " ounces, Expiration Date: " + self._expiration)
