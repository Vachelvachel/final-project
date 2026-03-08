"""
This module explores the research question 1 and 3:
Which WHO region has the most significant change in the level
of PM2.5 concentrations?
Which region has the highest pollution level measured by
AQI(Air Quality Index)?
"""
import pandas as pd
import plotly.express as px
import eda


def load_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning the dataset and extract the columns we focused on.
    """
    col_focus = ["WHO Region", "WHO Country Name", "Measurement Year",
                 "PM2.5 (μg/m3)", "PM10 (μg/m3)", "NO2 (μg/m3)"]
    df_focus = eda.clean(df, col_focus)
    return df_focus


def pm25_average(df: pd.DataFrame) -> None:
    """
    Visualize the trend of average PM2.5 concentration for different regions
    by year.
    """
    df_grouped = df.groupby(['WHO Region', 'Measurement Year']
                            )['PM2.5 (μg/m3)'].mean().reset_index()
    fig = px.line(df_grouped, x="Measurement Year", y="PM2.5 (μg/m3)",
                  color="WHO Region",
                  title="Average PM2.5 Concentration by WHO Region",
                  labels={'Measurement Year': 'Year',
                          'PM2.5 (μg/m3)': 'PM2.5 Concentration (μg/m3)'})
    fig.show()


def pm25_increase(df: pd.DataFrame) -> str:
    """
    Get the region has the most significant increase in the level
    of PM2.5 concentrations
    """
    regions = df['WHO Region'].unique()
    increase = {}
    for region in regions:
        region_df = df[df['WHO Region'] == region]
        pm25_2010 = region_df[region_df['Measurement Year'] == 2010][
                    'PM2.5 (μg/m3)'].mean()
        pm25_2021 = region_df[region_df['Measurement Year'] == 2021][
                    'PM2.5 (μg/m3)'].mean()
        diff = pm25_2021 - pm25_2010
        increase[region] = diff
    max_diff = increase[regions[0]]
    result = regions[0]
    for region in increase:
        if increase[region] > max_diff:
            max_diff = increase[region]
            result = region
    return result


def highest_aqi(df: pd.DataFrame) -> str:
    """
    Get the region has the highest average pollution level based on AQI.
    """
    df = df.copy()
    df['overall_aqi'] = df[['PM2.5 (μg/m3)', 'PM10 (μg/m3)',
                            'NO2 (μg/m3)']].max(axis=1)
    avg_aqi_by_region = (df.groupby('WHO Region')['overall_aqi']
                         .mean())
    avg_aqi_df = avg_aqi_by_region.reset_index()
    fig = px.bar(avg_aqi_df, x="WHO Region", y="overall_aqi",
                 color="WHO Region",
                 title="Average AQI by WHO Region",
                 labels={'overall_aqi': "Average AQI"})
    fig.show()
    return avg_aqi_by_region.idxmax()


def main():
    df = pd.read_csv("pollution.csv", na_values=["---"])
    df = load_data(df)
    pm25_average(df)
    print('The region with the most significant increase in the level of'
          'PM2.5 concentrations is ' + pm25_increase(df))
    print('The region with the highest pollution level based on AQI is: ' +
          highest_aqi(df))


if __name__ == '__main__':
    main()
