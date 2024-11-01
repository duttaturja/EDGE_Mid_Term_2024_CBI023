given_list = [] #user given list
prime_number_list = [] #list that will have primes 
#prime finding functions
def display_prime_numbers(list): 
    #loop to get all the elements of the list
    for i in list:
        #checks if element is 1
        if i == 1:
            continue
        is_prime = True #declaring cheker variable
        #loop to get all the integers from 2 to the element
        for j in range(2,i):
            #checking if i is divisible by j or not
            if i%j == 0:
                is_prime = False
        
        #entering primes into the list of prime numbers
        if is_prime:
            prime_number_list.append(i)

n=input("Enter Your list length: ") #user input
n= int(n) #datatype declaration
for i in range(0,n): #loop to get elements of the list
    x = input(f"{i+1}th element: ") #getting user input
    x=int(x) #datatype declaration
    given_list.append(x) #entering primes into the list of prime numbers

display_prime_numbers(given_list) #calling the functions
print(prime_number_list) #showing output