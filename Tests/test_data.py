import pytest

from bmi_calculator_fun import calculateBmi


def test_data():
    dataFile = 'Data/input.json'
    data, overweightCount = calculateBmi(dataFile)

    assert overweightCount == 1