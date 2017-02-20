import sys, os
import math
sys.path.append('C:/Users/nstoddar/AppData/Local/Continuum/Anaconda3/envs/py2_pcse/Lib/site-packages/pcse')
import datetime as dt

import pcse
from pcse.base_classes import SimulationObject, VariableKiosk

mysignal = "My first signal"

class MySimObj(SimulationObject):

    def initialize(self, day, kiosk):
        self._connect_signal(self.handle_mysignal, mysignal)

    def handle_mysignal(self, arg1, arg2):
        print "Value of arg1,2: %s, %s" % (arg1, arg2)

    def send_signal_with_exact_arguments(self):
        self._send_signal(signal=mysignal, arg2=math.pi, arg1=None)

    def send_signal_with_more_arguments(self):
        self._send_signal(signal=mysignal, arg2=math.pi, arg1=None,
                          extra_arg="extra")

    def send_signal_with_missing_arguments(self):
        self._send_signal(signal=mysignal, arg2=math.pi, extra_arg="extra")


# Create an instance of MySimObj
day = dt.date(2000,1,1)
k = VariableKiosk()
mysimobj = MySimObj(day, k)

# This sends exactly the right amount of keyword arguments
mysimobj.send_signal_with_exact_arguments()

# this sends an additional keyword argument 'extra_arg' which is ignored.
mysimobj.send_signal_with_more_arguments()

# this sends the signal with a missing 'arg1' keyword argument which the handler
# expects and thus causes an error, raising a TypeError
try:
    mysimobj.send_signal_with_missing_arguments()
except TypeError, exc:
    print "TypeError occurred: %s" % exc
