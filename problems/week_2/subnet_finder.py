import ipaddress


def main():
    # Test cases
    print(find_subnet('192.168.10.1', '255.255.255.0'))
    print(find_subnet('10.10.1.1', '255.255.0.0'))
    print(find_subnet('172.16.2.35', '255.255.255.248'))


def find_subnet(ip_add: str, mask: str) -> str:
    ''' Returns the network address for a given IP address and mask
    - ip_add: IP address
    - mask: Subnet mask '''
    
    interface = f"{ip_add}/{mask}"                      # Joins the interface parts
    interface_obj = ipaddress.ip_interface(interface)   # Creates an interface object
    network_add = interface_obj.network                 # Finds the network address
    return str(network_add).split('/')[0]               # Strips off the CIDR notation


if __name__ == "__main__":
    main()