import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import eda


def load_data(df: pd.DataFrame) -> pd.DataFrame:
    col_focus = ["WHO Region", "WHO Country Name", "Measurement Year",
                 "PM2.5 (μg/m3)", "PM10 (μg/m3)", "NO2 (μg/m3)"]
    df_focus = eda.clean(df, col_focus)
    return df_focus


def pm25_average(df: pd.DataFrame) -> None:
    df_grouped = df.groupby(['WHO Region', 'Measurement Year']
                            )['PM2.5 (μg/m3)'].mean().reset_index()
    sns.set_theme()
    sns.lineplot(data=df_grouped, x="Measurement Year", y="PM2.5 (μg/m3)",
                 hue="WHO Region")
    plt.xlabel("Year")
    plt.ylabel("PM2.5 Concentration (μg/m3)")
    plt.title("Average PM2.5 Concentration by WHO Region")
    plt.savefig('average_pm25.png', bbox_inches='tight')


def pm25_increase(df: pd.DataFrame) -> str:
    regions = df['WHO Region'].unique()
    increase = {}
    for region in regions:
        region_df = df[df['WHO Region'] == region]
        pm25_2010 = region_df[region_df['Measurement Year'] == 2010][
                    'PM2.5 (μg/m3)'].mean()
        pm25_2022 = region_df[region_df['Measurement Year'] == 2021][
                    'PM2.5 (μg/m3)'].mean()
        diff = pm25_2022 - pm25_2010
        increase[region] = diff
    max_diff = increase[regions[0]]
    result = regions[0]
    for region in increase:
        if increase[region] > max_diff:
            max_diff = increase[region]
            result = region
    return result


def main():
    df = pd.read_csv("pollution.csv", na_values=["---"])
    load_data(df)
    print('The region with the most significant increase in the level of'
          'PM2.5 concentrations is ' + pm25_increase(df))


if __name__ == '__main__':
    main()
