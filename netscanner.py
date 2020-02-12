import scapy.all as scapy
import optparse as op

def myInput():
    parseObj=op.OptionParser()
    parseObj.add_option("-i", "--ip", dest="ip_range", help="enter ip address")
    (userInput, arguement) = parseObj.parse_args()
    if not userInput.ip_range:
        print("use -i to enter an ip range to begin scan")
    return userInput

def scanner(ip):
    requestPacket=scapy.ARP(pdst=ip)
    broadcastPacket=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combinedPacket=broadcastPacket/requestPacket
    (answered,unanswered)=scapy.srp(combinedPacket,timeout=1)
    answered.summary()

userIp=myInput()
scanner(userIp.ip_range)