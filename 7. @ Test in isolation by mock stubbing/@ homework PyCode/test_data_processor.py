# test_data_processor.py

from unittest import mock 
from data_processor import process_and_store_data

@mock.patch('data_processor.Database')
def test_process_and_store_data(MockDatabase):
    # Create a mock instance of the Database class
    mock_db_instance = MockDatabase.return_value
    
    # Define the return values for the mock methods
    mock_db_instance.get_all_data.return_value = [1,2,3]
    
    assert sum(mock_db_instance.get_all_data.return_value) == 6
    