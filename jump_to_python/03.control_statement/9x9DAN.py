
print(f"{'|GuGuDan|':=^20}\f")
for colum in range(2,10):
    print(f"{'{colum}':-^20}".format(colum=colum))
    for row in range(1,10):
        result = colum * row
        print('{colum} x {row} = {result}'.format(colum=colum, row=row, result=result)) 
    print("\f")    