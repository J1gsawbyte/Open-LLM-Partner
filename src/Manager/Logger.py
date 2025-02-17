# Manager/Logger.py
import os
import json
import time

current_path = 'd:\\Code\\Project\\AIPartner\\'

ColorDic = {
    'default' : '\033[0m',
    'blod' : '\033[1m',
    'underline' : '\033[4m',
    'black' : '\033[30m',
    'red' : '\033[31m',
    'green' : '\033[32m',
    'yellow' : '\033[33'
}

LogTypeColorDic = {}

def get_color_utf8(
    color : str, 
    ) -> str:
    """通过颜色获取其对应的UTF-8码
    Args:
        color (str): 颜色字符串
    Returns:
        str: 带有颜色的字符串
    """
    string = ColorDic.get(color)
    if len(string) == 0:
        return ColorDic['default']
    return string
def get_color_reset_utf8() -> str:
    """获取重置颜色的UTF-8码
    Returns:
        str: 重置颜色的UTF-8码
    """
    return '\033[0m'
    
    

class Logger:
    log_output_path = ''
    
    def __init__(self):
        self.load_default_log_output_path()
        self.load_default_log_type_color_dic()
        
        
    def load_default_log_output_path(self, config_path : str = current_path + 'config\\config.json'):
        """
        获取默认日志输出路径
        Args:
            config_path (str): config文件路径
        """
        with open(config_path, 'r') as f:
            config = json.load(f)
            self.log_output_path = config['default-logger-output-path']
            
    def load_default_log_type_color_dic(self, config_path : str = current_path + 'config\\config.json'):
        """
        获取日志类型颜色字典
        Args:
            config_path (str): config文件路径
        """
        with open(config_path, 'r') as f:
            config = json.load(f)
            LogTypeColorDic['Info'] = config['default-log-type-color']['Info']
            LogTypeColorDic['Warn'] = config['default-log-type-color']['Warn']
            LogTypeColorDic['Error'] = config['default-log-type-color']['Error']
    
    def log(self, info : str, ) -> None:                                         
        """
        记录日志
        Args:
            info(str): 日志详细信息
        """
        with open(self.log_file_path, 'a') as f:
            f.write(info + '\n')
            
    def print_log(self, type : str, head : str, info : str) -> None:
        """ 
        输出日志
        Args:
            type (str): 日志类型 - |Info|Warn|Error|
            head (str): 日志头部信息
            info (str): 要输出的字符串
        """
        # 获取当前时间并格式化为 '年-月-日 时:分:秒'
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 拼接时间与信息，格式为 "时间 : info"
        log_message = f" {type} - [{head}]{formatted_time} : {info}"    
        
        print(log_message)
        
    def print_colored_log(self, type : str, head : str, info : str) -> None:
        """ 
        根据日志的类型，输出不同颜色的日志 | 在config.json中配置
        Args:
            type (str): 日志类型 - |Info|Warn|Error|
            head (str): 日志头部信息
            info (str): 要输出的字符串
        """
        # 获取当前时间并格式化为 '年-月-日 时:分:秒'
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 拼接时间与信息，格式为 "时间 : info"
        log_message = f" {type} - [{head}]{formatted_time} : {info}"
            
        print(get_color_utf8(LogTypeColorDic.get(type)) + log_message + get_color_reset_utf8())
        
        