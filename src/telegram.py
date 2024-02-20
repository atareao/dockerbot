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
from aiohttp import ClientSession

logger = logging.getLogger(__name__)


class TelegramException(Exception):
    """Telegram exception

    Args:
        Exception (_type_): exception
    """


class Telegram:
    """A class to work with Telegram
    """

    def __init__(self, url: str, token: str, offset: int = 0,
                 timeout: int = 300):
        """Init Telegram class

        Args:
            url (str): base url for telegram
            token (str): token for bot
            offset (int): identifier of the frist update to be returned
            timeout (int): timeout in seconds for long polling
        """
        logger.info("__info__")
        print(f"Token: {token}")
        self._url = f"https://{url}/bot{token}"
        self._offset = offset
        self._timeout = timeout
        self._headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    async def send_message(
            self, chat_id: int, thread_id: int, message: str) -> dict:
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
        print(url)
        payload = {
            "chat_id": chat_id,
            "message_thread_id": thread_id,
            "text": message,
            "parse_mode": "markdown"
        }
        return await self._post("sendMessage", payload)

    async def get_me(self) -> dict:
        """
        A simple method for testing your bot's authentication token.

        Returns
        -------
        dict
            basic information about the bot in form of a User object.
        """
        return await self._get("getMe", {})

    async def get_updates(self) -> dict:
        """
        Receive incoming updates using log polling

        Returns
        -------
        dict
            Updates
        """
        params = {
            "offset": self._offset,
            "timeout": self._timeout
        }
        return await self._get("getUpdates", params)

    async def set_webhook(self, url: str) -> dict:
        """Set webhook

        Parameters
        ----------
        url : str
            url to webhook

        Returns
        -------
        dict
            response
        """
        payload = {"url": url}
        return await self._post("setWebhook", payload)

    async def delete_webhook(self) -> dict:
        """[TODO:description]

        Returns
        -------
        bool
            True on success
        """
        return await self._post("deleteWebhook", {})

    async def get_webhook_info(self) -> dict:
        """get Webhook info

        Returns
        -------
        dict
            info about webhook
        """
        return await self._get("getWebhookInfo", {})

    async def _post(self, endpoint: str, payload: dict) -> dict:
        """
        do a post

        Returns
        -------
        dict
            response
        """
        url = f"{self._url}/{endpoint}"
        logger.info(f"Url: {url}. Payload: {payload}")
        async with ClientSession() as session:
            async with session.post(
                    url, headers=self._headers, json=payload) as response:
                logger.debug(response)
                if response.status == 200:
                    return await response.json()
                logger.debug(response.status)
                logger.debug(await response.json())
        raise Exception()

    async def _get(self, endpoint: str, params: dict) -> dict:
        """
        do a get

        Returns
        -------
        dict
            response
        """
        url = f"{self._url}/{endpoint}"
        logger.info(f"Url: {url}. Params: {params}")
        async with ClientSession() as session:
            async with session.get(
                    url, headers=self._headers, params=params) as response:
                logger.debug(response)
                if response.status == 200:
                    return await response.json()
                logger.debug(response.status)
                logger.debug(await response.json())
        raise Exception()

