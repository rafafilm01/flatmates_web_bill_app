# a class is needed for each HTML page we will be displaying with Flask
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
#import internal libraries



app = Flask (__name__)

class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView): 
    
    def get(self):
        bill_form = BillForm()
        return render_template ('bill_form_page.html', bill_form=bill_form)

class ResultsPage(MethodView):
    
    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data
        print (f"the bill amount is {amount} and it is for {period}")
        return (amount, period)

#bill form is not going to be a dedicated page but rather a form on the page
#the BillFrom class will be called in the get method that is running the BillFormPage 
# and also needs to be refferred to in HTML code for that page 
class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")

    name_1 = StringField("Name: ")
    days_in_house_1 = StringField("Days in the house: ")

    name_2 = StringField("Name: ")
    days_in_house_2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")
    



#URL rules to root the classe to the html addresses (/ - home etc.), form there sepcific methods are actioned depending on the typr of request GET, POST etc.)
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)