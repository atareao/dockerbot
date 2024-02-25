#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests
"""

import os
import pytest
from dotenv import load_dotenv
from src import log
from src.telegram import Telegram

pytest_plugins = ("pytest_asyncio",)

load_dotenv()


class TestTelegram:
    def setup_class(self):
        url = os.getenv("TELEGRAM_URL")
        token = os.getenv("TELEGRAM_TOKEN")
        self._chat_id = int(os.getenv("TELEGRAM_CHAT_ID", "0"))
        self._thread_id = int(os.getenv("TELEGRAM_THREAD_ID", "0"))
        self._telegram = Telegram(url, token) if url and token else None

    @pytest.mark.asyncio
    async def test_telegram_get_me(self):
        """Test telegram class
        """
        if self._telegram:
            try:
                response = await self._telegram.get_me()
            except Exception as exception:
                pytest.fail(f"Error: {exception}")
        else:
            response = None
        log.debug(response)
        if not response or not isinstance(response, dict):
            pytest.fail("No info about me")

    @pytest.mark.asyncio
    async def test_telegram_send_message(self):
        """Test telegram class
        """
        message = "This is a test messages"
        if self._telegram:
            try:
                response = await self._telegram.send_message(
                    self._chat_id,
                    self._thread_id, message)
            except Exception as exception:
                pytest.fail(f"Error: {exception}")
        else:
            response = None
        log.debug(response)
        if not response or not isinstance(response, dict):
            pytest.fail("Message not send")


    @pytest.mark.asyncio
    async def test_telegram_get_updates(self):
        """Test telegram class
        """
        if self._telegram:
            try:
                response = await self._telegram.get_updates()
            except Exception as exception:
                pytest.fail(f"Error: {exception}")
        else:
            response = None
        log.debug(response)
        if not response or not isinstance(response, dict):
            pytest.fail("There is no updates")


    @pytest.mark.asyncio
    async def test_telegram_get_webhook_info(self):
        """Test get webhook info method of Telegram class
        """
        if self._telegram:
            try:
                response = await self._telegram.get_webhook_info()
            except Exception as exception:
                pytest.fail(f"Error: {exception}")
        else:
            response = None
        log.debug(response)
        if not response or not isinstance(response, dict):
            pytest.fail("No webhook info")
