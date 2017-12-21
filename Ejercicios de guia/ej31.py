def seg(h,m,s):
	"""Pasa una cantidad de horas minutos y segundos solo a segundos"""
	h1 = h * 3600
	m1 = m * 60
	return h1 + m1 + s
def hora(s):
	"""La inversa de seg"""
	h = 0
	m = 0
	while s>=3600:
		s = s - 3600
		h = h + 1
	while s>=60:
		s = s - 60
		m = m + 1
	return (h, m, s)
	

