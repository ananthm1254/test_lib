from libs import utils
from test_runner.test_exception import TestException

class FileManager:
    def __init__(self, lib):
        self.lib = lib

    def erase_page(self, block_address=None, page_address=None, resp_qid=None, args=None):
        if args is None:
            args = {
                "block_address": block_address,
                "page_address": page_address,
                "resp_qid": resp_qid,
            }
        if utils.erase_direct(self.lib, args=args):
            pass
        else:
            raise TestException("Erase failed at Block: {} and Page : {}".format(args["block_address"], args["page_address"]))

    def write_to_page(self, block_address=None, page_address=None, resp_qid=None, buff_ptr=None, args=None):
        if args is None:
            args = {
                "block_address": block_address,
                "page_address": page_address,
                "resp_qid": resp_qid,
                "buff_ptr": buff_ptr
            }
        if utils.write_direct(self.lib, args=args):
            pass
        else:
            raise TestException("Write failed at Block: {} and Page : {}".format(args["block_address"], args["page_address"]))
        

    def read_one_chunk(self, block_address=None, page_address=None, offset=None, resp_qid=None, buff_ptr=None, args=None):
        if args is None:
            args = {
                "block_address": block_address,
                "page_address": page_address,
                "offset": offset,
                "resp_qid": resp_qid,
                "buff_ptr": buff_ptr
            }
        ret, read_buffer = utils.read_direct(self.lib, args=args)
        if ret:
            return read_buffer
        else:
            raise TestException("Read failed at Block: {}, Page : {} and Offset: {}".format(args["block_address"], args["page_address"],
                                                                                            args["offset"]))

    def write(self):
        pass

    def read(self):
        pass

    def read_compare(self):
        pass