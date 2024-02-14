MAX_VOL = 1000000
MAX_DIM = 150 
MAX_MASS = 20

def sort(width, height, length, mass):
	vol = width*height*length
	tags = []
	weird_package = width >= MAX_DIM or height >= MAX_DIM or length >= MAX_DIM

	if weird_package or vol >= MAX_VOL:
		tags.append('b')

	if mass >= MAX_MASS:
		tags.append('h')

	if not tags:
		return 'STANDARD'
	elif len(tags) == 1:
		return 'SPECIAL'
	else:
		return 'REJECTED'
