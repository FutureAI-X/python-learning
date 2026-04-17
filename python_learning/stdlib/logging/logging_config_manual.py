import logging

logger = logging.getLogger()        # 如果没指定名称，获取的是根Logger
logger.setLevel(logging.DEBUG)      # 设置日志打印级别

# 创建 Formatter, 定义日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 创建控制台 Handler (StreamHandler)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# 创建文件 Handler (FileHandler)
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

# 将 Handler 添加到 Logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")