"""
Testing functions in result.py
"""
import pandas as pd
import result


def test_pm25_increase() -> None:
    """
    test pm25_increase()
    """
    df = pd.DataFrame({'WHO Region': ['A', 'A', 'B', 'B', 'C', 'C'],
                       'Measurement Year': [2010, 2021, 2010, 2021,
                                            2010, 2021],
                       'PM2.5 (μg/m3)': [1, 10, 2, 10, 3, 10]})
    assert result.pm25_increase(df) == 'A'


def test_highest_aqi() -> None:
    """
    test highest_aqi()
    """
    df = pd.DataFrame({'WHO Region': ['A', 'B', 'C'],
                       'PM2.5 (μg/m3)': [5, 6, 7],
                       'PM10 (μg/m3)': [4, 5, 9],
                       'NO2 (μg/m3)': [9, 10, 11]})
    assert result.highest_aqi(df) == 'C'


def main():
    test_pm25_increase()
    test_highest_aqi()
    print("All test passed!")


if __name__ == "__main__":
    main()
