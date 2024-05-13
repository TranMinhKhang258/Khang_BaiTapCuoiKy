def Cong(a, b):
    sign_a = a // 10**10
    sign_b = b // 10**10
    num_a = a % 10**10
    num_b = b % 10**10
    
    result_num = num_a + num_b
    
    if result_num > 10**10 - 1:  
        return [-1]  
    else:
        if sign_a >= sign_b:  
            result_sign = sign_a
        else:
            result_sign = sign_b
        return result_sign * 10**10 + result_num

a = 1000000001  
b = 2000000002 

print("Kết quả của a + b:", Cong(a, b))
