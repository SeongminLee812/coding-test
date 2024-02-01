# 해설 정답 코드
class Forecast():
    def __init__(self, date, weekday, whether):
        self.date = date
        self.weekday = weekday
        self.whether = whether

    def __repr__(self):
        return " ".join([self.date, self.weekday, self.whether])

n = int(input())
ans = Forecast('2101-12-31', '', '')

for _ in range(n):
    day, weekday, whether = input().split()
    f = Forecast(day, weekday, whether)
    if whether == 'Rain':
        if ans.date > f.date:
            ans = f

print(ans)


# # 시간을 줄여보기 위해 작성한 코드
# n = int(input())
#
# faster = '2101-01-01'
# wkdy = ''
# whe = ''
#
# for _ in range(n):
#     days, weekday, whether = input().split()
#     if whether == 'Rain':
#         y, m, d = days.split('-')
#         prev_y, prev_m, prev_d = faster.split('-')
#         if y < prev_y:
#             faster, wkdy, whe = days, weekday, whether
#         elif y == prev_y:
#             if m < prev_m:
#                 faster, wkdy, whe = days, weekday, whether
#             elif m == prev_m:
#                 if d < prev_d:
#                     faster, wkdy, whe = days, weekday, whether
#
# print(" ".join(map(str, [faster, wkdy, whe])))


# # 기존 읽기 편한 코드
# n = int(input())
#
# days = []
#
# for _ in range(n):
#     day, weekday, whether = input().split()
#     if whether == 'Rain':
#         days.append(day + ' ' + weekday + ' ' + whether)
#
# def sorting(text: str) -> str:
#     days, weekday, whether = text.split()
#     y, m, d = days.split('-')
#     return y, m, d
#
# days.sort(key=sorting)
# print(days[0])