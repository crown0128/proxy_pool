# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ProxyHandler.py
   Description :
   Author :       JHao
   date：          2016/12/3
-------------------------------------------------
   Change Activity:
                   2016/12/3:
-------------------------------------------------
"""
__author__ = 'JHao'

from helper.proxy import Proxy
from db.dbClient import DbClient
from handler.configHandler import ConfigHandler


class ProxyHandler(object):
    """ Proxy CRUD operator"""

    def __init__(self):
        self.conf = ConfigHandler()
        self.db = DbClient(self.conf.dbConn)

    def get(self):
        """
        return a useful proxy
        :return:
        """
        self.db.changeTable(self.conf.useProxy)
        proxy = self.db.get()
        if proxy:
            return Proxy.createFromJson(proxy)
        return None

    def pop(self):
        """
        return and delete a useful proxy
        :return:
        """
        self.db.changeTable(self.conf.useProxy)
        proxy = self.db.pop()
        if proxy:
            return Proxy.createFromJson(proxy)
        return None

    def put(self, proxy):
        """
        put proxy into use proxy
        :return:
        """
        self.db.changeTable(self.conf.useProxy)
        self.db.put(proxy)

    def delete(self, proxy):
        """
        delete useful proxy
        :param proxy:
        :return:
        """
        self.db.changeTable(self.conf.useProxy)
        return self.db.delete(proxy.proxy)

    def getAll(self):
        """
        get all proxy from pool as Proxy list
        :return:
        """
        self.db.changeTable(self.conf.useProxy)
        proxies_dict = self.db.getAll()
        return [Proxy.createFromJson(value) for _, value in proxies_dict.items()]

    def exists(self, proxy):
        """
        check proxy exists
        :param proxy:
        :return:
        """
        self.db.changeTable(self.conf.useProxy)
        return self.db.exists(proxy.proxy)

    def getCount(self):
        """
        return raw_proxy and use_proxy count
        :return:
        """
        self.db.changeTable(self.conf.useProxy)
        total_raw_proxy = self.db.getCount()
        self.db.changeTable(self.conf.rawProxy)
        total_use_proxy = self.db.getCount()
        return {'raw_proxy': total_raw_proxy, 'use_proxy': total_use_proxy}
