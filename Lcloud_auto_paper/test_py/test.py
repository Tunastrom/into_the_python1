

test_list = [100, 200, 0, 200]

for i in range(len(test_list)):
    try:                          #start  #end
        print(test_list.index(200,   i,   i+1))
    except:
        continue
