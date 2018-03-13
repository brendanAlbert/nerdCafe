import csv
import datetime



def date_diff(fname, colname1, colname2):
    """
    Computes the difference between dates in days
    :param fname: string, name of csv file
    :param colname1: string-valued column name for numeric purchase date
    :param colname2: string-valued column name for numeric expiration date
    :return: colname2 - colname1 in days
    """
    with open(fname,'r',newline='') as f:
        reader=csv.DictReader(f)
        data = list(reader)
        headers=reader.fieldnames
        ingredients={}
        for row in data:
  
            # Convert day/month/year date into iso8601 date
            startdt=row[colname1].replace('/',' ')
            startyr = '20' + startdt.split()[2]
            startmo = startdt.split()[1]
            startdy = startdt.split()[0]
            startdate = datetime.date(int(startyr), int(startmo), int(startdy))

            enddt = row[colname2].replace('/', ' ')
            endyr = '20' + enddt.split()[2]
            endmo = enddt.split()[1]
            enddy = enddt.split()[0]
            enddate=datetime.date(int(endyr), int(endmo), int(enddy))

            shelflife=enddate-startdate
            name=row["Ingredient"]
            ingredients[name]=shelflife
           

    with open("shelflife.csv",'w',newline='') as f:
        headers=["Ingredient","Shelf Life"]
        writer=csv.DictWriter(f, headers)
        writer.writeheader()
        for name, shelflife in ingredients.items():
            writer.writerow({"Ingredient":name,"Shelf Life":shelflife})


def main():
    date_diff("produce.csv","Purchase Date","Expiration Date")

main()
