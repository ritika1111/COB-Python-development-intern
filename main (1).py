'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def is_valid_ipv4(ip):
    address = ip.split(".")
    
    # Check if there are exactly 4 parts
    if len(address) != 4:
        return False
    
    # Check if each part is a valid integer between 0 and 255
    for i in address:
        try:
            num = int(i)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    
    return True


ip_address = input("Enter an ip address to validate")
if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
