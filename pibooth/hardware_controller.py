"""Controls the hardware and GPIO access.

This module handles all the access to GPIO pins and other hardware.
"""

import time
import sys
from thread import allocate_lock, start_new_thread
import RPi.GPIO as GPIO

_should_run = False
_is_running = False
_is_initialized = False
thread_lock = allocate_lock()
is_running_lock = allocate_lock()


def init(args):
    if not _is_initialized:
        GPIO.setmode(GPIO.GPIOBOARD)
        GPIO.setup(18, GPIO.IN)
        GPIO.setup(11, GPIO.OUT)
        _is_initialized = True
    return _is_initialized


def _query_loop():
    global _is_running
    is_running_lock.acquire()
    if not _is_running:
        _is_running = True
    else:
        quit = True
    is_running_lock.release()
    if quit:
        return False

    while _should_run:
        thread_lock.acquire()
        # do stuff
        thread_lock.release()

    is_running_lock.acquire()
    _is_running = False
    quit = False
    is_running_lock.release()


def start():
    global _should_run
    _should_run = True
    thread.start_new_thread(_query_loop)


def stop():
    global _should_run
    _should_run = False


if __name__ = "main":
    init(sys.argv[1:])
    return start()
else:
    _is_initialized = init()
