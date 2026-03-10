"""
This module explore the WHO pollution dataset, including functions
for cleaning data, getting statistical result of categorical and
numerical variables we interested in and also creating two
visualizations.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def clean(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Calculating the percentage of rows with at least one
    missing value and remove them.
    """
    df = df[columns]
    row_missing = df.isna().any(axis=1).sum()
    total = df.shape[0]
    percentage = (row_missing/total) * 100
    print("missing value percentage: ", str(percentage))
    df1 = df.dropna()
    print("Number of rows after dropping missing values:", df1.shape[0])
    return df1


def count_region(df: pd.DataFrame) -> pd.Series:
    """
    List all of WHO region and the count of each of them.
    """
    region_count = df.groupby("WHO Region").size()
    print(region_count)
    return region_count


def stat(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    The statistical results of PM2.5, PM10, NO2 concentration and year.
    """
    return (df[columns].describe())


def pm25_by_region(df: pd.DataFrame) -> None:
    """
    The bar chart shows the average pm2.5 concentration
    across each WHO region.
    """
    data = df[["WHO Region", "PM2.5 (μg/m3)"]]
    sns.set_theme()
    sns.catplot(data=data, x="WHO Region", y="PM2.5 (μg/m3)", kind="bar")
    plt.xlabel("WHO Region")
    plt.ylabel("Average PM2.5 Concentration (μg/m3)")
    plt.title("Average PM2.5 Concentration by WHO Region")
    plt.xticks(rotation=45)
    plt.savefig("bar_plot_pm25.png", bbox_inches="tight")


def pm25_by_year(df: pd.DataFrame) -> None:
    """
    The line chart shows the PM2.5 concentration change over year
    in different regions.
    """
    data = df[["Measurement Year", "WHO Region", "PM2.5 (μg/m3)"]]
    sns.set_theme()
    sns.relplot(data=data, x="Measurement Year", y="PM2.5 (μg/m3)",
                kind="line", hue="WHO Region")
    plt.xlabel("Year")
    plt.ylabel("PM2.5 Concentration (μg/m3)")
    plt.title("PM2.5 Concentration change over years by WHO Region")
    plt.savefig('line_plot_pm25.png', bbox_inches='tight')


def main():
    df = pd.read_csv("pollution.csv", na_values=["---"])
    # Remain the columns we are interested in
    col_focus = ["WHO Region", "WHO Country Name", "Measurement Year",
                 "PM2.5 (μg/m3)", "PM10 (μg/m3)", "NO2 (μg/m3)"]
    # Clean dataset
    df_focus = clean(df, col_focus)
    # summary of variables
    cols = ["PM2.5 (μg/m3)", "PM10 (μg/m3)", "Measurement Year", "NO2 (μg/m3)"]
    stat(df_focus, cols)
    count_region(df_focus)
    # Visualization
    pm25_by_region(df_focus)
    pm25_by_year(df_focus)


if __name__ == '__main__':
    main()
