from unittest.mock import patch, MagicMock

# Import the main function to be tested
from app.main1 import main


@patch('tkinter.Tk', return_value=MagicMock())
@patch('tkinter.ttk.Notebook', return_value=MagicMock())
def test_main(MockTk, MockNotebook):
    # Mock the tab classes
    mock_mac_to_phone_tab = MagicMock()
    mock_generate_log_tab = MagicMock()
    mock_user_log_app = MagicMock()
    mock_remove_duplicate_phone_numbers_tab = MagicMock()
    mock_phone_number_comparator_tab = MagicMock()
    mock_phone_number_categorizer_tab = MagicMock()

    # Patch the imports for the tab classes to use the mocks
    with patch('app.frames.MacAddressGui.tab_mac_to_phone.MacToPhoneTab', mock_mac_to_phone_tab), \
            patch('app.frames.LogOfChanges.tab_generate_log.GenerateLogTab', mock_generate_log_tab), \
            patch('app.frames.LogOfChanges.remove_user_log.UserLogApp', mock_user_log_app), \
            patch('app.frames.PhoneCheck.remove_duplicate_phone_numbers.RemoveDuplicatePhoneNumbersTab',
                  mock_remove_duplicate_phone_numbers_tab), \
            patch('app.frames.PhoneCheck.skype_phone_match.PhoneNumberComparatorTab', mock_phone_number_comparator_tab), \
            patch('app.frames.PhoneCheck.prefix_add.PhoneNumberCategorizerTab', mock_phone_number_categorizer_tab):
        # Run the main function, which should now use the mocked tab classes
        root = MockTk.return_value  # Get the mock Tk instance
        main()

        # Check that the main function calls to initialize tabs
        mock_mac_to_phone_tab.assert_called_once_with(MockNotebook.return_value)
        mock_generate_log_tab.assert_called_once_with(MockNotebook.return_value)
        mock_user_log_app.assert_called_once_with(MockNotebook.return_value)
        mock_remove_duplicate_phone_numbers_tab.assert_called_once_with(MockNotebook.return_value)
        mock_phone_number_comparator_tab.assert_called_once_with(MockNotebook.return_value)
        mock_phone_number_categorizer_tab.assert_called_once_with(MockNotebook.return_value)

        # Verify that the notebook was packed
        MockNotebook.return_value.pack.assert_called_once_with(expand=1, fill="both")
