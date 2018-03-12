#
# Team Shrug
# Project1
#

import csv
import re
import ingredients as ing
import subprocess as sub
import os


class InventoryManager():
    """
    InventoryManager will manage the Ingredients classes.
    Functionality:
    -Upload a CSV file to create ingredient objects
    -Show a list of ALL ingredients
    -Show a list of each type of ingredient
    -Delete away expired ingredients : edit CSV file to reflect changes
    -view a CSV file of the ingredients
    -Add new ingredients: use regular expressions to validate entries for new ingredients
    """

    def __init__(self):
        """
        Creates an instance of an InventoryManager
        """
        self._ingredients_count = 0
        # lets make a list of drygood objects
        self._drygoods = []

        # lets make a list of liquid objects
        self._liquids = []

        # lets make a list of meat objects
        self._meat = []

        # lets make a list of drygood objects
        self._produce = []

    def get_ingredients_count(self):
        """
        gets number of ingredients currently listed in inventorymanager.

        Returns: int, the number of ingredients
        """
        return self._ingredients_count

    def get_drygoods_count(self):
        """
        gets number of dry good ingredients currently listed in inventorymanager.

        Returns: int, the number of drygoods
        """
        return len(self._drygoods)

    def get_liquids_count(self):
        """
        gets number of liquid ingredients currently listed in inventorymanager.

        Returns: int, the number of liquids
        """
        return len(self._liquids)

    def get_meats_count(self):
        """
        gets number of meat ingredients currently listed in inventorymanager.

        Returns: int, the amount of meat
        """
        return len(self._meat)

    def get_produce_count(self):
        """
        gets number of produce ingredients currently listed in inventorymanager.

        Returns: int, the number of produce
        """
        return len(self._produce)

    def upload_drygood_csv(self, fname):
        """
        Takes in a dry good csv file and creates a DryGood object for each entry.

        Param: fname, the string of the cvs file name.
        """
        # make sure you can open the file
        try:
            with open(fname, "r", newline="") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if reader.line_num == 1:
                        # skip first line
                        continue

                    # create a drygoods object for every entry
                    type = row["Ingredient"]
                    grams = row["Amount"]
                    self._drygoods.append(ing.DryGoods(type, grams))
                    # keep track of how many ingredients we have
                    self._ingredients_count += 1
        except EnvironmentError:  # parent of IOError, OSError and WindowsError where available
            print("Error: {} could not be found.".format(fname))

    def new_drygood(self, fname, new_item, new_amount):
        """
        Adds a new drygood object.
        Changes the CSV file to reflect the new item.

        Param: fname, string for csv file name
        Param: new_item, string name of new entry
        Param: new_amount, int quantity
        """
        # make sure the new_amount is a positive integer
        if str(new_amount).isdigit():
            with open(fname, "a+", newline="") as f:
                self._drygoods.append(ing.DryGoods(new_item, new_amount))
                f.write(new_item + "," + str(new_amount) + "\n")
        else:
            print("Error: Please make sure to enter a positive integer for the quantity")

    def add_more_drygood(self, fname, item, amount):
        """
        Add more of an existing drygood

        Param: fname, a string of the filename to add to
        Param: item, a string of the item name
        Param: amount, an int of the amount to add
        """
        # make a flag to make sure the name IS in our list
        is_found = False

        # make sure the amount is a pos number. data validation.
        if str(amount).isdigit():
            for each in self._drygoods:
                # find the item in the list
                if each.get_name().lower() == item.lower():
                    is_found = True
                    # change the amount for the object
                    each.increase_amt(amount)

                    # Rewrite the file to update
                    try:
                        with open(fname, "r", newline="") as f:
                            reader = csv.DictReader(f)
                            data = list(reader)
                            headers = reader.fieldnames
                        with open(fname, 'w', newline='') as f:
                            writer = csv.DictWriter(f, headers)
                            # if row is Avienda's, update Quantity
                            writer.writeheader()
                            for row in data:
                                if row["Ingredient"].lower() == item.lower():
                                    row["Amount"] = str(int(row["Amount"]) + amount)
                                writer.writerow(row)
                    except EnvironmentError:  # parent of IOError, OSError and WindowsError where available
                        print("Error: {} could not be found.".format(fname))

            if not is_found:
                print("Error: {} is not in the list of dry goods.".format(item))

        else:
            print("Error: Please make sure to only enter positive number for the quantity")

    def upload_liquid_csv(self, fname):
        """
        Takes in a liquid csv file and creates a Liquid object for each entry.

        Param: fname, the string of the cvs file name.
        """
        try:
            with open(fname, "r", newline="") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if reader.line_num == 1:
                        # skip first line
                        continue

                    # create a drygoods object for every entry
                    bottle = row["Ingredient"]
                    ounces = row["Amount"]
                    expiration = row["Expiration Date"]
                    self._liquids.append(ing.Liquids(bottle, ounces, expiration))
                    # keep track of how many ingredients we have
                    self._ingredients_count += 1
        except EnvironmentError:  # parent of IOError, OSError and WindowsError where available
            print("Error: {} could not be found.".format(fname))

    def new_liquid(self, fname, new_item, new_amount, new_expiration):
        """
        Adds a new liquid object.
        Changes the CSV file to reflect the new item.

        Param: fname, string for csv file name
        Param: new_item, string name of new entry
        Param: new_amount, int quantity
        Param: new_expiration, string representing the date of expiration of the new entry
        """
        # make sure the new_amount is a positive integer
        if str(new_amount).isdigit():
            # validate expiration with regular expression to make sure it is the format "##/##/##"
            if re.match(r"\d\d/\d\d/\d\d", new_expiration):
                with open(fname, "a+", newline="") as f:
                    self._liquids.append(ing.Liquids(new_item, new_amount, new_expiration))
                    f.write(new_item + "," + str(new_amount) + "," + new_expiration + "\n")
            else:
                print("Error: Please enter expiration date in the format \"DD/MM/YY\"")
        else:
            print("Error: Please make sure to enter a positive integer for quantity")

    def upload_meat_csv(self, fname):
        """
        Takes in a meat csv file and creates a Meat object for each entry.

        Param: fname, the string of the cvs file name.
        """
        try:
            with open(fname, "r", newline="") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if reader.line_num == 1:
                        # skip first line
                        continue

                    # create a drygoods object for every entry
                    type = row["Ingredient"]
                    ounces = row["Amount"]
                    date = row["Purchase Date"]
                    self._meat.append(ing.Meats(type, ounces, date))
                    # keep track of how many ingredients we have
                    self._ingredients_count += 1
        except EnvironmentError:  # parent of IOError, OSError and WindowsError where available
            print("Error: {} could not be found.".format(fname))

    def new_meat(self, fname, new_item, new_amount, new_purchase_date):
        """
        Adds a new meat object.
        Changes the CSV file to reflect the new item.

        Param: fname, string for csv file name
        Param: new_item, string name of new entry
        Param: new_amount, int quantity
        Param: new_purchase_date, string representing the date of purchase of the new entry
        """
        # make sure the new_amount is a positive integer
        if str(new_amount).isdigit():
            # validate expiration with regular expression to make sure it is the format "##/##/##"
            if re.match(r"\d\d/\d\d/\d\d", new_purchase_date):
                with open(fname, "a+", newline="") as f:
                    this_meat = ing.Meats(new_item, new_amount, new_purchase_date)
                    self._meat.append(this_meat)
                    f.write(new_item + "," + str(new_amount) + "," + new_purchase_date +
                            "," + this_meat.get_expiration() + "\n")
            else:
                print("Error: Please enter purchase date in the format \"DD/MM/YY\"")
        else:
            print("Error: Please make sure to enter a positive integer for quantity")

    def upload_produce_csv(self, fname):
        """
        Takes in a produce csv file and creates a Produce object for each entry.

        Param: fname, the string of the cvs file name.
        """
        try:
            with open(fname, "r", newline="") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if reader.line_num == 1:
                        # skip first line
                        continue

                    # create a drygoods object for every entry
                    name = row["Ingredient"]
                    grams = row["Amount"]
                    date = row["Purchase Date"]
                    self._produce.append(ing.Produce(name, grams, date))
                    # keep track of how many ingredients we have
                    self._ingredients_count += 1
        except EnvironmentError:  # parent of IOError, OSError and WindowsError where available
            print("Error: {} could not be found.".format(fname))

    def new_produce(self, fname, new_item, new_amount, new_purchase_date):
        """
        Adds a new produce object.
        Changes the CSV file to reflect the new item.

        Param: fname, string for csv file name
        Param: new_item, string name of new entry
        Param: new_amount, int quantity
        Param: new_purchase_date, string representing the date of purchase of the new entry
        """
        # make sure the new_amount is a positive integer
        if str(new_amount).isdigit():
            # validate expiration with regular expression to make sure it is the format "##/##/##"
            if re.match(r"\d\d/\d\d/\d\d", new_purchase_date):
                with open(fname, "a+", newline="") as f:
                    this_produce = ing.Produce(new_item, new_amount, new_purchase_date)
                    self._produce.append(this_produce)
                    f.write(new_item + "," + str(new_amount) + "," + new_purchase_date +
                            "," + this_produce.get_expiration() + "\n")
            else:
                print("Error: Please enter purchase date in the format \"DD/MM/YY\"")
        else:
            print("Error: Please make sure to enter a positive integer for quantity")

    def clean_kitchen(self, fname_liquids, fname_meats, fname_produce, date):
        """
        Deletes expired records.

        Param: fname_liquids, string for liquid csv file name
        Param: fname_meats, string for meats csv file name
        Param: fname_produce, string for produce csv file name
        """
        # validate date is in correct format "##/##/##"
        if re.match(r"\d\d/\d\d/\d\d", date):
            # make list of indicies to delete
            i = 0
            liq_list = []

            for each in self._liquids:
                if self._is_old(date, each.get_expiration()):
                    liq_list.append(i)
                i += 1

            i = 0
            meat_list = []

            for each in self._meat:
                if self._is_old(date, each.get_expiration()):
                    meat_list.append(i)
                i += 1

            i = 0
            produce_list = []

            for each in self._produce:
                if self._is_old(date, each.get_expiration()):
                    produce_list.append(i)
                i += 1

            # delete objects in lists
            for each in reversed(liq_list):
                self._liquids.pop(each)

            for each in reversed(meat_list):
                self._meat.pop(each)

            for each in reversed(produce_list):
                self._produce.pop(each)

            # rewrite CSV files to reflect changes
            self.rewrite_liquids_csv(fname_liquids, "Ingredient,Amount,Expiration Date\n")
            self.rewrite_meats_csv(fname_meats, "Ingredient,Amount,Purchase Date,Expiration Date\n")
            self.rewrite_produce_csv(fname_produce, "Ingredient,Amount,Purchase Date,Expiration Date\n")
        else:
            print("Error: Please enter today's date in the format \"DD/MM/YY\"")

    def _is_old(self, date, expir_date):
        """
        Helper Functon for clean_kitchen.
        
        Param: date, string representing todays date in the format "DD/MM/YY"
        Param: expir_date, string representing an existing item's expiration date

        Returns: bool, true if the item is old, false if the item is not past expiration
        """

        if int(expir_date[6:]) > int(date[6:]):
            return False
        elif int(expir_date[6:]) == int(date[6:]):
            if int(expir_date[3:5]) > int(date[3:5]):
                return False
            elif int(expir_date[3:5]) == int(date[3:5]):
                return int(expir_date[0:2]) < int(date[0:2])
            else:
                return True
        else:
            return True

    def rewrite_drygoods_csv(self, fname, headers):
        """
        Creates a new drygoods CSV file or overwrites an old one.

        Param: fname, string representing csv file name to write to
        Param: headers, the headers for the CSV file
        """
        with open(fname, 'w', newline='') as f:
            writer = csv.writer(f)
            f.write(headers)

            for each in self._drygoods:
                writer.writerow([each.get_name(), str(each.get_amount())])

    def rewrite_liquids_csv(self, fname, headers):
        """
        Creates a new liquids CSV file or overwrites an old one.

        Param: fname, string representing csv file name to write to
        Param: headers, the headers for the CSV file
        """
        with open(fname, 'w', newline='') as f:
            writer = csv.writer(f)
            f.write(headers)

            for each in self._liquids:
                writer.writerow([each.get_name(), str(each.get_amount()), each.get_expiration()])

    def rewrite_meats_csv(self, fname, headers):
        """
        Creates a new meats CSV file or overwrites an old one.

        Param: fname, string representing csv file name to write to
        Param: headers, the headers for the CSV file
        """
        with open(fname, 'w', newline='') as f:
            writer = csv.writer(f)
            f.write(headers)

            for each in self._meat:
                writer.writerow([each.get_name(), str(each.get_amount()), each.get_purchase(), each.get_expiration()])

    def rewrite_produce_csv(self, fname, headers):
        """
        Creates a new produce CSV file or overwrites an old one.

        Param: fname, string representing csv file name to write to
        Param: headers, the headers for the CSV file
        """
        with open(fname, 'w', newline='') as f:
            writer = csv.writer(f)
            f.write(headers)

            for each in self._produce:
                writer.writerow([each.get_name(), str(each.get_amount()), each.get_purchase(), each.get_expiration()])

    def print_all_ingredients(self):
        """
        prints the number of ingredients currently on record followed by all ingredient objects.
        """
        print("There are {} ingredients".format(str(self._ingredients_count)))
        print("These are the ingredients currently in stock: ")
        self.print_drygoods()
        self.print_liquids()
        self.print_meat()
        self.print_produce()

    def print_drygoods(self):
        """
        prints all drygood objects
        """
        for each in self._drygoods:
            print(each)

    def print_liquids(self):
        """
        prints all liquid objects
        """
        for each in self._liquids:
            print(each)

    def print_meat(self):
        """
        prints all meat objects
        """
        for each in self._meat:
            print(each)

    def print_produce(self):
        """
        prints all produce objects
        """
        for each in self._produce:
            print(each)

    def open_excel(self, fname):
        """
        opens a CSV file in excel if the os is windows, and in open office if Linux.
        """
        if os.name == "nt":
            res = sub.run(['cmd', '/c', 'start', fname])
        elif os.name == "posix":
            res = sub.run(["openoffice", fname])

