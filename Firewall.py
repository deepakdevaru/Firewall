import socket
import struct
import nfqueue


class Extract():

    def extract_mac(self,pkt):
        E = Extract()
        dest_addr, src_addr,type= struct.unpack('! 6s 6s H',pct[:14] )
        return E.mac_unpack(dest_addr),E.mac_unpack()

    def mac_unpack(self,data):
        converted_string= B':'.join(["%02X" % (ord(x)) for x in data])
        return converted_string.upper()









class Mainclass:
    connect= socket.socket (socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    pkt =connect.recvfrom(655536) #receive buffer