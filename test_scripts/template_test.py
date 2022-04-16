from test_runner.test_runner import TestRunner
from libs import structures
import ctypes

class TemplateTest(TestRunner):

    def __init__(self):
        super(TemplateTest, self).__init__()

    def initialiaze(self):
        super(TemplateTest, self).initialiaze()
        pass

    def test(self):
        self.log("Good")
        self.log(self.library)
        erasemsg = structures.EraseMsg()
        erasemsg.respQId = 0
        erasemsg.address.address = 0
        ret = self.library.FileErase(ctypes.byref(erasemsg))
        self.log(ret)

def main():
    test = TemplateTest()
    test.run_test()

if __name__ == "__main__":
    main()