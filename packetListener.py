import scapy.all as scapy
from scapy_http import http
import optparse as op

def input():
    parser = op.OptionParser()
    parser.add_option("-i", "--interface", dest=interface, help="use -i or --interface to enter interface" )
    (inputs, arguements) = parser.parse_args()
    if not inputs.interface:
        print("enter an interface to begin!")
    return inputs

def listener(listenPort):
    scapy.sniff(iface=listenPort, store=False, prn=analyzer)

def analyzer(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

myinterface = input().interface
listener(myinterface)