pH = int(input('Enter pH: '))

if pH < 0 or pH > 14:
    input('Invalid pH ')

if pH > 7:
    print('Basic')
elif pH < 7:
    print('Acidic')
else:
    print('Neutral')
