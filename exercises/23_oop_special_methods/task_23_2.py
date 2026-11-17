import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "22_oop_basics"))
from task_22_2 import CiscoTelnet as BaseCiscoTelnet


class CiscoTelnet(BaseCiscoTelnet):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.telnet.close()
