#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2015 Dilusense Inc. All Rights Reserved.

"""This is a file about Person Class mapping to database table"""

from sqlalchemy import BigInteger, Column, Date, DateTime, Float, Integer, String, text

from db.tables.base import BasePortalDB


class PersonLatest(BasePortalDB):
    """Person corresponding database table Person"""
    __tablename__ = 'person_latest'

    pid = Column(BigInteger, primary_key=True, nullable=False)
    serial_number = Column(String(100))
    identity = Column(String(20))
    name = Column(String(50))
    birthdate = Column(Date)
    sex = Column(String(5))
    nation = Column(String(10))
    address = Column(String(80))
    grant_dept = Column(String(40))
    start_date = Column(Date)
    stop_date = Column(Date)
    nationality = Column(String(50))
    card_type = Column(Integer)
    is_black_list = Column(Integer)
    person_type = Column(String(100))
    process_advice = Column(String(200))
    five_type = Column(Integer)
    is_holiday = Column(Integer)
    control_unit = Column(String(100))
    link_man = Column(String(50))
    telephone = Column(String(30))
    card_img_path = Column(String(130))
    scene_img_path = Column(String(130))
    face_img_path = Column(String(130))
    iron_detect = Column(Integer)
    data_status = Column(String(35))
    rgbd_path = Column(String(100))
    rgbd_md5 = Column(String(35))
    pic_name = Column(String(80))
    pic_md5 = Column(String(35))
    texture_path = Column(String(100))
    texture_md5 = Column(String(35))
    material_path = Column(String(100))
    material_md5 = Column(String(35))
    model_path = Column(String(100))
    model_md5 = Column(String(35))
    _2d_best_frame_path = Column('2d_best_frame_path', String(100))
    _2d_best_frame_md5 = Column('2d_best_frame_md5', String(35))
    _3d_best_frame_color_path = Column('3d_best_frame_color_path', String(100))
    _3d_best_frame_color_md5 = Column('3d_best_frame_color_md5', String(35))
    _3d_best_frame_depth_path = Column('3d_best_frame_depth_path', String(100))
    _3d_best_frame_depth_md5 = Column('3d_best_frame_depth_md5', String(35))
    _3d_1v1_class1 = Column('3d_1v1_class1', String(35))
    _3d_1v1_class1_score = Column('3d_1v1_class1_score', Float)
    _3d_1v1_class2 = Column('3d_1v1_class2', String(35))
    _3d_1v1_class2_score = Column('3d_1v1_class2_score', Float)
    _3d_1v1_class3 = Column('3d_1v1_class3', String(35))
    _3d_1v1_class3_score = Column('3d_1v1_class3_score', Float)
    standby1 = Column(String(50))
    standby2 = Column(String(100))
    standby3 = Column(String(200))
    device_code = Column(String(30))
    collect_time = Column(DateTime, primary_key=True, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    create_time = Column(DateTime)
