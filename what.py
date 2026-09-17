num=int(input("Enter a  number of elements:")) 
reverse = int(str(num)[::-1])
if num == reverse:
    print("pallindrome")
else:
    print("not a pallindrome")