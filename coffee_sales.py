#coffee.py - create a dataset for coffee sales
import csv
import random

def create_csv():
    headers=["Coffee","Quantity","Customer"]
    students=["Mauraine","Iguaine","Elaine","Avienda"]
    coffees=["Espresso","Caffe Latte","Caffe Mocha","Rasberry Mocha","Hot Chocolate"]
    
    with open("coffee_sales.csv","w", newline='') as f:
    # write a row of info to the csv, create a writer object
        writer=csv.writer(f)  
        # pass it the header and iterate through the records
        writer.writerow(headers)
        for i in range(10):
            coffee=random.choice(coffees)
            num=random.randint(1,5)
            student=random.choice(students)  
            writer.writerow([coffee, num, student])
def compute_sales(fname):
    with open(fname,'r',newline='') as f:
        reader=csv.DictReader(f)
        headers=reader.fieldnames
        #print('headers = ',headers)
        total=0
        for row in reader:
            #print('row = ',row)
            total += int(row['Quantity'])
        return total

def update_sales(fname, customer_name):
    # read in the csv data
    with open(fname,'r',newline='') as f:
        reader=csv.DictReader(f)
        data=list(reader) 
        headers=reader.fieldnames
    with open(fname,'w',newline='') as f:
        writer=csv.DictWriter(f,headers)
        writer.writeheader()
        for row in data:
            if row["Customer"]==customer_name:
                row["Quantity"]=str(int(row["Quantity"]) + 3)
            writer.writerow(row)



def generate_inventory_report(fname):
    # create a ditionary that maps the coffee
    # to the number of coffees sold for that coffee.
    # create the reader and empty dictionary
    coffees={}
    with open(fname,'r',newline='') as f:
        reader=csv.DictReader(f) # pass it f as the file

        for row in reader: # need to update, need a key?
            name=row["Coffee"]
            num_sold=int(row["Quantity"]) # pass it to an int
            num_sold+=coffees.get(name,0)  # another way to access the
            # value of a key
            # default value is 0 if not already exist
            coffee[name]=num_sold
    # while we are in the reader, need to
    # initialize empty dictionary


    # for each row
      # update coffee dictionary with quantity

    # print results
    for coffee, value in coffees.items():
        print("{:15s}{}".format(coffee, value))
        # string at least 15 long, else padd it on rhs to make it 15
        # so that columns will align
def main():
    filename="coffee_sales.csv"
    create_csv()
    sold=compute_sales(filename)
    print('sold=',sold)
    # print("Total Sales ${:.2f}".format(sold))
    # update_sales(filename,"Avienda")
    # compute_sales(filename)
    # generate_inventory_report(filename)


main()

