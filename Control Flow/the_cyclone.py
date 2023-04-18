height = int(input('Enter height: '))
credits = int(input('Enter credits: '))

if height >= 137 and credits >= 10:
    print('Enjoy the ride!')
elif height < 137:
    print('You are not tall enough to ride.')
else:
    print('You don\'t have enough credits to ride.')
