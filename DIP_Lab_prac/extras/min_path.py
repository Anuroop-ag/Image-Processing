'''
minimum cost of shortest path

2 8 6
3 5 4
4 3 2
'''
h = 8
###### weights for all possible arcs that can be in min cost path from first row to last row ########
e_2_8_down = a = h - (2-8) 
e_8_6_down = b = h - (8-6)

e_8_5_right= c =  h- (5-8)
e_8_5_left = d = h- (8-5)

e_3_5_down = e = h- (3-5)
e_5_4_down = f = h- (5-4)

e_5_3_right = w =  h- (3-5)
e_5_3_left = x = h- (5-3)

e_4_3_down = y = h- (4-3)
e_3_2_down = z = h- (3-2)



