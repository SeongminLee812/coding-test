# nums = input()

# 내 답안 -> 틀림
# result = 1
# for s in nums:
#     n = int(s)
#     if n > 1:
#         result *= n
#     else:
#         result += n
#
# print(result)


data = input()

# 첫번째 문자를 대입
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if result > 1 and num > 1:
        result *= num
    else:
        result += num

print(result)
