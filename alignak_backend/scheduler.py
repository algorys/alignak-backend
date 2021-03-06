#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ``alignak_backend.scheduler`` module

    This module manages the scheduler jobs
"""
import alignak_backend.app


def cron_cache():
    """
    It's the scheduler used to send to graphite / influxdb retention perfdata if previously
    graphite / influxdb wasn't available

    :return: None
    """
    # test communication and see if data in cache
    alignak_backend.app.cron_timeseries()
