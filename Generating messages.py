# -*- coding: utf-8 -*-
"""
Created on Wed May 30 20:50:39 2018

@author: TRISHA
"""

import simplefix
import datetime
import sys
import time
import warnings
from simplefix import *


msg = simplefix.FixMessage()

class FixMessage(object):
    
def __init__(self):
    print("initialising message")
    
    self.begin_string = '8'
    self.message_type = '35'
    
     def count(self):
        return len(self.pairs)
   
msg.append_pair(1, "tm435967")
msg.append_pair(54, 1)
msg.append_pair(44, 37.0582)

 if tag is None or value is None:

        if int(tag) == 8:
            self.begin_string = fix_val(value)

        if int(tag) == 35:
            self.message_type = fix_val(value)
      if header:
            self.pairs.insert(self.header_index,
                              (fix_tag(tag),
                               fix_val(value)))
            self.header_index += 1
        else:
            self.pairs.append((fix_tag(tag), fix_val(value)))
        return

msg.append_pair(8, "FIX.4.2")
msg.append_pair(35, 0)
msg.append_pair(49, "SENDER")
msg.append_pair(56, "TARGET")
msg.append_pair(112, "TR0003692")
msg.append_pair(34, 4684, header=True)
msg.append_time(52, header=True)

BEGIN_STRING = "8=FIX.4.2"
STR_SEQ = ["49=SENDER", "56=TARGET"]

msg.append_string(BEGIN_STRING, header=True)
msg.append_strings(STR_SEQ, header=True)


# append time 

def append_time(self, tag, timestamp=None, precision=3, utc=True,
                    header=False):
    
      if not timestamp:
            t = datetime.datetime.utcnow()

        elif type(timestamp) is float:
            if utc:
                t = datetime.datetime.utcfromtimestamp(timestamp)
            else:
                t = datetime.datetime.fromtimestamp(timestamp)

        else:
            t = timestamp

        s = t.starttime("%Y%m%d-%H:%M:%S")
        if precision == 3:
            s += ".%03d" % (t.microsecond / 1000)
        elif precision == 6:
            s += ".%06d" % t.microsecond
        elif precision != 0:
            raise ValueError("Precision should be one of 0, 3 or 6 digits")

        return self.append_pair(tag, s, header=header)
    
    
      def append_utc_timestamp(self, tag, timestamp=None, precision=3,
                             header=False):
          
                  if timestamp is None:
            t = datetime.datetime.utcnow()
        elif type(timestamp) is float:
            t = datetime.datetime.utcfromtimestamp(timestamp)
        else:
            t = timestamp

        s = t.strftime("%Y%m%d-%H:%M:%S")
        if precision == 3:
            s += ".%03d" % (t.microsecond / 1000)
        elif precision == 6:
            s += ".%06d" % t.microsecond
        elif precision != 0:
            raise ValueError("Precision should be one of 0, 3 or 6 digits")

        return self.append_pair(tag, s, header=header)
    
    
       def append_utc_time_only(self, tag, timestamp=None, precision=3,
                             header=False):
           
             if timestamp is None:
            t = datetime.datetime.utcnow()
        elif type(timestamp) is float:
            t = datetime.datetime.utcfromtimestamp(timestamp)
        else:
            t = timestamp

        s = t.strftime("%H:%M:%S")
        if precision == 3:
            s += ".%03u" % (t.microsecond / 1000)
        elif precision == 6:
            s += ".%06u" % t.microsecond
        elif precision != 0:
            raise ValueError("Precision should be one of 0, 3 or 6 digits")

        return self.append_pair(tag, s, header=header)

msg.append_utc_timestamp(52, precision=6, header=True)
msg.append_tz_timestamp(1132, my_datetime)
msg.append_utc_time_only(1495, start_time)
msg.append_tz_time_only(1079, maturity_time)

msg.append_utc_time_only_parts(1495, 7, 0, 0, 0, 0)
msg.append_tz_time_only_parts(1079, 20, 0, 0, offset=-300)


def get(self, tag, nth=1):
      tag = fix_tag(tag)
        nth = int(nth)

        for t, v in self.pairs:
            if t == tag:
                nth -= 1
                if nth == 0:
                    return v

        return None
    
      def remove(self, tag, nth=1):
            tag = fix_tag(tag)
        nth = int(nth)

        for i in range(len(self.pairs)):
            t, v = self.pairs[i]
            if t == tag:
                nth -= 1
                if nth == 0:
                    self.pairs.pop(i)
                    return v

        return None



