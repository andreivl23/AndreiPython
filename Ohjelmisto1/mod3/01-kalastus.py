kuha_pituus = input("Kuinka pitkä kuha on?: ")

if int(kuha_pituus) < 37:
    print(f"Laskea kuhan takaisin järveen!\n"
          f"Alimmasta sallitusta pyyntimitasta puuttu {37 - int(kuha_pituus)}")
else:
    print("Kaikki hyvin, kuhan pituus on " + kuha_pituus)