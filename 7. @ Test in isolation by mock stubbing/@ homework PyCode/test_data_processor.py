# test_data_processor.py

import pytest
from unittest import mock 
from data_processor import process_and_store_data

# 20-24 行是額外加的

@mock.patch('data_processor.Database')
def test_process_and_store_data(MockDatabase):
    # Create a mock instance of the Database class
    mock_db_instance = MockDatabase.return_value
    
    # Define the return values for the mock methods
    mock_db_instance.get_all_data.return_value = [1,2,3]
    
    # Test the process_and_store_data function
    result = process_and_store_data(4)

    # Assert that the Database. insert_data method was called with the correct value
    mock_db_instance.insert_data.assert_called_once_with(4)

    # Assert that the Database.get_all_data method was called
    mock_db_instance.get_all_data.assert_called_once()

    # Assert the result of the process_and_store_data function
    assert result == 6

if __name__ == "__main__":
    pytest.main()
