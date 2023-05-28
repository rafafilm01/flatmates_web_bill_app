
import webbrowser
from fpdf import FPDF
import os #needed to access the generated pfd report that is nested in a outputFile

class PdfReport : 
    """
    object that holds data on the roomate and the bill and passes it on into PDF version 
    """
    def __init__  (self, filename):
        self.filename = filename

    
    def generate(self, flatmate1, flatmate2, bill ):

        #varialbles used in PDF cell values  #FOR CLEANER CODE
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2 ))  
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2 ))  
        #create a PDF instance from FPDF class 
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #adding extra image on top od the doc
        pdf.image("./files/house.png", w=30, h=30)

        #populate the PDF with static and dynamic content 
        pdf.set_font(family="Times", size= 22, style="B")
        pdf.cell (w=0, h=80, txt="Roomates bill" , border=0 , align='C', ln=1)
        pdf.set_font(family="Times", size= 18, style="B")
        pdf.cell (w=100, h=40, txt="Period: ", border=0)
        pdf.cell (w=150, h=40, txt= bill.period , border=0, ln=1)
        #dynamic data name and due_amount
        pdf.set_font(family="Times", size= 16)
        pdf.cell (w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell (w=100, h=40, txt=flatmate1_pay, border=0, ln=1)
        pdf.cell (w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell (w=100, h=40, txt=flatmate2_pay , border=0, ln=1)

        #save and output PDF into a file
        #change the working directory 
        os.chdir("outputFiles")
        
        pdf.output(self.filename)

        #autmatically open the PDF in a default web browser  once it has been created 
        webbrowser.open(self.filename)