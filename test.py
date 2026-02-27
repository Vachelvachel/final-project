"""
Testing functions in eda.py
"""
import pandas as pd
import eda


def test_clean(df: pd.DataFrame) -> None:
    """
    Test clean()
    """
    col_focus = ["WHO Region", "WHO Country Name", "Measurement Year",
                 "PM2.5 (μg/m3)", "PM10 (μg/m3)", "NO2 (μg/m3)"]
    # Clean dataset
    df_clean = eda.clean(df, col_focus)
    assert (len(df_clean) == 3)
    assert df_clean.isna().sum().sum() == 0


def test_stat(df: pd.DataFrame) -> None:
    """
    test stat()
    """
    # Clean the dataset firstly
    col_focus = ["WHO Region", "WHO Country Name", "Measurement Year",
                 "PM2.5 (μg/m3)", "PM10 (μg/m3)", "NO2 (μg/m3)"]
    df_clean = eda.clean(df, col_focus)

    cols = ["PM2.5 (μg/m3)", "PM10 (μg/m3)", "Measurement Year", "NO2 (μg/m3)"]
    stat = eda.stat(df_clean, cols)
    median_pm25 = stat.loc["50%", "PM2.5 (μg/m3)"]
    assert (median_pm25 == 7)
    max_pm10 = stat.loc["max", "PM10 (μg/m3)"]
    assert (max_pm10 == 15)


def test_count_region(df: pd.DataFrame) -> None:
    """
    test count_region()
    """
    # Clean the dataset firstly
    col_focus = ["WHO Region", "WHO Country Name", "Measurement Year",
                 "PM2.5 (μg/m3)", "PM10 (μg/m3)", "NO2 (μg/m3)"]
    df_clean = eda.clean(df, col_focus)

    ret = eda.count_region(df_clean)
    assert (len(ret) == 2)
    assert (ret["European Region"] == 1)


def main():
    df = pd.read_csv("test.csv")
    test_clean(df)
    test_stat(df)
    test_count_region(df)
    print("All test passed!")


if __name__ == "__main__":
    main()
