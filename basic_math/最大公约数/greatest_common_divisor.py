'''
Author       : Zhu Honglin
Date         : 2020-09-11 16:05:59
LastEditTime : 2020-09-11 17:41:28
'''

def old_gcd(a, b):
    if a < b:
        return old_gcd(b, a)
    
    if a % b == 0:
        return b
    else:
        return old_gcd(b, a % b)
    

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    test_case = [
        [12, 5],
        [434, 32],
        [1, 2],
        [9, 3],
    ]

    for item in test_case:
        rst = old_gcd(item[0], item[1])
        print(f'{item[0]} and {item[1]}: {rst}')