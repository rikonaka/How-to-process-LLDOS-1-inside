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

filename = 'alert_i' # change you file name here

def finish_all():
	os.remove('result_1')

def split_alert_d():
	dt = open('result_1', 'r')
	save_name =  'result-' + filename
	dt_out = open(save_name, 'a')
	
	for i in dt.readlines():
		d_1 = re.sub(r',,,,,', ',', i)
		d_2 = re.sub(r',,', ',', d_1)
		d_3 = re.sub(r',', ',', d_2)
		d_4 = re.sub(r'  ', '', d_3)
		d_5 = re.sub(r', ', ',', d_4)
		d_6 = re.sub(r' , ', ',', d_5)
		d_7 = re.sub(r' ,', ',', d_6)
		dt_out.writelines(d_7)
		#dt_out.write('\n')
	
	dt.close()
	dt_out.close()
	print 'Finish the d_x module'
	
def split_alert_index():
	#splite the [
	alert_txt = open(filename, 'r')
	alert_save = open('result_1', 'a')
	for i in alert_txt.readlines():
		
		get_2 = re.sub(r'\[\*\*\]', ',', i)
		get_3 = re.sub(r'\]\s\[', '],[', get_2)
		get_4 = re.sub(r'\{', ',', get_3)
		get_5 = re.sub(r'\}', ',', get_4)
		get_6 = re.sub(r'\(', ',', get_5)
		get_7 = re.sub(r'\)', '', get_6)
		get_8 = re.sub(r'\:', ',', get_7)
		get_9 = re.sub(r'\->', ',', get_8)
		get_10 = re.sub(r'\]\s', '],', get_9)
		get_11 = re.sub('\s\s', '', get_10)
		alert_save.writelines(get_11)
		#alert_save.write('\n')
	
	alert_txt.close()
	alert_save.close()
	print 'Finish the init sub'

def main():
	split_alert_index()
	split_alert_d()
	finish_all()
	#just_replace()

if __name__ == '__main__':
	main()
