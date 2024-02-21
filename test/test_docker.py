#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests
"""

import logging
import pytest
from src.docker import Docker

logger = logging.getLogger(__name__)
pytest_plugins = ("pytest_asyncio",)
socket = "/run/user/1000/docker.sock"


@pytest.mark.asyncio
async def test_get_containers():
    """Test telegram class
    """
    docker = Docker(socket)
    containers = await docker.get_containers()
    logger.debug(containers)
    if containers is None:
        pytest.fail("Can not get containers")


@pytest.mark.asyncio
async def test_get_images():
    """Test telegram class
    """
    docker = Docker(socket)
    images = await docker.get_images()
    logger.debug(images)
    if images is None:
        pytest.fail("Can not get images")
