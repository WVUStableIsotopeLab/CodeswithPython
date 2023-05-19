import numpy as np 

A = np.array([[1, 400, 160000, 0.05, 0.00000625], [1, 500, 250000, 0.04472136, 0.00000400], [1, 600, 360000, 0.04082483, 0.00000278], [1, 700, 490000, 0.03779645, 0.00000204],[1, 800, 640000, 0.03535534, 0.00000156]]) 

y = np.array([120.91, 131.39, 139.01, 146.53, 156.06]) 

x = np.linalg.solve(A, y) 

print(x) 

B = np.array([[1, 1000, 1000000, 0.0316227766016838, 0.000001000000000], [1, 1100, 1210000, 0.0301511344577764, 0.000000826446281], [1, 1200, 1440000, 0.0288675134594813, 0.000000694444444], [1, 1300, 1690000, 0.0277350098112615, 0.000000591715976],[1, 1400, 1960000, 0.0267261241912424, 0.000000510204082]]) 

z = np.array([148.49, 143.55, 140.74, 140.07, 141.42]) 

a = np.linalg.solve(B, z) 

print(a) 

col1 = "A" 

col2 = "B" 

data = pd.DataFrame({col1:x,col2:a}) 

data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False) 
