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


 # message consists oof tag-value pairs
msg = simplefix.FixMessage()

# fix value for string
def fix_val(value):
 if type(value) == bytes:
        return value

    if sys.version_info[0] == 2:
        return bytes(value)
    elif type(value) == str:
        return bytes(value, 'UTF-8')
    else:
        return bytes(str(value), 'ASCII')
    
    
    # fix value for tag
    def fix_tag(value):
         if sys.version_info[0] == 2:
        return bytes(value)
    else:
        if type(value) == bytes:
            return value
        elif type(value) == str:
            return value.encode('ASCII')
        return str(value).encode('ASCII')


# fix message
class FixMessage(object):
    
    
 # fix message getting initialised
def __init__(self):
    print("initialising message")
    
    self.begin_string = '8'
    self.message_type = '35'
    
    
    # return number of pairs
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
    
    
    
    # ADD a field to timestamp
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
    
    
    
    
      # ADD a field to time_only
       def append_utc_time_only(self, tag, timestamp=None, precision=3,
                             header=False):
           
           
           
   # h= hours, m= minutez, s= seconds
     ih = int(h)
        if ih < 0 or ih > 23:
            raise ValueError("Hour value `h` (%u) out of range "
                             "0 to 23" % ih)
        im = int(m)
        if im < 0 or im > 59:
            raise ValueError("Minute value `m` (%u) out of range "
                             "0 to 59" % im)
        isec = int(s)
        if isec < 0 or isec > 60:
            raise ValueError("Seconds value `s` (%u) out of range "
                             "0 to 60" % isec)
        v = "%02u:%02u:%02u" % (ih, im, isec)

        if ms is not None:
            ims = int(ms)
            if ims < 0 or ims > 999:
                raise ValueError("Milliseconds value `ms` (%u) "
                                 "out of range 0 to 999" % ims)
            v += ".%03u" % ims

            if us is not None:
                ius = int(us)
                if ius < 0 or ius > 999:
                    raise ValueError("Microseconds value `us` (%u) "
                                     "out of range 0 to 999" % ius)
                v += "%03u" % ius

        return self.append_pair(tag, v, header=header)



           
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


 # append tag-value pair in string format
  def append_string(self, field, header=False):
      
      
       # split into tag and value
        bits = field.split('=', 1)
        if len(bits) != 2:
            raise ValueError("Field missing '=' separator.")


 # check if tag is integer?
  try:
            tag_int = int(bits[0])
        except ValueError:
            raise ValueError("Tag value must be an integer")

        # Save.
        self.append_pair(tag_int, bits[1], header=header)
        return

      
      
# append raw data
 def append_data(self, len_tag, val_tag, data, header=False):
     
       self.append_pair(len_tag, len(data), header=header)
        self.append_pair(val_tag, data, header=header)
        return

# return nth value for tag
def get(self, tag, nth=1):
      tag = fix_tag(tag)
        nth = int(nth)

        for t, v in self.pairs:
            if t == tag:
                nth -= 1
                if nth == 0:
                    return v

        return None
    
    
    
    # remove nth value for tag
    
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



 # Convert message into correct format (specified)
  def encode(self, raw=False):
     
      buf = "b"
        if raw:
        for tag, value in self.pairs:
                buf += tag + b'=' + value + SOH_STR

            return buf
 
    # When message is not in correct format
    if self.message_type is None:
            raise ValueError("No message type set")

        buf = b"35=" + self.message_type + SOH_STR + buf
    
    
    
    # When message is sequence
    def __getitem__(self, item_index):
     if item_index >= len(self.pairs):
            raise IndexError

        tag, value = self.pairs[item_index]
        return int(tag), value



