#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2024 Lorenzo Carbonell <a.k.a. atareao>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""A module for telegram
"""

import logging
from httpx import AsyncClient

logger = logging.getLogger(__name__)


class TelegramException(Exception):
    """Telegram exception

    Args:
        Exception (_type_): exception
    """


class Telegram:
    """A class to work with Telegram
    """

    def __init__(self, url: str, token: str):
        """Init Telegram class

        Args:
            url (str): base url for telegram
            token (str): token for bot
        """
        logger.info("__info__")
        self._url = f"https://{url}/bot{token}"
        self._headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    async def send_message(self, chat_id: int, thread_id: int, message: str):
        """Send message to Telegram

        Args:
            chat_id (int): id for chat
            thread_id (int): id for thread
            message (str): message to send

        Returns:
            _type_: _description_
        """
        logger.info("send_message")
        url = f"{self._url}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "message_thread_id": thread_id,
            "parse_mode": "markdown",
            "text": message
        }
        logger.debug(payload)
        async with AsyncClient() as client:
            response = await client.post(
                url, headers=self._headers, json=payload
            )
            logger.debug(response)
            if response.status_code == 200:
                return response.json()
