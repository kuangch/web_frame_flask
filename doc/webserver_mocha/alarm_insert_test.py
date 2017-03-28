import os
import string
from db.instance_db_connection import DBConnection
from db.tables.alarm import AlarmInfo
from utils.init_helper import InitHelper

__author__ = 'Thinkpad'

import random
import time

import datetime

pool = ['a','b','c','d','e','f','g','h','i','j','A','B','C','D','E','F','G','H','I','J','K','M','1','2','3','4','5','6','7','8']

device_codes = ['B1M11SG07420', 'B1M11SG92690', 'B1M11SG30239', 'B1M11SG40179', 'B1M11SG29688',
                'B1M11SG92791', 'B1M11SG20461', 'B1M11SG18619', 'B1M11SG61951', 'B1M11SG59116']

def insert_data():

    today = datetime.datetime.now()
    db = DBConnection().connect()
    for i in range(0, 1000000):
        itme = AlarmInfo()
        itme.raise_time = today
        # itme.device_code = device_codes[random.randint(0, 9)]
        itme.device_code = str(random.randint(1, 21))
        itme.alarm_severity = random.randint(1, 3)
        # itme.personal_info_id = string.join(random.sample(pool, 20)).replace(" ", "")
        itme.personal_info_id = '123456'
        itme.personal_info_name = string.join(random.sample(pool, 10)).replace(" ", "")
        itme.personal_info_has_passport = random.randint(0, 1)
        db.add(itme)
        db.commit()
        time.sleep(2)


def run():

    # init app config
    config_dir = os.path.dirname(os.getcwd())
    config_dir = os.path.dirname(config_dir) + '/src/local/'
    InitHelper.init_app_conf(config_dir)

    insert_data()


if __name__ == '__main__':

    run()
