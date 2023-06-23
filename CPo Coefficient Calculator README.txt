README




	 		                       __
	 	  	                       __|
	 	  	                       __|
	                                ______
	 	                       /   ___|
	 	                      /  /    '
                                     /  /	              
                                     [ [
                                     | |                  CPO COEFFICIENT CALCULATOR, 2023
                                     [ [                  _   _           _
                                     \  \
                                      \  \ ___,
                                       \______|
                  

					


_______________________________________________________________________________________________________________________________________
CPo Coefficient Calculator (C3) is the Python code found in Bowman et al. (2023) and use of this software must cite this work.
_______________________________________________________________________________________________________________________________________
License: MIT


Contact: sabowman@mix.wvu.edu, or wvu.stableisotopelab@gmail.com


The code is modified from that found in Kong et al. (2020), and is given as:
	import numpy as np
	A = np.array([[1, 400, 160000, 0.05, 0.00000625], [1, 500, 250000, 0.04472136, 0.00000400], [1, 600, 360000, 0.04082483, 0.00000278], [1, 700, 490000, 0.03779645, 0.00000204],[1, 800, 640000, 0.03535534, 0.00000156]])
	y = np.array([120.91, 131.39, 139.01, 146.53, 156.06])
	x = np.linalg.solve(A, y)
	print(x)
	B = np.array([[1, 1000, 1000000, 0.0316227766016838, 0.000001000000000], [1, 1100, 1210000, 0.0301511344577764, 0.000000826446281], [1, 1200, 	1440000, 0.0288675134594813, 0.000000694444444], [1, 1300, 1690000, 0.0277350098112615, 0.000000591715976],[1, 1400, 1960000, 0.0267261241912424, 	0.000000510204082]])
	z = np.array([148.49, 143.55, 140.74, 140.07, 141.42])
	a = np.linalg.solve(B, z)
	print(a)
	col1 = "A"
	col2 = "B"
	data = pd.DataFrame({col1:x,col2:a})
	data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)

Note that bracketed values within A and B arrays are the A matrices consisting of the temperatures for the chosen polynomial form (e.g., 1, T, T**2, T**-0.5, T**-2 per Hemingway (1990)) for 400 to 800 K, and 1000 K to 1400 K, respectively.  Similarly, the bracketed values within the y and z arrays correspond to the b matrices at each respective temperature interval (400 K to 800 K, and 1000 K to 1400 K).  The values within the bracketed A and B arrays will need to be cleared and replaced with the appropriate temperatures.  Similarly, the values within the y and z arrays will also need to be replaced with the corresponding CPo value at the accompanying temperature.  For example, taking the hematite data found in Hemingway (1990) and substituting into the respective B and z arrays, we find that "1000" and "148.49" are a pair, "1100" and "143.55" are a pair and so on.  If the z (or y) array is transposed into a vertical column, its constituents align with those in the B (or A) array.


References:	
Bowman, S., Pathak, A., Agrawal, V., and Sharma, S., 2023, A simple method for obtaining heat capacity coefficients of minerals, American Mineralogist, v. XXX, p. XXX-XXX

Hemingway, B.S., 1990, Thermodynamic properties for bunsenite, NiO, magnetite, Fe3O4, and hematite, Fe2O3, with comments on selected oxygen buffer reactions, American Mineralogist, v. 75, p. 781-790

Kong, Q., Siauw, T., and Bayen, A.M., 2021, Python Programming and Numerical Methods: A Guide for Engineers and Scientists, Academic Press, London, pp. 456


