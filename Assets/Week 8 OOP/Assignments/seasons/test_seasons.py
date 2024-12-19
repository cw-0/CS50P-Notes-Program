import pytest
from seasons import get_time, convert_number


def test_one_year_ago(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2023-11-22')
    time_elapsed = get_time("2023-11-22")
    result = convert_number(time_elapsed)
    expected_result = "five hundred twenty-seven thousand forty minutes have passed"
    assert result == expected_result



def test_two_years_ago(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2022-11-22')
    time_elapsed = get_time("2022-11-22")
    result = convert_number(time_elapsed)
    expected_result = "one million, fifty-two thousand, six hundred forty minutes have passed"
    assert result == expected_result



def test_invalid_date_format(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'september 25, 2003')
    with pytest.raises(SystemExit):
        get_time('september 25, 2003')

        
