#
# 
# Copyright 2016 isinstance <super_big_hero@sina.com>/*
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# 
# 
#

#!/usr/bin/env python

import os
import re

filename = '172.16.112.50+result' # input you filename after the draw_1step.py

def cut_the_fir_col():
	cut_fp = open(filename, 'r')
	cut_save = open(filename + '-1', 'a')
	for cut_r in cut_fp.readlines():
		cut_s = cut_r.split(",")
		cut_s.pop(0)
		cut_s.pop(0)
		cut_sw = ",".join(cut_s)
		cut_save.writelines(cut_sw)
	cut_fp.close()
	cut_save.close()


def most_important_way():
	im_fp = open(filename +'-1', 'r')
	im_save = open(filename + '-2', 'a')
	for im_r in im_fp.readlines():
		im_s = im_r.split(",")
		line_0 = im_s[0]
		line_1 = im_s[1]
		h = []
		result_hour = int(line_0) - 1
		result_min = int(line_1)
		fin_result = float(result_hour) + float(result_min) / 60
		most_want = im_s[2]
		h.append(str(fin_result))
		h.append(most_want)
		h_w = ",".join(h)
		im_save.writelines(h_w)
		#im_save.writelines('\n') # keep this
	im_fp.close()
	im_save.close()


def is_same_list(one, b_list):
	for two in b_list:
		if str(one) == str(two):
			return 0
	return 1

def make_same_list():
	fir_use = True
	li_fp = open(filename + '-2', 'r')
	li_save = open('same_list', 'a')
	big = []
	for li_r in li_fp.readlines():
		li_s = li_r.split(",")
		big_guy = li_s[-1]
		if fir_use:
			big.append(big_guy)
			fir_use = False
		
		else:
			joo = is_same_list(big_guy, big)
			if joo == 1:
				#print 'want to write ', big_guy
				big.append(big_guy)
			#li_read_same.close()
	for b in big:
		li_save.writelines(b.strip('\n'))
		li_save.writelines('\n')
	li_fp.close()
	li_save.close()


def return_num(thing):
	num = 1
	sl = open('same_list', 'r')
	for ss in sl.readlines():
		if ss == thing:
			return num
		else:
			num += 1


def replace_event():
	ev_fp = open(filename + '-2', 'r')
	ev_save = open(filename + '-3', 'a')
	
	for ev_r in ev_fp.readlines():
		ev_s = ev_r.split(",")
		event = ev_s[-1]
		ee = []
		num = return_num(event)
		
		ee.append(ev_s[0])
		ee.append(str(num))
		ee_w = ",".join(ee)
		print ev_s[-1], num
		ev_save.writelines(ee_w)
		ev_save.writelines('\n')
	ev_fp.close()
	ev_save.close()


def main():
	cut_the_fir_col()
	most_important_way()
	make_same_list()
	replace_event()

if __name__ == "__main__":
	main()
