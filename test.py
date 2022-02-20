import ctypes
from libs.structures import *
from libs import utils
import json

from libs.constants import *

lib = utils.initiliaze_shared_library()

input_dict = json.load(open("test_lib/configs/input_001.json"))

print(json.dumps(input_dict, sort_keys=False, indent=4))


voter = {
    "tag" : 1,
    "age" : 25,
    "issues" : {
        "social" : 1,
        "economic" : 2
    }
}
for i in range(10):
    output = utils.send_payload(lib, cmd=FE_TASK_FE_INIT)
    print(output.value)
for i in range(10):
    output = utils.send_payload(lib, cmd=FE_TASK_INIT_BE, input_dict=voter)
    voter = output.convert_to_dict()
    print(voter)
