def check_digit_in_word(substr):
    real_digit=1
    for digit in valid_digits_in_word:
        if digit in substr:
            return real_digit
        real_digit=real_digit+1
    return 0

def find_first_number():
    i=0
    substr=""
    findDigit=False
    digit_converted=0
    while not line[i].isnumeric() and not findDigit:
        substr=substr + line[i]
        digit_converted=check_digit_in_word(substr)
        if (digit_converted != 0):
            findDigit=True
        i=i+1
    if findDigit:
        first_num=str(digit_converted)
    else:
        first_num=line[i]
    return first_num

def find_last_number():
    i=len(line)-1
    substr=""
    digit_converted=0
    findDigit=False
    while not line[i].isnumeric() and not findDigit:
        substr=line[i] + substr
        digit_converted=check_digit_in_word(substr)
        if (digit_converted != 0):
            findDigit=True
        i=i-1
    if findDigit:
        last_num=str(digit_converted)
    else:
        last_num=line[i]
    return last_num


f = open('input.csv', encoding="utf-8")
sum=0
valid_digits_in_word=["one","two","three","four","five","six","seven","eight","nine"]
for line in f:
    first_num=find_first_number()
    last_num=find_last_number()
    number=first_num + last_num
    sum=sum+int(number)
print(sum)
