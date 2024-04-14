import random
import time

import urllib3


class EndDevice:
    def __init__(self,num) :
        self.num=num

    def Generate_mac_address(self):
        mac_addresss = [str(random.randint(0x00, 0xFF)) for x in range(self.num+1)]
        return ("00:" + ":".join(mac_addresss))
    """GENERATES RANDOM MAC ADDRESS ANS ASSIGNS TO END-DEVICES"""

e1=EndDevice(2)
print(e1.Generate_mac_address())