def compare(number):
    result=True
    i=0  
    while i < len(number)-1:
        num = number[i]
        if num>number[i+1]:
            result = False
            break
        i+=1
    return result


def is_rebote(number):
    result= True
    is_increasing = compare(number)
    is_decreasing = compare(number[::-1])
    if  is_decreasing or is_increasing:
        result = False
    return result


def get_number(param=2000000,percen=99):
    number = 'No number'
    count_reb=0
    for i in range(100,param):
        val = [int(num) for num in str(i)]
        if is_rebote(val):
            count_reb+=1
            avg = (count_reb * 100)/i
            if int(avg) == percen:
                number = f"The number is: {i}"
                break
    print(number)

if __name__ == "__main__":
    get_val = input("Enter The Percentage: ")
    try:
        int(get_val)
        get_number(percen=int(get_val))
    except ValueError:
        print('enter an integer number')
