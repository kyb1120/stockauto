import pyupbit

access = "MbJxZO51bdhllWH8KaXiObZJYOcouk6pJnivm9fH"          
secret = "Kn0u4hM2QhnoxuDbOVjs58edxxJ5SC9acef51QcM"        
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ADA"))     # KRW-ADA 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
