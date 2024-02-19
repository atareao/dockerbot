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
        response = await telegram.get_me()
    else:
        response = None
    logger.debug(response)
    assert response is not None
    assert response != ""


@pytest.mark.asyncio
async def test_telegram_send_message():
    """Test telegram class
    """
    message = "This is a test messages"
    if telegram:
        response = await telegram.send_message(chat_id, thread_id, message)
    else:
        response = None
    logger.debug(response)
    assert response is not None
    assert response != ""


@pytest.mark.asyncio
async def test_telegram_get_updates():
    """Test telegram class
    """
    if telegram:
        response = await telegram.get_updates()
    else:
        response = None
    logger.debug(response)
    assert response is not None
    assert response != ""
