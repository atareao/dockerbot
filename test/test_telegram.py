#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests
"""

import os
import pytest
from dotenv import load_dotenv
from src.telegram import Telegram

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_telegram():
    """Test telegram class
    """
    load_dotenv()
    url = os.getenv("TELEGRAM_URL")
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    thread_id = os.getenv("TELEGRAM_THREAD_ID")
    if url and token and chat_id and thread_id:
        telegram = Telegram(url, token)
        chat_id = int(chat_id)
        thread_id = int(thread_id)
        message = "Esto es una prueba"
        response = await telegram.send_message(chat_id, thread_id, message)
    else:
        response = None
    assert response is not None
    assert response != ""
