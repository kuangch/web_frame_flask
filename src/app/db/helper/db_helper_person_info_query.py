#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
import traceback
from flask import logging
from sqlalchemy import func
from db.instance_db_connection import DBConnection
from db.tables.info_portal import InfoPortal
from db.tables.person import Person
from db.tables.person_latest import PersonLatest
from utils.common import fun_execute_time
from utils.global_info import GlobalInfo


def query_pic_frame_model_path(portal_id, time):
    db_session = None
    try:
        db_session = DBConnection().connect()
        if db_session is not None:
            query = db_session\
                .query(Person.pic_name.label('pic_path'),
                       Person.texture_path.label('texture_path'),
                       Person._2d_best_frame_path.label('_2d_pic_path'),
                       Person.material_path.label('mtl_path'),
                       Person.model_path.label('obj_path'))\
                .filter(Person.device_code == portal_id)\
                .filter(Person.collect_time == time)

            res = query.all()[0]
            return res

    except:
        logging.getLogger(GlobalInfo.logger_main).error(traceback.format_exc())
        return None
    finally:
        if db_session:
            db_session.close()
    return None


def query_latest_person_pass_info(min_id=1, limit=''):
    db_session = None
    try:
        db_session = DBConnection().connect()
        if db_session is not None:
            query = db_session\
                .query(PersonLatest.pic_name.label('pic_path'),
                       PersonLatest.pid.label('id'),
                       PersonLatest.collect_time.label('collect_time'),
                       PersonLatest.name.label('person_name'),
                       InfoPortal.portal_id.label('portal_id'))\
                .join(InfoPortal, InfoPortal.portal_id == PersonLatest.device_code)\
                .filter(PersonLatest.pid > min_id)\
                .order_by(PersonLatest.pid.desc())

            if isinstance(limit, int):
                query = query.limit(limit)

            return query.all()

    except:
        logging.getLogger(GlobalInfo.logger_main).error(traceback.format_exc())
        return None
    finally:
        if db_session:
            db_session.close()
    return None


@fun_execute_time
def query_person_max_index():
    """
    query person max index
    """

    db_session = None
    try:
        db_session = DBConnection().connect()
        if db_session is not None:
            query = db_session.query(func.max(PersonLatest.pid).label('max_id'))
            return query.all()[0].max_id or 0

    except:
        logging.getLogger(GlobalInfo.logger_main).error(traceback.format_exc())
        return None
    finally:
        if db_session:
            db_session.close()
    return None
