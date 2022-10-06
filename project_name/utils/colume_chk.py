
def colume_chk(data01,data02):
    '''
    args: data01,data02 are pandas dataframe
    return: same columns in data01 and data02 and count of columns
    
    '''
    count=0
    list1=[]
    for i in data01.columns:
        if i in data02.columns:
            count+=1
            list1.append(i)   
            print(count, i)
    print(f'\n number of columns in both data sets: {count}')
