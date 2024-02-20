#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests
"""

import os
import logging
import pytest
from dotenv import load_dotenv
from src.telegram import Telegram

logger = logging.getLogger(__name__)
pytest_plugins = ("pytest_asyncio",)

load_dotenv()
url = os.getenv("TELEGRAM_URL")
token = os.getenv("TELEGRAM_TOKEN")
chat_id = int(os.getenv("TELEGRAM_CHAT_ID", "0"))
thread_id = int(os.getenv("TELEGRAM_THREAD_ID", "0"))
telegram = Telegram(url, token) if url and token else None


@pytest.mark.asyncio
async def test_telegram_get_me():
    """Test telegram class
    """
    if telegram:
        try:
            response = await telegram.get_me()
        except Exception as exception:
            pytest.fail(f"Error: {exception}")
    else:
        response = None
    logger.debug(response)
    if not response or not isinstance(response, dict):
        pytest.fail("No info about me")


@pytest.mark.asyncio
async def test_telegram_send_message():
    """Test telegram class
    """
    message = "This is a test messages"
    if telegram:
        try:
            response = await telegram.send_message(chat_id, thread_id, message)
        except Exception as exception:
            pytest.fail(f"Error: {exception}")
    else:
        response = None
    logger.debug(response)
    if not response or not isinstance(response, dict):
        pytest.fail("Message not send")


@pytest.mark.asyncio
async def test_telegram_get_updates():
    """Test telegram class
    """
    if telegram:
        try:
            response = await telegram.get_updates()
        except Exception as exception:
            pytest.fail(f"Error: {exception}")
    else:
        response = None
    logger.debug(response)
    if not response or not isinstance(response, dict):
        pytest.fail("There is no updates")


@pytest.mark.asyncio
async def test_telegram_get_webhook_info():
    """Test get webhook info method of Telegram class
    """
    if telegram:
        try:
            response = await telegram.get_webhook_info()
        except Exception as exception:
            pytest.fail(f"Error: {exception}")
    else:
        response = None
    logger.debug(response)
    if not response or not isinstance(response, dict):
        pytest.fail("No webhook info")
