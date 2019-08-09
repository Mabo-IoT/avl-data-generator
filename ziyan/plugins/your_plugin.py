# -*- coding: utf-8 -*-
import time
import random
from logging import getLogger

from Doctopus.Doctopus_main import Check, Handler

log = getLogger('Doctopus.plugins')


class MyCheck(Check):
    def __init__(self, configuration):
        super(MyCheck, self).__init__(configuration=configuration)

    
    def generate(self):
        """
        generate random data
        """
        data = {
            "anl_lmbdafrcfr_x": self.random_float(-1,1),
            "bct1_ex_t": self.random_float(20, 630),
            "bskl_air_t": self.random_float(20,25),
            "bskl_cba_ap": self.random_float(10,11),
            "cac_airi_ap": self.random_float(96, 101),
            "cac_airi_t": self.random_float(20, 40),
            "cac_airo_ap": self.random_float(95, 102),
            "cac_airo_t": self.random_float(12, 36),
            "cac_airt_dvl": self.random_float(34, 36),
            "cbn_ve_pct": self.random_float(0, 1),
            "cc_gas_p": self.random_float(-0.1, 1),
            "cel_air_t": self.random_float(20, 30),
            "cel_relhum_pct": self.random_float(0,1),
            "ct1a_ex_t": self.random_float(20, 650),
            "cwc_pidact_t": self.random_float(0, 100),
            "cwc_wtrbyp_p": self.random_float(1, 90),
            "cwc_wtrbyp_t": self.random_float(20, 95),
            "cwc_wtri_p": self.random_float(0, 100),
            "cwc_wtri_t": self.random_float(0,100),
            "cwc_wtro_p": self.random_float(0, 100),
            "cwc_wtro_t": self.random_float(0, 100),
            "cwc_wtro_dvl": self.random_float(0, 100),
            "d_afil_tq": self.random_float(0,150),
            "d_spddig_n": self.random_float(0, 5000),
            "e_bmep_P": self.random_float(0, 10),
            "e_edsp_vl": self.random_float(0, 65),
            "e_obsfc_fe": self.random_float(0, 10),
            "e_pwr_pw": self.random_float(0, 10),
            "e_saeapp_tq": self.random_float(-100000, 0),
            "ecol_res_p": self.random_float(0, 100),
            "eo_cool_vf": self.random_float(20, 70),
            "esp_oil_t": self.random_float(20,110),
            "ex_bkpvlvr_set": self.random_float(0, 5),
            "ex_postctbk_p": self.random_float(-2, 2),
            "ex_prectbk_p": self.random_float(0, 18),
            "f_f_dox": self.random_float(0, 2),
            "fl_sup_p": self.random_float(0, 400),
            "oc_eoilt_dvl": self.random_float(0, 100),
            "oc_pidact_t": self.random_float(20, 100),
            "og_oil_p": self.random_float(0, 260),
            "og_oil_t": self.random_float(20, 105),
            "ok_fire": random.randint(0,1),
            "ok_gas": random.randint(0,1),
            "s_cycdone_cnt": random.randint(0,1000),
            "s_f_t": self.random_float(0, 20),
            "s_saeapp_pw": self.random_float(-100000, 0),
            "status": random.randint(0,1),
        }
        return data 

    @staticmethod
    def random_float(a, b):
        return round(random.uniform(a, b),2)

    def user_check(self):
        """

        :param command: user defined parameter.
        :return: the data you requested.
        """

        data = self.generate()
        # data = {
        #     "status": random.randint(0,1),
        #     "temp": round(random.uniform(20.0, 25.0),2),
        #     "warning": "warning msg",
        # }
        log.debug('%s', data)
        time.sleep(5)
        yield data


class MyHandler(Handler):
    def __init__(self, configuration):
        super(MyHandler, self).__init__(configuration=configuration)

    def user_handle(self, raw_data):
        """
        用户须输出一个dict，可以填写一下键值，也可以不填写
        timestamp， 从数据中处理得到的时间戳（整形?）
        tags, 根据数据得到的tag
        data_value 数据拼接形成的 list 或者 dict，如果为 list，则上层框架
         对 list 与 field_name_list 自动组合；如果为 dict，则不处理，认为该数据
         已经指定表名
        measurement 根据数据类型得到的 influxdb表名

        e.g:
        list:
        {'data_value':[list] , required
        'tags':[dict],        optional
        'table_name',[str]   optional
        'timestamp',int}      optional

        dict：
        {'data_value':{'fieldname': value} , required
        'tags':[dict],        optional
        'table_name',[str]   optional
        'timestamp',int}      optional

        :param raw_data: 
        :return: 
        """
        # exmple.
        # 数据经过处理之后生成 value_list
        log.debug('%s', raw_data)
        data_value_list = raw_data

        tags = {'eqpt_no': '1900'}

        # user 可以在handle里自己按数据格式制定tags
        user_postprocessed = {'data_value': data_value_list,
                              'tags': tags, }
        yield user_postprocessed
