from test_runner.test_runner import TestRunner
from test_runner.test_exception import TestException
from libs.file_manager import FileManager
from libs import utils


class WriteReadCompareDirect(TestRunner):

    def __init__(self):
        super(WriteReadCompareDirect, self).__init__()
        self.file_size = 16*1024
        self.file_mgr = None

    def add_arguments(self):
        super(WriteReadCompareDirect, self).add_arguments()

    def initialize(self):
        super(WriteReadCompareDirect, self).initialize()
        self.file_mgr = FileManager(self.library)

    def test(self):
        for block_address in range(0, 1):
            for page_address in range(0, 16):
                self.log("Step 1. Erase the file")
                args = {
                    "block_address": block_address,
                    "page_address": page_address,
                    "resp_qid": 0,
                }
                self.file_mgr.erase_page(args=args)

                self.log("Step 2. Generate write pattern randomly")
                write_buffer = utils.generate_write_buffer(length=self.file_size)
                self.log("Step 3. Send write request directly to file stack")
                args = {
                    "block_address": block_address,
                    "page_address": page_address,
                    "resp_qid": 0,
                    "buff_ptr": write_buffer
                }
                self.file_mgr.write_to_page(args=args)

                self.log("Step 4. Sequentially read from file for 16 chunks")
                for offset in range(0, 16):
                    self.log(f"Step 4.{offset}. Reading offset {offset}")
                    read_buffer = utils.generate_read_buffer(length=1024)
                    args = {
                        "block_address": block_address,
                        "page_address": page_address,
                        "resp_qid": 0,
                        "offset": offset,
                        "buff_ptr": read_buffer
                    }
                    read_buffer = self.file_mgr.read_one_chunk(args=args)
                    if read_buffer[:1024] != write_buffer[offset * 1024: (offset + 1) * 1024]:
                        raise TestException(f"Read compare failed at offset {offset}")


def main():
    test = WriteReadCompareDirect()
    test.run_test()


if __name__ == "__main__":
    main()
