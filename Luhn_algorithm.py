#check if card number is valid
def verify_card_number(card_number):
    #getting the odd digits
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
        
    #getting the even digits
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    
    #getting the even digits with conditions
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
        
    #checking if total is divisible by 10   
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

#translating card number digits with the translate method
def main():
    card_number = input('Type your card number:')
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

#checking conditions on verify_card_number function (card number should be divisble by 10)
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()