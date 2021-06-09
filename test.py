import pyupbit

access = "MbJxZO51bdhllWH8KaXiObZJYOcouk6pJnivm9fH"          # 본인 값으로 변경
secret = "Kn0u4hM2QhnoxuDbOVjs58edxxJ5SC9acef51QcM"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BCH"))     # KRW-ADA 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회