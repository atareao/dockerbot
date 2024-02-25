#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Lorenzo Carbonell <a.k.a. atareao>

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

import inspect
import logging
import traceback
import time


def _logea(message, logger, level):
    if level == logging.DEBUG:
        logger.debug(message)
    elif level == logging.INFO:
        logger.info(message)
    elif level == logging.WARN:
        logger.warn(message)
    elif level == logging.ERROR:
        logger.error(message)
        logger.error(traceback.format_exc())


def logea(item, level):
    stack = inspect.stack()
    parentframe = stack[2][0]
    module = inspect.getmodule(parentframe)
    module_name = module.__name__ if module else __name__
    logger = logging.getLogger(module_name)

    if inspect.isfunction(item):

        def wrap(*args, **kwargs):
            descriptor = f"{item.__module__}.{item.__name__}"
            _logea(f"Start: {descriptor}", logger, level)
            _logea(f"Start: {item.__qualname__}", logger, level)
            if args:
                _logea(f"Args: {args}", logger, level)
            if kwargs:
                _logea(f"Kwargs: {kwargs}", logger, level)
            start = time.time()
            result = item(*args, **kwargs)
            elapsed = int((time.time() - start) * 1000)
            if result:
                _logea(f"Result: {result}", logger, level)
            _logea(f"End: {descriptor} ({elapsed})", logger, level)
            return result
        return wrap
    else:
        _logea(str(item), logger, level)


def debug(item):
    return logea(item, logging.DEBUG)


def info(item):
    return logea(item, logging.INFO)


def warn(item):
    return logea(item, logging.WARN)


def error(item):
    return logea(item, logging.ERROR)

