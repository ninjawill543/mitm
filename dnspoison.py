from scapy.all import DNS, DNSQR, IP, send, IPv6, sr, UDP, sniff, DNSRR, sendp, Ether, srp1, ARP


pkts = sniff(count=10,filter="udp dst port 53 host 10.5.1.2 ")

pkts.nsummary()

  