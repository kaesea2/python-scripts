import subprocess as sp
import optparse as op

def input():
    parser=op.OptionParser()
    parser.add_option("-i", "--interface", dest=interface, help="use -i or --interface to specify interface")
    parser.add_option("-m", "--mac", dest=macAddr, help="use -m or --mac to specify mac address")
    (inputs,arguements)=parser.parse_args()
    if not inputs.interface:
        print("please specify an interface")
    if not inputs.macAddr:
        print("please enter the mac address you want to change to!")
    return inputs
def changer(iface,mac):
    sp.call(["ifconfig",iface,"down"])
    sp.call(["ifconfig",iface,"hw","ether", mac])
    sp.call(["ifconfig",iface,"up"])
    print("changed successfully")
def newMacchecker(iface):
    ifconfig=sp.check_output(["ifconfig", iface])
    print(ifconfig)
myIface=input().interface
myMac=input().macAddr
changer(myIface,myMac)
newMacchecker(myIface)