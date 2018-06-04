# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:17:28 2018

@author: rajan
"""


from data import RAW_DATA_TAGS, RAW_LEN_TAGS


class FixParser(object):
    
     def __init__(self):
         
           # buffer to aculate messages
         self.value = "b"

       self.raw_len_tags = RAW_LEN_TAGS[:]
       
        self.raw_data_tags = RAW_DATA_TAGS[:]
        return

   def add_raw(self, length_tag, value_tag):
         # define tags
       
           self.raw_len_tags.append(length_tag)
        self.raw_data_tags.append(value_tag)
        return

  # remove tags
    def remove_raw(self, length_tag, value_tag):
            self.raw_len_tags.remove(length_tag)
        self.raw_data_tags.remove(value_tag)
        return
    
    
      # reset the state
  def reset(self):
      
        self.value = "b"
        self.pairs = []
        return
    
    
   
      # Append buffer
    def append_buffer(self, buf):
     self.buf += fix_val(buf)
        return


     # return reference to inyernal buffer
       def get_buffer(self):
       return self.buf
    
    
    
    
    def get_message(self):
      #  break buffer into tag value-pairs
      start = 0
        point = 0
        in_tag = True
        raw_len = 0
        tag = 0

        while point < len(self.buf):
            if in_tag and self.buf[point] == EQUALS_BYTE:
                tag_string = self.buf[start:point]
                point += 1

                tag = int(tag_string)
                if tag in self.raw_data_tags and raw_len > 0:
                    if raw_len > len(self.buf) - point:
                        break

                    value = self.buf[point:point + raw_len]
                    self.pairs.append((tag, value))
                    self.buf = self.buf[point + raw_len + 1:]
                    point = 0
                    raw_len = 0
                    start = point

                else:
                    in_tag = False
                    start = point

            elif self.buf[point] == SOH_BYTE:
                value = self.buf[start:point]
                self.pairs.append((tag, value))
                self.buf = self.buf[point + 1:]
                point = 0
                start = point
                in_tag = True

                if tag in self.raw_len_tags:
                    raw_len = int(value)

            point += 1

        if len(self.pairs) == 0:
            return None

      
        # check pair
        while self.pairs and self.pairs[0][0] != 8:
         
            self.pairs.pop(0)

        if len(self.pairs) == 0:
            return None

        # Look for checksum.
        index = 0
        while index < len(self.pairs) and self.pairs[index][0] != 10:
            index += 1

        if index == len(self.pairs):
            return None

        # Found checksum
        m = FixMessage()
        pairs = self.pairs[:index + 1]
        for tag, value in pairs:
            m.append_pair(tag, value)
        self.pairs = self.pairs[index + 1:]

        return m