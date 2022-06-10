import numpy as np
from math import floor

#Function 1
def random_MPS(d, L):
	""" Generate a random MPS, returns a list of M matrices, 
	each M matric is a list of σ matrices
	
	Arguments:
	d -- degrees of freedom for each particle
	L --  number of particles
	"""

	MPS = []
	M_list = []
	sigma = []

	#Here we create the first half of the M matrices
	for l in range(0, floor(L/2)):

		M = []
		sigma_shape = [np.power(d, l), np.power(d, l + 1)]

		for dim in range(0, d):

			M.append(np.random.rand(*sigma_shape))

		M_list.append(M)

	#This handles the case when L is odd, which inserts an extra M in the middle 
	if L % 2 == 1:
		M = []
		sigma_shape = [np.power(d, floor(L/2)), np.power(d, floor(L/2))]

		for dim in range(0, d):

			M.append(np.random.rand(*sigma_shape))
		M_list.append(M)

	#Here we handle the second half of the M matrices
	for l in range(floor(L/2) - 1, -1, -1):

		M = []
		sigma_shape = [np.power(d, l + 1), np.power(d, l)]

		for dim in range(0, d):

			M.append(np.random.rand(*sigma_shape))
			
		M_list.append(M)

	return M_list


#Function 2
def MPS_to_state(mps):
	""" Convert an MPS (A list of M matrices) into a state vector.
	The mps format must be the same as the output of function 1
	"""

	state = []
	recur_matrix_multiply([], mps, state)
	return state 


#Recursive function made for Function 2
def recur_matrix_multiply(bucket, M_list_subset, vector):


	#Base case: We are at the last M matrix
	if len(M_list_subset) == 1:

		#Multiply by every sigma matrix
		for sigma in M_list_subset[0]:

			vector.append(np.trace(np.matmul(bucket,sigma)))
			
	else:

		for sigma in M_list_subset[0]:

			if len(bucket) > 0:
				recur_matrix_multiply(np.matmul(bucket, sigma), M_list_subset[1:], vector)
			else:
				recur_matrix_multiply(sigma, M_list_subset[1:], vector)



#Function 3
def state_to_MPS(state):

	C_matrix = []

	r1 = 

	for 