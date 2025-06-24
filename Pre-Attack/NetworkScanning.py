from scapy.all import *

# Limit ports we are searching for. We are not performing a full port scan
ports = [25,80,53,443,445,8080,8443]

# Simple Syn Scan performing the first step of a handshake and wait for the ACK response. The handshake is not completed which might help evade detection.
def SynScan(host):
  # Packets are either answered or not. We define the packets we want. 
  ans, unans = sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags="S"),timeout=2,verbose=0)
  print("Open ports at %s:" %host)
  for (s,r,) in ans:
    if s[TCP].dport == r[TCP].sport:
      print(s[TCP].dport)

# 
def DNSScan(host):
  # We use UDP since DNS is often using UDP.
  ans, unans = sr(IP(dst=host)/UDP(sport=5555,dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2,verbose=0)
  if ans:
    print("DNS Servre at %s"%host)

host = "8.8.8.8"

SynScan(host)
DNSScan(host)