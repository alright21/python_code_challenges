# This function returns an array with all the prime factors of a number
# O(n^2)
def get_prime_factors(n):

    result = []
    while n > 1:

        found = False
        
        for i in range(2, n+1):
            if(not found):
                print(i)
                if n%i==0:
                    result.append(i)
                    n = n//i
                    found=True
                
    return(result)

# take the input
number = int(input("Enter a number: "))

# get the result
print(get_prime_factors(number))

