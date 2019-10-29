"""读取数据文件"""
import os
import yaml
from config import basedir

def read_excel():
    pass


def read_yaml(file_name, section=None):
    file_path = os.path.join(basedir, 'data', file_name)
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    if section is None:
        return data
    else:
        return data[section]
