# Copyright (c) 2006, Neville-Neil Consulting
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of Neville-Neil Consulting nor the names of its 
# contributors may be used to endorse or promote products derived from 
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# File: $Id: snarf.py,v 1.1 2006/07/13 10:05:40 gnn Exp $
#
# Author: George V. Neville-Neil
#
# Description: A quick and dirty packet snooper that demo's the power of PCS

import pcs
from pcs.packets.ethernet import ethernet

def main():

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-i", "--interface",
                      dest="interface", default=None,
                      help="Which interface to snarf from.")
    
    (options, args) = parser.parse_args()

    snarf = pcs.PcapConnector(options.interface)

    while 1:
        packet = ethernet(snarf.read())
        print packet
        print packet.data
        
main()
