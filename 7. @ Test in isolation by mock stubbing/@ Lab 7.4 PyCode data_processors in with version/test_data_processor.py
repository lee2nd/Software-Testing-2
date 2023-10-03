# test_data_processor.py

import pytest
from unittest import mock
from data_processor import get_and_process_data

def test_get_and_process_data():
    # Mocking the fetch_data_from_api function with mock data [1, 2, 3]
    with mock.patch('data_processor.fetch_data_from_api', return_value=[1, 2, 3]) as mock_fetch:
        result = get_and_process_data("https://example.com/api/data")
        # Assert that the mocked function was called with the correct URL
        mock_fetch.assert_called_once_with("https://example.com/api/data")
        # Assert the result of the get_and_process_data function
        assert result == 6

def test_get_and_process_data_api_error():
    # Mocking the fetch_data_from_api function to return None (API error)
    with mock.patch('data_processor.fetch_data_from_api', return_value=None) as mock_fetch:
        result = get_and_process_data("https://example.com/api/data")
        # Assert that the mocked function was called with the correct URL
        mock_fetch.assert_called_once_with("https://example.com/api/data")
        # Assert the result of the get_and_process_data function when API call fails
        assert result is None

if __name__ == "__main__":
    pytest.main()
