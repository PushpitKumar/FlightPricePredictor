# FlightPricePredictor

## Table of Contents
* Overview/Problem Statement
* App Implementation
* Working Environment/Libraries
* File Structure 
* Deployment
* Drawbacks and Future Scope
* Credits

### 1. Overview/Problem Statement
In this ML model, we try to predict the flight fare using regression techniques such as LinearRegression RandomForest, XgBoost, etc. RandomForest gave the best results with minimum error and highest accuracy. The app was developed using flask framework in python and finally deployed on Heroku platform.

### 2. App Implementation  
Link: [FlightFarePrediction](https://flightpricepredictor99.herokuapp.com/)  
The app asks for user to enter their preffered airline, Date of Journey which includes (Departure date and time, Arrival date and time), place they are travellng from, destination and number of stoppages. Based on these input flight fare is predicted.  

![1](https://user-images.githubusercontent.com/83957848/119222295-39977f00-bb11-11eb-88de-5d48ef77a728.JPG)  
![2](https://user-images.githubusercontent.com/83957848/119222303-43b97d80-bb11-11eb-87cf-aa0ba72b88c5.JPG)


### 3. Working Environment/Libraries
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
The web app was deployed on Heroku platform after connecting to this github repository. You need to have an account in order to deploy the model.  
![3](https://user-images.githubusercontent.com/83957848/119222443-06092480-bb12-11eb-8102-086761ded15b.JPG)



### 6. Drawbacks and Future Scope
The data used for training and testing purpose of model was of 2019 only. The model doesn't take into consideration, seasonal effects on flight fare, also some of the flights have been out of business in the current scenario such as Jet Airways. The dataset only contained travel details from 5-6 different cities of India. The app's front end has room for improvement using CSS or other styling techniques. Different algorithms can be used for more accurate results.

### 7. Credits
I would like to thank [Krish Naik](https://github.com/krishnaik06) for hosting this problem statement on his youtube channel and [Amar Mandal](https://github.com/Mandal-21) whose work was taken as inspiration for succesfull completion of this project.  


