# FlightPricePredictor

## Table of Contents
* Overview/Problem Statement
* Dataset
* File Structure
* Major Packages/Libraries Used
* Installation/Working Environment
* Building the Web App
* Model Deployment on Heroku Platform
* App Implementation
* Drawbacks and Future Scope
* Credits

### 1. Overview/Problem Statement
* Ever wondered how much a flight would cost you while making travel plans? This ML model tries to predict the flight fare using regression techniques.
* For this problem, Linear Regression, RandomForest and XgBoost algorithms were implemented, RandomForest giving the best results.

### 2. Dataset
* The dataset was taken from MachineHack and is available on Kaggle. 
* The dataset contains the following features: **Airline**, **Date of Journey**, **Source**, **Destination**, **Route**, **Departure Time**, **Arrival Time**, **Duration of Flight**, **Total Stops** and **Additional Information**.
* [Dateset Link](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh)

### 3. File Structure
```
├── static 
│   ├── flight.jpg
├── templates
│   ├── index.html
├── Flight_Test.xlsx
├── Flight_Train.xlsx
├── Notebook.ipynb
├── Procfile
├── README.md
├── app.py
├── flight.pkl
├── requirements.txt
```

### 4. Major Packages/Libraries Used
* pandas 
* numpy
* sci-kit learn
* matplotlib
* seaborn
* Flask
* gunicorn

### 5. Installation/Working Environment
Follow the instructions if you want to run the app from your local computer.
* The app is written using **Python 3.8.5**. You can download it from [here](https://www.python.org/downloads/).You can also download **Anaconda** which is a distribution of python from [here](https://www.anaconda.com/products/individual). I would recommend downloading anaconda since it is very useful as it comes with a lot of python libraries, Jupyter and Spyder IDE.
* Once you are done with the installation, you can clone this repository to your computer and install the required packages and libraries using the following line of code through the command prompt where your local environment is setup.
```
pip install -r requirements.txt
```
### 6. Building the Web App
* The web was developed using flask micro web framework which is written in python suitable for small scale projects such as this one. For more information you can check the offical flask website by clicking [here](https://flask.palletsprojects.com/en/2.0.x/)
* Basic HTML was needed for designing the webpage and to make sure it was responsive to user inputs. 

### 7. Model Deployment on Heroku Platoform
* You will have to create a account in order to deploy the model. Login to your account and go to the deploy section.
* Connect to your github repository and deploy the model manually or through Heroku CLI.

![3](https://user-images.githubusercontent.com/83957848/119222443-06092480-bb12-11eb-8102-086761ded15b.JPG)

### 8. App Implementation  
* Link: [FlightFarePrediction](https://flightpricepredictor99.herokuapp.com/)  
* The app asks for user to enter their preffered airline, Date of Journey which includes (Departure date and time, Arrival date and time), place they are travellng from, destination and number of stoppages. Based on these input flight fare is predicted.  

![1](https://user-images.githubusercontent.com/83957848/119222295-39977f00-bb11-11eb-88de-5d48ef77a728.JPG)  
![2](https://user-images.githubusercontent.com/83957848/119222303-43b97d80-bb11-11eb-87cf-aa0ba72b88c5.JPG)


### 9. Drawbacks and Future Scope
* The data used for training and testing purpose of model was of 2019 only. 
* The model doesn't take into consideration the seasonal effects on flight fare. Maybe flights in winter season have a higher fare cost in India.
* Some of the flights have been out of business in the current scenario such as Jet Airways.
* The dataset only contained travel details from 5-6 different cities of India. 
* The app's front end has room for improvement using CSS or other styling techniques. I will be updating the application once I have learnt CSS.
* More algorithms can be used for more accurate results.

### 10. Credits
I would like to thank [Krish Naik](https://github.com/krishnaik06) for hosting this problem statement on his youtube channel and [Amar Mandal](https://github.com/Mandal-21) whose work was taken as inspiration for successful completion of this project.  


