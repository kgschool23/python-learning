# nested loop = A loop within another loop (outer, innter)
                # outer loop:
                #     inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="") # end="" replaces new line (/n) with whatever is in quotes (empty here)
    print() # prints new line


