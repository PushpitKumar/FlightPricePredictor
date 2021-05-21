from flask import Flask, render_template, request
from flask_cors import cross_origin
import jsonify
import requests
import sklearn
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("flight.pkl","rb"))

@app.route("/",methods=['GET'])
@cross_origin()
def Home():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':

        #Airline
        Airlines = request.form['Airline']
        if Airlines=='Jet Airways':
            Jet_Airways = 1
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='Indigo':
            Jet_Airways = 0
            Indigo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='Air India':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='Multiple carriers':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='SpiceJet':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='Vistara':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='GoAir':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='Multiple carriers Premium economy':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='Jet Airways Business':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0
        elif Airlines=='Vistara Premium economy':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
        elif Airlines=='Trujet':
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
        else:
            #Air_Asia = 1
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        #Departure
        Dep_Date = request.form['Dep_Time']
        Dep_Day = int(pd.to_datetime(Dep_Date,format='%Y-%m-%dT%H:%M').day)
        Dep_Month = int(pd.to_datetime(Dep_Date,format='%Y-%m-%dT%H:%M').month)
        Dep_Hour = int(pd.to_datetime(Dep_Date,format='%Y-%m-%dT%H:%M').hour)
        Dep_Minute = int(pd.to_datetime(Dep_Date,format='%Y-%m-%dT%H:%M').minute)

        #Arrival
        Arrival_Date = request.form['Arrival_Time']
        Arrival_Day = int(pd.to_datetime(Arrival_Date,format='%Y-%m-%dT%H:%M').day)
        Arrival_Month = int(pd.to_datetime(Arrival_Date,format='%Y-%m-%dT%H:%M').month)
        Arrival_Hour = int(pd.to_datetime(Arrival_Date,format='%Y-%m-%dT%H:%M').hour)
        Arrival_Minute = int(pd.to_datetime(Arrival_Date,format='%Y-%m-%dT%H:%M').minute)

        #Duration
        Duration_Hour = abs(Arrival_Hour-Dep_Hour)
        Duration_Minute = abs(Arrival_Minute-Dep_Minute)

        #Total Stops
        Stops = int(request.form['Total_Stops'])

        prediction = model.predict([[
        Stops,
        Dep_Day,
        Dep_Month,
        Dep_Hour,
        Dep_Minute,
        Arrival_Hour,
        Arrival_Minute,
        Duration_Hour,
        Duration_Minute,
        Jet_Airways,
        Indigo,
        Air_India,
        Multiple_carriers,
        SpiceJet,
        Vistara,
        GoAir,
        Multiple_carriers_Premium_economy,
        Jet_Airways_Business,
        Vistara_Premium_economy,
        Trujet
        ]])

        result = round(prediction[0],2)

        return render_template('index.html',prediction_text="Flight Fare: Rs {}".format(result))

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
