def litroiksi(gallonit):
    litrat = gallonit * 3.78541
    return litrat
gallonit = 0

while gallonit >= 0:
    gallonit = int(input("Anna gallonit: "))
    litrat = litroiksi(gallonit)
    print(f"{gallonit} gallonaa on {litrat:.2f} litraa bensiiniä")