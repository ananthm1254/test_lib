from test_runner.test_runner import TestRunner
from libs import structures
import ctypes
import random

class TemplateTest(TestRunner):

    def __init__(self):
        super(TemplateTest, self).__init__()
        self.file_size = 16*1024

    def initialiaze(self):
        super(TemplateTest, self).initialiaze()
        pass

    def test(self):
        self.log("Good")
        self.log(self.library)
        # while True:
        # self.file_size = self.file_size + 1024
        erasemsg = structures.EraseMsg()
        erasemsg.respQId = 0
        erasemsg.address.address = 0
        ret = self.library.FileErase(ctypes.byref(erasemsg))

        writemsg = structures.WriteMsg()
        writemsg.respQId = 0
        writemsg.address.address = 0
        self.log(writemsg.buffPtr)
        x = [random.randint(0, 255) for i in range(0,self.file_size)]
        # self.log(x)
        arr = (ctypes.c_uint8 * len(x))(*x)
        ctypes.cast(arr, ctypes.POINTER(ctypes.c_uint8))
        writemsg.buffPtr = arr
        ret = self.library.FileWrite(ctypes.byref(writemsg))
        self.log(ret)

        for i in range(0,16):
            readmsg = structures.ReadMsg()
            readmsg.address.addressSpecific.block_number = 0
            readmsg.address.addressSpecific.page_number = 0
            readmsg.address.addressSpecific.offset = i
            readmsg.respQId = 0
            y = (ctypes.c_uint8 * (1024))()
            ctypes.cast(y, ctypes.POINTER(ctypes.c_uint8))
            readmsg.buffPtr = y
            ret = self.library.FileRead(ctypes.byref(readmsg))
            y = readmsg.buffPtr
            self.log(y[:1024])
            if y[:1024] == x[i*1024:(i+1)*1024]:
                self.log("success with {}".format(self.file_size))
            # else:
                # break
        # self.log(readmsg.buffPtr[:self.file_size])

def main():
    test = TemplateTest()
    test.run_test()

if __name__ == "__main__":
    main()