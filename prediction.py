"""
The module explore the research question 2:
What will the PM2.5 concentration of the European region be in 2027?
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import seaborn as sns
import matplotlib.pyplot as plt
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
    Fit a Decision Tree model to predict PM2.5 levels for
    Europe and visualize the result.
    """
    europe = df[df['WHO Region'] == "European Region"]
    europe = europe[europe['Measurement Year'].notna() &
                    europe['PM2.5 (μg/m3)'].notna()]
    # average = (europe.groupby('Measurement Year')['PM2.5 (μg/m3)']
    #            .mean().reset_index())
    x = europe[['Measurement Year']]
    y = europe['PM2.5 (μg/m3)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    model = DecisionTreeRegressor()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    grid = sns.relplot(x=y_test, y=predictions)
    grid.set(title="Observed PM2.5 v. Predicted PM2.5",
             xlabel='Observed PM2.5',
             ylabel='Predicted PM2.5')
    grid.ax.axline((0, 0), slope=1, color='k', ls='--')
    plt.savefig('pm25_prediction.png', bbox_inches='tight')
    predict_2027 = model.predict([[2027]])
    print('Predicted PM2.5 concentration in 2027 is: ' + str(predict_2027))


def main():
    df = pd.read_csv("pollution.csv", na_values=["---"])
    load_data(df)
    prediction(df)


if __name__ == '__main__':
    main()
