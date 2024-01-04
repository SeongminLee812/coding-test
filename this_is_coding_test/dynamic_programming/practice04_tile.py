n = int(input())

# Initialize DP table to store previous result
d = [0] * 1001

# Bottom up Dynamic Programming
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i -2]) % 796796


