# FlightPricePredictor

## Table of Contents
* Overview/Problem Statement
* App 
* Working Environment/Libraries
* File Structure 
* Deployment
* Drawbacks and Future Scope
* Credits

### 1. Overview/Problem Statement
In this ML model, we try to predict the flight fare using regression techniques such as LinearRegression RandomForest, XgBoost, etc. RandomForest gave the best results with minimum error and highest accuracy. The app was developed using flask framework in python and finally deployed on Heroku platform.

### 2. App 
Link: [FlightFarePrediction](https://flightpricepredictor99.herokuapp.com/)  
The app asks for user to enter their preffered airline, Date of Journey which includes (Departure date and time, Arrival date and time), place they are travellng from, destination and number of stoppages. Based on these input flight fare is predicted.  
![Stars](https://user-images.githubusercontent.com/83957848/119222197-bece6400-bb10-11eb-8163-e2782dc1f979.jpg)


### 3. Working Environment 
The ML model was built on Jupyter Notebook using python. The main libraries used were pandas, numpy, sklearn, matplotlib and seaborn. The ML algorithms used for model building were LinearRegression, RandomForest and XgBoost.

### 4. File Structure
```
├── static 
│   ├── css
├── templates
│   ├── index.html
├── app.py
├── flight.pkl
├── Flight_Test.xlsx
├── Flight_Train.xlsx
├── Notebook.ipynb
├── Procfile
├── requirements.txt
```

### 5. Deployment
The web app was deployed on Heroku platform after connecting to this github repository.

### 6. Drawbacks and Future Scope
The data used for training and testing purpose of model was of 2019 only. The model doesn't take into consideration, seasonal effects on flight fare, also some of the flights have been out of business in the current scenario. The app's front end has room for improvement using CSS or other styling techniques. Different algorithms can be used for more accurate results.

### 7. Credits
I would like to thank [Krish Naik](https://github.com/krishnaik06) for hosting this problem statement on his youtube channel and [Amar Mandal](https://github.com/Mandal-21) whose work was taken as inspiration for succesfull completion of this project. 

