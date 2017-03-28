#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
from apscheduler.schedulers.background import BackgroundScheduler

from services.timer_task.timer_tasks import *


def execute_timer_tasks():

    scheduler = BackgroundScheduler()

    scheduler.add_job(tt_1, 'cron', id='tt_clear_person_info_cache_data',
                      hour='22')

    scheduler.add_job(tt_1, 'cron', id='tt_clear_real_time_pic_cache_data',
                      hour='8-22', minute='0,10,20,30,40,50')
    scheduler.start()
