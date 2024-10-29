import inspect
import logging

class BaseClass:
    import logging

    def getLogger(self):
        # to get the name of the test case file name at runtime
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # FileHandler class to set the location of log file
        fileHandler = logging.FileHandler('logfile.log')

        # Formatter class to set the format of log file
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        # object of FileHandler gets formatting info from setFormatter #method
        fileHandler.setFormatter(formatter)

        # logger object gets formatting, path of log file info with addHandler #method
        logger.addHandler(fileHandler)

        # setting logging level to INFO
        logger.setLevel(logging.DEBUG)

        # logging debug message with logger object
        logger.debug("A debug statement is executed")

        # logging info message with logger object
        logger.info("An information statement is executed")

        # logging warning message with logger object
        logger.warning("A warning message is executed")

        # logging error message with logger object
        logger.error("An error message is executed")

        # logging critical message with logger object
        logger.critical("A critical message is executed")

        return logger