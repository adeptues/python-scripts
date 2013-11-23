#!/usr/bin/python

import nmap
import optparse

def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] "+tgtHost+"tcp/"+tgtPort+" "+state

def main():
    #command line parser
    parser = optparse.OptionParser('Usage $prog -H '+
                                   '<target host> -p <target port>')
    parser.add_option('-H',
                      dest='tgtHost',type='string',help='Specify target host')
    parser.add_option('-p',dest='tgtPort',type='int',help='Specify target port')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(', ')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost,tgtPort)

if __name__ == '__main__':
    main()

