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
            #print("row = ", row)

            startdt=row[colname1].replace('/',' ')
            startyr = '20' + startdt.split()[2]
            startmo = startdt.split()[1]
            startdy = startdt.split()[0]
            #startdate=startyr+'-'+startmo+'-'+startdy
            startdate = datetime.date(int(startyr), int(startmo), int(startdy))
            #print("colname1=",row[colname1],"   startdate=",startdate)

            enddt = row[colname2].replace('/', ' ')
            endyr = '20' + enddt.split()[2]
            endmo = enddt.split()[1]
            enddy = enddt.split()[0]
            #enddate = endyr + '-' + endmo + '-' + enddy
            enddate=datetime.date(int(endyr), int(endmo), int(enddy))
            #print("column2=",row[colname2],"enddate=", enddate)

            shelflife=enddate-startdate
            #print(row)
            #print(row['Ingredient'])
            #print(row)
            name=row["Ingredient"]
            ingredients[name]=shelflife
            #print("name =", name, "startdate =",startdate, "enddate =", enddate,  "shelflife=" , shelflife)

    with open("shelflife.csv",'w',newline='') as f:
        headers=["Ingredient","Shelf Life"]
        writer=csv.DictWriter(f, headers)
        writer.writeheader()
        #print("ingredients = ",ingredients)
        for name, shelflife in ingredients.items():
            writer.writerow({"Ingredient":name,"Shelf Life":shelflife})


def main():
    date_diff("produce.csv","Purchase Date","Expiration Date")

main()
