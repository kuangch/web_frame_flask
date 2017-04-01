#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
from flask import logging
from msg_trans import ZMQPort
from msg_trans.thread_subs_msg import SubsMsgServer
from services.msg_center.zmq_msg_connections import ZMQConns
from utils.global_info import GlobalInfo
from utils.my_constant import MyConstant
from utils.regular_expression import Regular
from utils.serialize_utils import SerializeUtils


class PortalMsgManager(object):

    @staticmethod
    def add_new_conn(ip):
        if Regular.verify_ip(ip):
            sms = SubsMsgServer(ip, ZMQPort.SUBS)
            sms.start()
            if sms.isAlive():
                ZMQConns().put(ip, sms)
        else:
            logging.getLogger(GlobalInfo.logger_main).info('ip: ' + ip + ' is unlawful can not connect to server')


    @staticmethod
    def init_portals():
        ips = SerializeUtils.get(MyConstant.portal_ips_serialize_data_key)
        if ips is None:
            logging.getLogger(GlobalInfo.logger_main).info('no ip to init zmq conn')
            return
        ips = set(ips)
        for ip in ips:
            PortalMsgManager.add_new_conn(ip)


    @staticmethod
    def update_portals(ips):
        smss = ZMQConns().get_all()
        sms_keys = ([])
        ip_keys = ([])

        if type(ips) == dict:
            ip_keys_store = {}
        elif type(ips) == list:
            ip_keys_store = []
        else:
            raise NameError('parameter of this method must be dict or list')

        try:
            ip_keys = set(ips)
        except:
            pass
        try:
            sms_keys = set(smss)
        except:
            pass

        new_ips = ip_keys - sms_keys
        old_ips = sms_keys - ip_keys
        intersection_ips = ip_keys & sms_keys

        for ip_key in ip_keys:
            if type(ips) == dict:
                ip_keys_store[ip_key] = ips[ip_key]
            else:
                ip_keys_store.append(ip_key)


        for ip in intersection_ips:
            logging.getLogger(GlobalInfo.logger_main).info('portal of ip: ' + ip + ' msg passageway is already exits')

        for ip in old_ips:
            if ZMQConns().get(ip) is not None:
                ZMQConns().get(ip).run_flag = False
                ZMQConns().remove(ip)

        for ip in new_ips:
            PortalMsgManager.add_new_conn(ip)

        SerializeUtils.update(MyConstant.portal_ips_serialize_data_key, ip_keys_store)

