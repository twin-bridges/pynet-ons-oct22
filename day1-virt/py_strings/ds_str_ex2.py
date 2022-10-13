
#User inputs IP address
ip_address = input('Please enter an IP address: ')

#creating an octet after every period.
octets = ip_address.split('.')

print()
print(f"{octets[0]:<12}{octets[1]:<12}{octets[2]:<12}{octets[3]:<12}")
print()