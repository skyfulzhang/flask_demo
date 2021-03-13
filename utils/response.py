def response_200(data=None):
	res_data = {
		"code": 200,
		"message": None,
		"data": data
	}
	return res_data


def response_400(msg=None):
	res_data = {
		"code": 400,
		"message": str(msg),
		"data": None
	}
	return res_data


def response_500():
	res_data = {
		"code": 500,
		"message": "Internal Server Error",
		"data": None
	}
	return res_data