# def main():
#     my_manager = InventoryManager()
#     my_manager.upload_drygood_csv("drygoods.csv")
#     print(my_manager.get_ingredients_count())
#     ########## liquids test
#     my_manager.upload_liquid_csv("liquids.csv")
#     print(my_manager.get_liquids_count())
#     ######## meat test
#     my_manager.upload_meat_csv("meats.csv")
#     print(my_manager.get_meats_count())
#     ######## produce test
#     my_manager.upload_produce_csv("produce.csv")
#     #print(my_manager.get_produce_count())
#     #print(my_manager.get_ingredients_count())
#     ######## see all test:
#     #my_manager.print_all_ingredients()
#     ######## test new drygood
#     #my_manager.new_drygood("drygoods.csv", "Potato Starch", 500)
#     #my_manager.print_drygoods()
#     ######## test add_more_drygood
#     #my_manager.add_more_drygood("drygoods.csv", "flour", 50)
#     ######## test new_liquid
#     #my_manager.new_liquid("liquids.csv", "Orange juice", 50, "12/04/12")
#     #my_manager.new_meat("meats.csv", "Pork", 50, "11/03/18")
#     #my_manager.new_produce("produce.csv", "Mango", 80, "11/03/18")
#     #my_manager.clean_kitchen("liquids.csv", "meats.csv", "produce.csv", "15/03/18")
#     #my_manager.print_all_ingredients()
#     ####### test open_excel
#     my_manager.open_excel("meats.csv")

# if __name__ == "__main__":
#     main()
