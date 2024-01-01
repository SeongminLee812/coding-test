# data = input()
#
# group = {0:0, 1:0}
#
# for i in range(1, len(data)):
#     if data[i] == data[i-1]:
#         pass
#     else:
#         if data[i-1] == '0':
#             group[0] += 1
#         else:
#             group[1] += 1
#     if i == len(data) - 1:
#         if data[i] == '0':
#             group[0] += 1
#         else:
#             group[1] += 1
#
# result = min(group.values())
#
# print(result)


# 교재 답안
data = input()
count0 = 0 # 전부 0으로 바뀌는 경우
count1 = 0 # 전부 1로 바뀌는 경우

# 첫번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 확인해가며 처리
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

result = min(count0, count1)
print(result)