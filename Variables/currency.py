cn = int(input("What do you have left in yuan?: "))
jp = int(input("What do you have left in yen?: "))
kr = int(input("What do you have left in won?: "))

cn_to_usd = cn * 0.15
jp_to_usd = jp * 0.0075
kr_to_usd = kr * 0.00076

print(cn_to_usd + jp_to_usd + kr_to_usd)
