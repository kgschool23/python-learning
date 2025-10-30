# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]
#            start is inclusive, end is exclusive

credit_number = "1234-5678-9012-3456"

# print(credit_number[:4]) # print first four digits
# print(credit_number[5:]) # prints all but first four digits
# print(credit_number[-1]) # prints last number
print(credit_number[::2]) # prints every second character
