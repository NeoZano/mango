def user_info(request):
	return {"ip":request.address_string()}