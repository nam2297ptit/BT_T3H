result = []
for a in range(1,50):
    for b in range(1,50):
        for c in range(1,50):
            if  c * a + b == 10 * c:
                result.append([a, b, c])
print(result)


'''
[[1, 9, 1], [1, 18, 2], [1, 27, 3], [1, 36, 4], [1, 45, 5], [2, 8, 1], [2, 16, 2], 
[2, 24, 3], [2, 32, 4], [2, 40, 5], [2, 48, 6], [3, 7, 1], [3, 14, 2], [3, 21, 3], 
[3, 28, 4], [3, 35, 5], [3, 42, 6], [3, 49, 7], [4, 6, 1], [4, 12, 2], [4, 18, 3], 
[4, 24, 4], [4, 30, 5], [4, 36, 6], [4, 42, 7], [4, 48, 8], [5, 5, 1], [5, 10, 2], 
[5, 15, 3], [5, 20, 4], [5, 25, 5], [5, 30, 6], [5, 35, 7], [5, 40, 8], [5, 45, 9], 
[6, 4, 1], [6, 8, 2], [6, 12, 3], [6, 16, 4], [6, 20, 5], [6, 24, 6], [6, 28, 7], 
[6, 32, 8], [6, 36, 9], [6, 40, 10], [6, 44, 11], [6, 48, 12], [7, 3, 1], [7, 6, 2], 
[7, 9, 3], [7, 12, 4], [7, 15, 5], [7, 18, 6], [7, 21, 7], [7, 24, 8], [7, 27, 9], 
[7, 30, 10], [7, 33, 11], [7, 36, 12], [7, 39, 13], [7, 42, 14], [7, 45, 15], [7, 48, 16],
[8, 2, 1], [8, 4, 2], [8, 6, 3], [8, 8, 4], [8, 10, 5], [8, 12, 6], [8, 14, 7], [8, 16, 8],
[8, 18, 9], [8, 20, 10], [8, 22, 11], [8, 24, 12], [8, 26, 13], [8, 28, 14], [8, 30, 15],
[8, 32, 16], [8, 34, 17], [8, 36, 18], [8, 38, 19], [8, 40, 20], [8, 42, 21], [8, 44, 22],
[8, 46, 23], [8, 48, 24], [9, 1, 1], [9, 2, 2], [9, 3, 3], [9, 4, 4], [9, 5, 5], [9, 6, 6], 
[9, 7, 7], [9, 8, 8], [9, 9, 9], [9, 10, 10], [9, 11, 11], [9, 12, 12], [9, 13, 13],
[9, 14, 14], [9, 15, 15], [9, 16, 16], [9, 17, 17], [9, 18, 18], [9, 19, 19], [9, 20, 20],
[9, 21, 21], [9, 22, 22], [9, 23, 23], [9, 24, 24], [9, 25, 25], [9, 26, 26], [9, 27, 27],
[9, 28, 28], [9, 29, 29], [9, 30, 30], [9, 31, 31], [9, 32, 32], [9, 33, 33], [9, 34, 34],
[9, 35, 35], [9, 36, 36], [9, 37, 37], [9, 38, 38], [9, 39, 39], [9, 40, 40], [9, 41, 41],
[9, 42, 42], [9, 43, 43], [9, 44, 44], [9, 45, 45], [9, 46, 46], [9, 47, 47], [9, 48, 48],
[9, 49, 49]]
'''
