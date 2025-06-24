import dns
import dns.resolver
import socket


# Find domain names associated with an IP address
def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]]+result[1]
    except socket.herror:
        return None


def DNSRequest(domain):
    ips = []
    try:
        result = dns.resolver.resolve(domain)
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print("Domain Names: %s" % ReverseDNS(answer.to_text()))
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return []
    return ips


# Iterate over each subdomain in the dictionary and create a full subdomain with that prefix and the perform a DNS request for it. nums is a boolean for checking if you need number prefixes searched too or not.
def SubdomainSearch(domain, dictionary, nums):
    successes = []
    for word in dictionary:
        subdomain = word+"."+domain
        DNSRequest(subdomain)
        if nums:
            for i in range(0, 10):
                s = word+str(i)+"."+domain
                DNSRequest(s)


domain = "google.com"
d = "subdomains.txt"
dictionary = []
# Reading from the file, breaking it into list and doing a doma
with open(d, "r") as f:
    dictionary = f.read().splitlines()
SubdomainSearch(domain, dictionary, True)
