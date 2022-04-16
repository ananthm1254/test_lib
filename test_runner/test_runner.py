import logging
from libs import utils
import os
import inspect

class TestRunner:
    """
    Test runner class for generic testing purposes
    """

    def __init__(self):
        self.library = None
    
    def get_caller_info(self):
        caller_frame = inspect.stack()[2]
        caller_filename_full = caller_frame.filename
        caller_filename_only = os.path.splitext(os.path.basename(caller_filename_full))[0]
        return caller_filename_full, caller_filename_only
    
    def configure_logging(self, name=None):
        if name is not None:
            logger = logging.getLogger(name)
        else:
            logger = logging.getLogger(__name__)

        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        return logger

    def log(self, msg, type="INFO"):
        _, filename_only = self.get_caller_info()
        logger = self.configure_logging(name=filename_only)
        if type == "INFO":
            logger.info(msg)
        elif type == "DEBUG":
            logger.debug(msg)
        elif type == "WARNING":
            logger.warning(msg)
        elif type == "ERROR":
            logger.error(msg)
        else:
            logger.error("Wrong logging type")

    def load_library_module(self):
        self.library = utils.initiliaze_shared_library()

    def initialiaze(self):
        self.log("Load library into the test framework")
        self.load_library_module()

    def test(self):
        pass

    def run_test(self):
        self.log("Initiliazing Test Runner")
        self.initialiaze()
        self.test()