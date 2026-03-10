"""
Testing functions in result.py
"""
import pandas as pd
import result


def test_pm25_change() -> None:
    """
    test pm25_increase()
    """
    df = pd.DataFrame({'WHO Region': ['A', 'A', 'B', 'B', 'C', 'C'],
                       'Measurement Year': [2010, 2021, 2010, 2021,
                                            2010, 2021],
                       'PM2.5 (μg/m3)': [1, 10, 2, 10, 3, 10]})
    df1 = pd.DataFrame({'WHO Region': ['A', 'A', 'A', 'B', 'B', 'B',
                                       'C', 'C', 'C'],
                       'Measurement Year': [2010, 2015, 2021, 2010, 2016, 2021,
                                            2010, 2017, 2021],
                        'PM2.5 (μg/m3)': [3, 6, 10, 1, 2, 10, 3, 8, 10]})
    assert result.pm25_change(df) == 'A'
    assert result.pm25_change(df1) == 'B'


def test_highest_aqi() -> None:
    """
    test highest_aqi()
    """
    df = pd.DataFrame({'WHO Region': ['A', 'B', 'C'],
                       'PM2.5 (μg/m3)': [5, 6, 7],
                       'PM10 (μg/m3)': [4, 5, 9],
                       'NO2 (μg/m3)': [9, 10, 11]})
    df1 = pd.DataFrame({'WHO Region': ['A', 'B', 'C', 'A', 'B', 'C'],
                        'PM2.5 (μg/m3)': [9, 10, 11, 12, 10, 5],
                        'PM10 (μg/m3)': [8, 5, 3, 2, 10, 3],
                        'NO2 (μg/m3)': [8, 6, 7, 8, 9, 7]})
    assert result.highest_aqi(df) == 'C'
    assert result.highest_aqi(df1) == 'A'


def main():
    test_pm25_change()
    test_highest_aqi()
    print("All test passed!")


if __name__ == "__main__":
    main()
