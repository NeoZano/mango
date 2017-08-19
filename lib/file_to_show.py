from pathlib import Path
from lib.error import page_missing as qoq

import re
import os



def show_page(file):
	if os.path.splitext(file)[1] == ".css":
		if os.path.exists("web/static/css/"+file):
			return [open("web/static/css/"+file, "r").read(),"text/css"]
		else:
			return [qoq(),"text/html"]
	elif os.path.splitext(file)[1] == '.html':
		if os.path.exists("web/"+file):
			return [open("web/"+file,"r").read(),"text/html"]
		else:
			return [qoq(),"text/html"]
	elif os.path.splitext(file)[1] == '.js':
		if os.path.exists("web/static/js/"+file):
			return [open("web/static/js/"+file,"r").read(),"text/html"]
		else:
			return [qoq(),"text/html"]
	else:
		return [qoq(),"text/html"]