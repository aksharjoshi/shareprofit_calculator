#tes and access data sent by POST
# using the request object from flask
from flask import Flask, render_template, request
#from flask_restful import reqparse
import json

# Initialize the Flask application
app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True

cost = 0
proceeds = 0

# This route will show a form to submit some JSON data
@app.route('/')
def index():
    return render_template('form.html')


# This route will accept a request containing JSON
# Then we'll convert that data into Python a structure
# and print it.
# Because we used a standard HTML form post to send the
# data, we need to get the JSON from request.form
# If on other hand the information was sent from an app,
# or even a python urllib2.Request we would need to use
# request.data to get the JSON string
@app.route('/request', methods=['POST'])
def jsonreq():
    # Get the JSON data sent from the form
    
    #jsondata = request.form['jsondata']
    
    ticker = request.form['ticker']
    allotment = int(request.form['allotment'])
    finalPrice = float(request.form['finalPrice'])
    sellCommision = float(request.form['sellCommision'])
    buyCommision = float(request.form['buyCommision'])
    initialPrice = float(request.form['initialPrice'])
    taxRate = request.form['taxRate']

    tax = float(taxRate.split("%")[-1])
    
    initialInvest = (allotment*initialPrice)
    finalInvest = (allotment*finalPrice)
    totalCommision = buyCommision + sellCommision

    taxTotal = (tax/100) * ((finalInvest) - (initialInvest) - totalCommision)

    netProfit = (finalInvest) - (initialInvest) - totalCommision - taxTotal
    #calcProfit(allotment, finalPrice, initialPrice, totalCommision, taxTotal)

    proceeds = allotment * finalPrice
    
    cost = (initialInvest) + totalCommision + taxTotal

    roi = (netProfit / (initialInvest + taxTotal + totalCommision)) * 100
    roiPerc = str(roi)+" "+"%"
    # Convert the JSON data into a Python structure
    #data = json.loads(jsondata)
    return render_template('request.html', roiPerc=roiPerc, netProfit=netProfit, ticker=ticker,totalCommision=totalCommision,taxRate=taxRate,taxTotal=taxTotal,proceeds=proceeds,cost=cost)


def calcProfit(allotment, finalPrice, initialPrice, totalCommision, taxTotal):
    proceeds = allotment * finalPrice
    
    cost = (allotment * initialPrice) + totalCommision + taxTotal
#     #return render_template('request.html', proceeds=proceeds, cost=cost)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000")
    )
