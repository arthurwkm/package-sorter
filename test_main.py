
from main import get_package_category, parse_input, validate_measurements

def test_standard_package():
    assert get_package_category(10, 10, 10, 1) == "STANDARD"

def test_special_package_volume():
    assert get_package_category(100, 100, 100, 1) == "SPECIAL"

def test_special_package_mass():
    assert get_package_category(10, 10, 10, 25) == "SPECIAL"

def test_rejected_package():
    assert get_package_category(100, 100, 100, 25) == "REJECTED"

def test_invalid_package():
    assert get_package_category(-1, 10, 10, 1) == "Incorrect input, try again"

def test_parse_input_valid():
    assert parse_input("10 20 30 40") == [10.0, 20.0, 30.0, 40.0]

def test_parse_input_invalid_format():
    assert parse_input("10 20 30") is None

def test_validate_measurements():
    assert validate_measurements(10, 20, 30, 40) is True
    assert validate_measurements(-1, 20, 30, 40) is False
