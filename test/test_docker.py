#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests
"""

import os
import asyncio
import pytest
from src.docker import Docker

pytest_plugins = ("pytest_asyncio",)

socket = "/run/user/1000/docker.sock"
docker = Docker(socket)


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
def get_docker():
    socket = "/run/user/1000/docker.sock"
    return Docker(socket)


@pytest.mark.asyncio
async def test_get_containers(get_docker):
    """Test telegram class
    """
    containers = await get_docker.get_containers()
    assert containers is not None


@pytest.mark.asyncio
async def test_get_images():
    """Test telegram class
    """
    docker = Docker("/run/user/1000/docker.sock")
    images = await docker.get_images()
    assert images is not None

