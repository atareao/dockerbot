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
"""Main process
"""

import asyncio
import logging
import os
import sys
import docker
from dotenv import load_dotenv
from telegram import Telegram

logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)


async def main():
    """Main function
    """
    logger.debug("main")
    load_dotenv()
    url = os.getenv("TELEGRAM_URL")
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    thread_id = os.getenv("TELEGRAM_THREAD_ID")
    if url and token and chat_id and thread_id:
        chat_id = int(chat_id)
        thread_id = int(thread_id)
        telegram_client = Telegram(url, token)
        client = docker.DockerClient(
            base_url="unix:///run/user/1000/docker.sock")
        for event in client.events(decode=True):
            message = process_event(event)
            if message:
                await telegram_client.send_message(chat_id, thread_id, message)


def process_event(event: dict) -> str:
    """Process event

    Args:
        event (dict): The event

    Returns:
        str: A message to send to Telegram
    """
    logger.debug("process_event: %s", event)
    if "Type" in event and "Action" in event and event["Type"] == "container" \
            and event["Action"] == "kill":
        name = event["Actor"]["Attributes"]["name"]
        return f"Container *{name}* was killed"
    return None


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
