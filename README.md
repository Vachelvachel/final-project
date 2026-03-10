# A Global Analysis of Urban Air Pollution
Our project explores the global air pollution dataset to answer three research questions:
1. Which WHO region has the most significant change in the level of PM2.5 concentrations?
2. What will the PM2.5 concentration of the European region be in 2027?
3. Which region has the highest average pollution level measured by AQI (Air Quality Index)?

## Libraries and Environment
The project is developed in Python 3.13.11(cse 163 environment)
The project includes the following Python libraries:
pandas, plotly, scikit-learn
You can install these libraries using these commands:
```
pip install pandas
pip install plotly
pip install scikit-learn
```

## Description of files
### result.py:
This module explores our research question 1 and question 3 and also visualize the average PM2.5 concentration for different regions and AQI of different regions.
prediction.py:
This module explores our research question 2 by using a linear regression model to predict PM2.5 levels for European region in 2027 and visualize the result.
### eda.py:
This module explores the global pollution dataset, including functions for cleaning data and getting statistical result of categorical and numerical variables.
### question_test.py:
Testing functions in ```result.py```
### test.py:
Testing functions in ```eda.py```
### pollution.csv:
The dataset used in the project
### test.csv:
The small dataset used for ```test.py```

## Instructions to run the project
Firstly, open the terminal and navigate to the same directory of project files. All files should be kept in the same directory when running the project.
To get the statistics summary of the dataset, you can run ```python eda.py``` to see the percentage of missing value in the dataset and get the statistical result of categorical and numerical variables in the console.

To test functions in ```eda.py```, you can run ```python test.py``` If you see "All test passed!" in the console, it means all of functions in eda.py work well.

To explore question 1 and 3, you can run commands ```python result.py``` It would generate the plots showing the plots of average PM2.5 concentration for different regions and AQI of different regions.It also contains the region with most significant PM2.5 change and the region with the highest AQI in the console.

To test functions in ```result.py```, you can run ```python question_test.py``` If you see "All test passed!" in the console, it means all of functions in ```question_test.py``` work well.

To explore question 2, you can run commands ```python prediction.py``` Then you can see the predicted PM2.5 concentration in 2027 for European region in the console.

## Notes:
You may see the output of ```prediction.py``` and ```question_test.py``` contains the missing value percentage and number of rows after dropping missing values. This is normal behaviour, because we called function ```clean()``` in ```eda.py``` in data processing up.
