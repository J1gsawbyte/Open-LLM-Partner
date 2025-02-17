# Manager/Logger.py
import os
import json
import time

current_path = 'd:\\Code\\Project\\AIPartner\\'

LogTypeColorDic = {}

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
    
    def Str2Log(self, head : str, info : str) -> str:
        """
        字符串转日志格式 ==== [头部]年-月-日 时:分:秒 : info
        Args:
            head (str): 日志头部 
            info (str): 详细信息
        Returns:
            str: 日志字符串
        """
        # 获取当前时间并格式化为 '年-月-日 时:分:秒'
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 拼接时间与信息，格式为 "时间 : info"
        log_message = f"[{head}]{formatted_time} : {info}"    
        # 返回日志字符串
        return log_message
    
        
    def log(self, info : str, ) -> None:                                         
        """
        记录日志
        Args:
            info(str): 日志详细信息
        """
        with open(self.log_file_path, 'a') as f:
            f.write(info + '\n')
            
    def print_log(self, log : str, type : str) -> None:
        """ 
        输出日志
        Args:
            log (str): 要输出的日志字符串
            type (str): 日志类型 - |Info|Warn|Error|
        """
        print(f'{type} - ' + log)
        
    def print_colored_log(self, log : str, type : str) -> None:
        """ 
        根据日志的类型，输出不同颜色的日志 | 在config.json中配置
        Args:
            log (str): 要输出的日志字符串
            type (str): 日志类型 - |Info|Warn|Error|
        """
        print()
        
        