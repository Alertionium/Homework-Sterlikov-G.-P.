columnNumber=int(input())
answer=""
while columnNumber>0:
    columnNumber -= 1
    ostatok=columnNumber%26
    letter=chr(65+ostatok)
    answer=letter+answer
    columnNumber=columnNumber//26
print(answer)