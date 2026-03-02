#This is just the logic of a firewall on how it works.
#This demonstrates the blocking and allowing process of IP Address's which is the primary goal of a firewall
#--------------------------------------------------------------------------------------------------------------------
import random

def generate_random_ip():
    return f'192.168.10.{random.randint(1, 254)}'

def check_rules(ip_address, firewall_rules):
    for key, value in firewall_rules.items():
        if ip_address == key:
            return value
    return 'Allow'

def main():
    rules = {
        '192.168.10.2' : 'Block',
        '192.168.10.4' : 'Block',
        '192.168.10.6' : 'Block',
        '192.168.10.50' : 'Block',
        '192.168.10.62' : 'Block'
    }
    
    for i in range(10):
        ip = generate_random_ip()
        action = check_rules(ip, rules)
        number = random.randint(0, 100)
        print(f'IP: {ip}, ACTION: {action}, NUMBER: {number}')
    
if __name__ == '__main__':
    main()