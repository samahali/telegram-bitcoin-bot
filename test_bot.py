"""
Unit tests for the main module functions.

This module contains tests for the `get_price` and `send_updates` functions
defined in the `main` module. It uses the `pytest` framework and mocks
external API calls to ensure that the tests are isolated and do not depend
on external services.

Fixtures:
    mock_constants: A pytest fixture that patches the constants used in
    the application with mock values for testing.

Test Cases:
    test_get_price_success: Tests the `get_price` function for a successful
    API response, asserting that the returned price matches the expected value.

    test_get_price_failure: Tests the `get_price` function for a failed
    API response, asserting that the returned price is None.

    test_send_updates_success: Tests the `send_updates` function for a
    successful message sending, asserting that the request was made once.

    test_send_updates_failure: Tests the `send_updates` function for a
    failed message sending, asserting that the request was made once.
"""


from decimal import Decimal
from unittest.mock import patch

import pytest
import requests

from .main import get_price, send_updates


class MockConstants(object):
    """Mock constants for testing"""
    API_KEY = "mock_api_key"
    TELEGRAM_BOT_TOKEN = "mock_bot_token"
    TELEGRAM_CHAT_ID = "mock_chat_id"
    LIMIT = 59000
    TIME_INTERVAL = 5 * 60

REQ_GET = "requests.get"


@pytest.fixture(autouse=True)
def mock_constants(monkeypatch):
    """Patch the constants module"""
    monkeypatch.setattr("constants.API_KEY", MockConstants.API_KEY)
    monkeypatch.setattr("constants.TELEGRAM_BOT_TOKEN", MockConstants.TELEGRAM_BOT_TOKEN)
    monkeypatch.setattr("constants.TELEGRAM_CHAT_ID", MockConstants.TELEGRAM_CHAT_ID)

def test_get_price_success():
    """Test the get_price function for successful API response."""
    with patch(REQ_GET) as mock_get:
        # Mock the response data
        mock_get.return_value.json.return_value = {
            "data": [{
                "quote": {
                    "USD": {
                        "price": Decimal("60000")
                    }
                }
            }]
        }
        price = get_price()
        assert price == Decimal("60000")
        mock_get.assert_called_once()

def test_get_price_failure():
    """Test the get_price function for failed API response."""
    with patch(REQ_GET) as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("API request failed")
        price = get_price()
        assert price is None
        mock_get.assert_called_once()

def test_send_updates_success():
    """Test the send_updates function for successful message sending."""
    with patch(REQ_GET) as mock_get:
        mock_get.return_value.status_code = 200
        send_updates("Test message")
        mock_get.assert_called_once()

def test_send_updates_failure():
    """Test the send_updates function for failed message sending."""
    with patch(REQ_GET) as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("API request failed")
        send_updates("Test message")
        mock_get.assert_called_once()
