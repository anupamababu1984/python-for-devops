num = int(input("Enter a num: " ))

def revNumber(num):
  reverse = 0
  while num != 0:
    reverse = (reverse*10) + (num%10)
    num = num//10
  return reverse

print("The reverse of the number : " , revNumber(num))  
        
