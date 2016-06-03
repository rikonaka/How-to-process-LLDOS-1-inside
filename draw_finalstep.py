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

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd


filename = '172.16.112.50+result-3'
title_name = '172.16.112.50'


def scatter_x():
	col_name = ['1','2']
	li = ['0']
	get_list = open('same_list', 'r')
	for g in get_list.readlines():
		li.append(g)
	data = pd.read_csv(filename, names=col_name)
	
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.scatter(x=data['1'], y=data['2'], alpha=0.5)
	ax.set_title(title_name)
	
	ax.set_xticks([9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5])
	ax.set_xticklabels(['09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30'])
	ax.set_xlabel('time/hour')
	
	ax.set_yticks(xrange(0, 16, 1))
	ax.set_yticklabels(li)
	#ax.set_yticklabels(['0', 'http_inspect NO CONTENT LENGTH OR TRANSFER ENCODING IN HTTP RESPONSE', 'spp_sdf SDF Combination Alert', 'SERVER ORACLE describe attempt', 'INDICATOR COMPROMISE 403 Forbidden', 'BROWSER OTHER HTTP characters prior to header evasion attempt', 'SERVER MAIL Metamail header length exploit attempt', 'SENSITIVE DATA Email Addresses', 'POLICY OTHER Remote non JavaScript file found in script tag src attribute', 'PROTOCOL ICMP Unusual PING detected', 'PROTOCOL ICMP PING', 'http_inspect SIMPLE REQUEST', 'BROWSER IE Microsoft Internet Explorer long URL buffer overflow attempt', 'PROTOCOL ICMP PING BSDtype', 'PROTOCOL ICMP PING Unix', 'POLICY OTHER FTP anonymous login attempt', 'http_inspect INVALID CONTENT LENGTH OR CHUNK SIZE', 'http_inspect UNKNOWN METHOD', 'SERVER WEBAPP redirect access', 'http_inspect UNESCAPED SPACE IN HTTP URI', 'SERVER WEBAPP Checkpoint Firewall 1 HTTP parsing format string vulnerability attempt', 'PROTOCOL ICMP Echo Reply'])
	ax.set_ylabel('Snort Label')
	plt.show()


def hist_x():
	col_name = ['1','2']
	#mu = 100
	#sigma = 15
	num_bins = 80
	li = ['0']
	get_list = open('same_list', 'r')
	for g in get_list.readlines():
		li.append(g)
	
	data = pd.read_csv(filename, names=col_name)
	#data.plot(kind='bar', stacked=True)
	#data['1'].hist(bins=60, alpha=0.3, color='k', normed=True)
	#data['1'].plot(kind='kde',style='k--')
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.hist(data['1'],num_bins,facecolor='green',alpha=0.5)
	#ax.hist(data['1'],num_bins,facecolor='green',alpha=0.5,orientation='horizontal')
	#ax.set_ylabel('Snort Label')
	ax.set_xlabel('Time/hour')
	ax.set_xticks([9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5])
	ax.set_xticklabels(['09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30'])
	#ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
	#ax.set_xticklabels(['20:00','21:00','22:00','23:00','24:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00'])
	
	ax.set_title('Count Snort of Label')
	#ax.set_yticks(xrange(0, 52, 1))
	#ax.set_yticklabels(li)
	#ax.set_yticklabels(['0','spp_sdf SDF Combination Alert','SENSITIVE DATA Email Addresses','3','http_inspect INVALID CONTENT LENGTH OR CHUNK SIZE','http_inspect NO CONTENT LENGTH OR TRANSFER ENCODING IN HTTP RESPONSE','6','7','Consecutive TCP small segments exceeding threshold','9','10','11','spp_ssh Protocol mismatch','13','14'])
	#ax.set_yticklabels(['0','spp_sdf SDF Combination Alert','SENSITIVE DATA Email Addresses','spp_gtp Message length is invalid','http_inspect INVALID CONTENT LENGTH OR CHUNK SIZE','http_inspect NO CONTENT LENGTH OR TRANSFER ENCODING IN HTTP RESPONSE','http_inspect JAVASCRIPT WHITESPACES EXCEEDS MAX ALLOWED','http_inspect UNESCAPED SPACE IN HTTP URI','Consecutive TCP small segments exceeding threshold','http_inspect SIMPLE REQUEST','IPV4 packet to current net dest address','http_inspect UNKNOWN METHOD','spp_ssh Protocol mismatch','http_inspect LONG HEADER','Reset outside window'])
	
	#ax.set_title('Count Snort of Time')
	#n, bins, patches= plt.hist(data['1'],num_bins,facecolor='green',alpha=0.5)
	#y = mlab.normpdf(bins, mu, sigma)
	#plt.plot(bins, y, 'r--')
	#plt.xlabel('Time')
	#plt.ylabel('High')
	#plt.title('Count of all')
	
	#mu = 100  # mean of distribution
	#sigma = 15  # standard deviation of distribution
	#x = mu + sigma * np.random.randn(10000)
	#num_bins = 50
	# the histogram of the data
	#n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
	# add a 'best fit' line
	#y = mlab.normpdf(bins, mu, sigma)
	#plt.plot(bins, y, 'r--')
	#plt.xlabel('Smarts')
	#plt.ylabel('Probability')
	#plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

	# Tweak spacing to prevent clipping of ylabel
	#plt.subplots_adjust(left=0.15)
	
	
	plt.show()


def hist2d_x():
	col_name = ['1','2']
	li = ['0']
	get_list = open('same_list', 'r')
	for g in get_list.readlines():
		li.append(g)
	data = pd.read_csv(filename, names=col_name)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.hist2d(x=data['1'], y=data['2'], bins=50, normed=True)
	
	ax.set_title(title_name)
	ax.set_xticks([9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5])
	ax.set_xticklabels(['09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30'])
	ax.set_xlabel('time/hour')
	
	ax.set_yticks(xrange(0, 16, 1))
	ax.set_yticklabels(li)
	#ax.set_yticklabels(['0', 'http_inspect NO CONTENT LENGTH OR TRANSFER ENCODING IN HTTP RESPONSE', 'spp_sdf SDF Combination Alert', 'SERVER ORACLE describe attempt', 'INDICATOR COMPROMISE 403 Forbidden', 'BROWSER OTHER HTTP characters prior to header evasion attempt', 'SERVER MAIL Metamail header length exploit attempt', 'SENSITIVE DATA Email Addresses', 'POLICY OTHER Remote non JavaScript file found in script tag src attribute', 'PROTOCOL ICMP Unusual PING detected', 'PROTOCOL ICMP PING', 'http_inspect SIMPLE REQUEST', 'BROWSER IE Microsoft Internet Explorer long URL buffer overflow attempt', 'PROTOCOL ICMP PING BSDtype', 'PROTOCOL ICMP PING Unix', 'POLICY OTHER FTP anonymous login attempt', 'http_inspect INVALID CONTENT LENGTH OR CHUNK SIZE', 'http_inspect UNKNOWN METHOD', 'SERVER WEBAPP redirect access', 'http_inspect UNESCAPED SPACE IN HTTP URI', 'SERVER WEBAPP Checkpoint Firewall 1 HTTP parsing format string vulnerability attempt', 'PROTOCOL ICMP Echo Reply'])
	ax.set_ylabel('Snort Label')
	plt.show()


def main():
	#scatter_x() # Notice here, remove the # if you want to draw the type picture
	#hist_x()
	#hist2d_x()

if __name__ == "__main__":
	main()
