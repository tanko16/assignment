print("Yusuf and sons")
principal = float(input('enter amount:'))
time = float(input('enter time:'))
rate = float(input('enter rate:'))
simple_interest = (principal*time*rate)/100
compound_interest = principal * ((1+rate/100)**time - 1)
print('simple interest is: %f' %(simple_interest))
print('compound interest is: %f' %(compound_interest))
