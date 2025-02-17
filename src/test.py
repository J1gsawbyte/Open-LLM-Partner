from Manager.Logger import  Logger

# 避免生成__pycache__文件夹
import sys
sys.dont_write_bytecode = True

if __name__ == '__main__':
    logger = Logger()
    logger.print_colored_log('Info', 'TestHead', 'This is an info message.')
    logger.print_colored_log('Warn', 'TestHead', 'This is a warning message.')
    logger.print_colored_log('Error', 'TestHead', 'This is an error message.')
