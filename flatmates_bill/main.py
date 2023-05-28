from reports import PdfReport
from flat import Bill, Flatmate




        


#### setting up objects 

amount = int(input("Please enter the bill amount : "))
period = input("please provide the period that the bill is due for : " )
print (amount)
the_bill = Bill(amount, period)

name1 = input("what is the nname of the first roomate ? : ")
name1_period = int(input(f"How many days has {name1} been in the house over {period}? : "))
name2 = input("what is the nname of the first roomate ? : ")
name2_period = int(input(f"How many days has {name2} been in the house over {period}? : "))
flatmate1 = Flatmate(name1, name1_period)
flatmate2 = Flatmate(name2, name2_period)

# #SANITY CHECK
print (flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print (f' first flatmate {flatmate1.name} paid his share of the bill which was  {flatmate1.pays(the_bill, flatmate2)}')

#generate the PDF
pdf_report = PdfReport(f'{the_bill.period}.pdf')
#generate functions operates on the objects that were created from other classes in order to complete the PDF
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)    