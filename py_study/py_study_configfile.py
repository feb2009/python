# -*- coding:UTF-8 -*-
import configparser

config=configparser.ConfigParser()
config.read("./config/gap.ini")
conf_sections=config.sections()
print(conf_sections)
conf_options=config.options("SQL Infomation")
print(conf_options)
conf_items=config.items("SQL Infomation")
print(conf_items)
conf_ip=config.get("SQL Infomation","ip")
conf_user=config.get("SQL Infomation","username")
print(conf_ip," ",conf_user)
