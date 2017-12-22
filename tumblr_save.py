#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import urllib
from bs4 import BeautifulSoup

def NextPage(soup):
	nav = soup.find('div').find_all('a')
	for link in nav:
		if link.string == 'next':
			return True
	return False
	


# --- MAIN ----------------------------------------------------------------------------------------
def save_from_tumblr():


	tumblr_name = raw_input("Nome do Tumblr: ")
	img_format = ".jpg"
	folder = tumblr_name
	if not os.path.isdir(folder):
		os.makedirs(folder)


	img_count = 0
	page_count = 1

	while(True): 

		url = "http://" + tumblr_name + ".tumblr.com/mobile/page/" + str(page_count)

		print ">> Requisitando página {}...".format(page_count)
		html_code = urllib.urlopen(url).read()
		html_code = str(html_code)

		soup = BeautifulSoup(html_code, 'html.parser')

		for a in soup.find_all('a'):
			if a['href'].endswith(img_format):
				print "Salvando imagem: " + str(img_count) + img_format + " da página {}.".format(page_count) 
				urllib.urlretrieve(a['href'], folder + '/' + str(img_count) + img_format)
				img_count = img_count + 1

		if NextPage(soup):
			page_count = page_count + 1
		else:
			print "Fim do blog. Total de páginas: {}".format(page_count)
			break

	alarm()	

# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    save_from_tumblr()