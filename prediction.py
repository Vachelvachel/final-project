"""
The module explore the research question 2:
What will the PM2.5 concentration of the European region be in 2027?
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import eda


def load_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning the dataset and extract the columns we focused on.
    """
    col_focus = ["WHO Region", "WHO Country Name", "Measurement Year",
                 "PM2.5 (μg/m3)", "PM10 (μg/m3)", "NO2 (μg/m3)"]
    df_focus = eda.clean(df, col_focus)
    return df_focus


def prediction(df: pd.DataFrame) -> None:
    """
    Fit a linear regression model to predict PM2.5 levels for
    Europe in 2027 and visualize the result.
    """
    europe = df[df['WHO Region'] == "European Region"]
    europe = europe[europe['Measurement Year'].notna() &
                    europe['PM2.5 (μg/m3)'].notna()]
    x = europe[['Measurement Year']]
    y = europe['PM2.5 (μg/m3)']
    # Using the data from 2010-2018 as our training data and
    # data after 2019 as the testing data.
    train = europe[europe['Measurement Year'] <= 2018]
    test = europe[europe['Measurement Year'] >= 2019]
    x_train = train[['Measurement Year']]
    y_train = train['PM2.5 (μg/m3)']
    x_test = test[['Measurement Year']]
    y_test = test['PM2.5 (μg/m3)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    model = LinearRegression()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    mse = mean_squared_error(y_test, predictions)
    predict_2027 = model.predict(pd.DataFrame({'Measurement Year': [2027]}))
    print('Predicted PM2.5 concentration in 2027 for Europe region is: ' +
          str(predict_2027) + 'mean squared error: ' + str(mse))


def main():
    df = pd.read_csv("pollution.csv", na_values=["---"])
    df = load_data(df)
    prediction(df)


if __name__ == '__main__':
    main()
