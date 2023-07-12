#!/usr/bin/env python
# coding: utf-8

# In[1]:


strne= input('nhập vào chuỗi ký tự :')


def countstr(txt):
    count = 0
    for char in txt:
        count += 1
    return count

print(' số ký tự trong chủi là: ', countstr(strne))

