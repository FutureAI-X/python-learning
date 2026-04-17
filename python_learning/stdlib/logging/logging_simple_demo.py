import logging

def use_print():
    print("debug message")
    print("info message")
    print("warning message")
    print("error message")
    print("critical message")

def use_logging():
    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")

if __name__ == '__main__':
    print("*" * 20)
    use_print()
    print("*" * 20)
    use_logging()