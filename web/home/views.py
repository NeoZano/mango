from lib.html_file import render
from lib.user_info import user_info
def home(request):
	b = user_info(request)["ip"]
	return render("home/index.html", locals())
