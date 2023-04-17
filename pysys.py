from pandas import Series
indexnumber = ["bitcoin", "pinetwork", "ethnume", "reple"]
profile = []

profile.append("BTC")
profile.append("PI")
profile.append("ETH")
profile.append("XRP")

s = Series(profile, index=indexnumber)
print(f'{s},{type(s)}')
del profile[0]

print(profile)


print(f'{s}')

greeting = "hello minsu"

print(greeting[0:5])