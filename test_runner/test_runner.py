import logging
import time
from libs import utils
from test_runner.test_exception import TestException
import os
import inspect
import argparse


class TestRunner:
    """
    Test runner class for generic testing purposes
    """

    def __init__(self):
        self.library = None
        self.logger = None
        self.start = None
        self.stop = None
        self.parser = None
        self.args = None

    def add_arguments(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            "--build_library",
            default=None,
            type=str,
            help="Build Library"
        )
        self.args = self.parser.parse_args()

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
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        return logger

    def log(self, msg, type="INFO"):
        _, filename_only = self.get_caller_info()
        if self.logger is None:
            self.logger = self.configure_logging(name=filename_only)
        if type == "INFO":
            self.logger.info(msg)
        elif type == "DEBUG":
            self.logger.debug(msg)
        elif type == "WARNING":
            self.logger.warning(msg)
        elif type == "ERROR":
            self.logger.error(msg)
        else:
            self.logger.error("Wrong logging type")

    def load_library_module(self):
        self.log(f"Load custom deveoped library {self.args.build_library}")
        self.library = utils.initiliaze_shared_library(lib_file=self.args.build_library)

    def initialize(self):
        self.add_arguments()
        self.log("Load library into the test framework")
        self.load_library_module()

    def test(self):
        pass

    def test_failed_method(self, err):
        self.stop = time.perf_counter()
        self.log("TEST FAILED")
        self.log(f"Run time : {round(self.stop - self.start, 4)}")
        raise err

    def test_passed_method(self):
        self.stop = time.perf_counter()
        self.log("TEST PASSED")
        self.log(f"Run time : {round(self.stop - self.start, 4)}")

    def run_test(self):
        self.start = time.perf_counter()
        self.log("Initializing Test Runner")
        try:
            self.initialize()
        except Exception as err:
            self.test_failed_method(err)

        try:
            self.test()
        except TestException as err:
            self.test_failed_method(err)
        else:
            self.test_passed_method()
