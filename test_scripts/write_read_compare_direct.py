from test_runner.test_runner import TestRunner
from test_runner.test_exception import TestException
from libs.file_manager import FileManager
from libs import utils


class TemplateTest(TestRunner):

    def __init__(self):
        super(TemplateTest, self).__init__()
        self.file_size = 16*1024
        self.file_mgr = None

    def initialize(self):
        super(TemplateTest, self).initialize()
        self.file_mgr = FileManager(self.library)

    def test(self):
        self.log("Step")

        self.log("Step 1. Generate write pattern randomly")
        write_buffer = utils.generate_write_buffer(length=self.file_size, seed=150)
        self.log("Step 2. Send write request directly to file stack")
        args = {
            "block_address": 0,
            "page_address": 0,
            "resp_qid": 0,
            "buff_ptr": write_buffer
        }
        self.file_mgr.write_to_page(args=args)

        self.log("Step 3. Sequentially read from file for 16 chunks")
        for offset in range(0, 16):
            self.log("Step 3.{}. Reading offset {}".format(offset, offset))
            read_buffer = utils.generate_read_buffer(length=1024)
            args = {
                "block_address": 0,
                "page_address": 0,
                "resp_qid": 0,
                "offset": offset,
                "buff_ptr": read_buffer
            }
            read_buffer = self.file_mgr.read_one_chunk(args=args)
            if read_buffer[:1024] != write_buffer[offset * 1024: (offset + 1) * 1024]:
                raise TestException(f"Read compare failed at offset {offset}")


def main():
    test = TemplateTest()
    test.run_test()


if __name__ == "__main__":
    main()
