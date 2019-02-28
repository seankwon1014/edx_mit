
##### Week 2: Simple Programs   3. Simple Algorithms (TIME: 41:06)   Exercise: guess my number

low = 0
high = 100
ans = (low + high) / 2
res = ''

print("Please think of a number between 0 and 100!")
while res != 'c':
    print("Is your secret number " + str(ans) + "?")
    res = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if res == 'l':
        low = ans
        ans = int((low + high) / 2)
    elif res ==  'h':
        high = ans
        ans = int((low + high) / 2)
    elif res == 'c':
        print("Game over. Your secret number was: " + str(ans))
        break
    else:
        print("Sorry, I did not understand your input.")


##### Week 2: Simple Programs   3. Simple Algorithms (TIME: 41:06)   Video: Floats and Fractions

num = 11
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ' '
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
if isNeg:
    result = '-' + result
result


##### Week 2: Simple Programs   4. Functions (TIME: 1:08:06)   Exercise: power iter
def iterPower(base, exp):
    ans = 1
    for i in range(exp):
        ans *= base
    return ans

##### Week 2: Simple Programs   4. Functions (TIME: 1:08:06)   Exercise: power recur
def recurPower(base, exp):
    # Your code here
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

recurPower(3,4)
recurPower(6.26, 0)

iterPower(3,3)
iterPower(4.59, 0)

##### Week 2: Simple Programs   4. Functions (TIME: 1:08:06)   Exercise: gcd iter
def gcdIter(a, b):
    if a > b:
        for i in range(1, a+1):
            if a % i == 0 and b % i == 0:
                ans = i
    else:
        for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            ans = i
     return ans

##### Week 2: Simple Programs   4. Functions (TIME: 1:08:06)   Exercise: gcd recur
def gcdRecur(a, b):
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)

gcdRecur(24,16)

#### Video: Recursion on non-numerics
def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
                return ans
    def ispal (s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and ispal(s[1:-1])
    return isPal(toChars(s))


##### Week 2: Simple Programs   4. Functions (TIME: 1:08:06)   Exercise: is in
def isIn(char, aStr):
    if aStr == '':
        return False
    else:
        ans = aStr[int(len(aStr)/2)]
        if char == ans:
            return True
        elif len(aStr) <= 1 or aStr == '':
            return False
        elif char < ans:
            return isIn(char, aStr[0:int(len(aStr)/2)])
        else:
            return isIn(char, aStr[int(len(aStr)/2):])

isIn('d','abcdef')


##### Week 2: Simple Programs   Complete Programming Experience: polysum   Grader
import math
def polysum(n, s):
    area = 0.25 * n * (s**2) / math.tan(math.pi / n)
    sqr = (n * s) ** 2
    sum = round(area + sqr, 4)
    return sum


##### Week 2: Simple Programs   Problem Set 2   Problem 1
def interest(balance, annualInterestRate, monthlyPaymentRate):
    for month in range(12):
        r_blc = balance - (balance * monthlyPaymentRate)
        balance = r_blc + (r_blc * annualInterestRate / 12)
    return round(balance,2)
print(interest(balance, annualInterestRate, monthlyPaymentRate))

interest(484, 0.2, 0.04)


##### Week 2: Simple Programs   Problem Set 2   Problem 2
def lowest(balance, annualInterestRate):
    ans = 0
    r_blc = balance
    while r_blc > 0:
        ans += 10
        r_blc = balance
        for month in range(12):
            r_blc = r_blc - ans
            r_blc = r_blc + (r_blc * annualInterestRate / 12)
    return ans
print(lowest(balance,annualInterestRate))


##### Week 2: Simple Programs   Problem Set 2   Problem 3
def bi(balance, annualInterestRate):
    l_bound = round(balance / 12, 2)
    h_bound = round((balance * (1+annualInterestRate)**12) / 12,2)
    ans = round((l_bound + h_bound) / 2, 2)
    r_blc = balance
    while round(r_blc) !=0 or r_blc > 0:
        r_blc = balance
        for month in range(12):
            c_blc = round(r_blc - ans,2)
            r_blc = round(c_blc + round((c_blc * annualInterestRate / 12),2),2)
        #     print("c_blc: " + str(c_blc))
        # print("ans: " + str(ans))
        # print("l_bound: " + str(l_bound))
        # print("h_bound: " + str(h_bound))
        if c_blc > 0:
            l_bound = ans
            ans = round((l_bound + h_bound) / 2, 2)
        elif c_blc < 0:
            h_bound = ans
            ans = round((l_bound + h_bound) / 2, 2)
    return ans
print(bi(balance, annualInterestRate))


