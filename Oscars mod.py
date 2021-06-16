from simpleOSC import initOSCClient, initOSCServer, setOSCHandler, sendOSCMsg, closeOSC, \
     createOSCBundle, sendOSCBundle, startOSCServer

    
def myTest():
    """ a simple function that creates the necesary sockets and enters an enless
        loop sending and receiving OSC
    """
    import time # in this example we will have a small delay in the while loop
    
    initOSCClient() # takes args : ip, port
    initOSCServer() # takes args : ip, port, mode --> 0 for basic server, 1 for threading server, 2 for forking server
    
    # bind addresses to functions 
    setOSCHandler('/check', checkcheckcheck)

    startOSCServer() # and now set it into action

    print 'ready to receive and send osc messages ...'

    try:
        while 1:
            sendOSCMsg("/test", [444]) # !! it sends by default to localhost ip "127.0.0.1" and port 9000 

            # create and send a bundle
            bundle = createOSCBundle("/test/bndlprt1")
            bundle.append(666) # 1st message appent to bundle
            bundle.append("the number of the beast") # 2nd message appent to bundle
            sendOSCBundle(bundle) # !! it sends by default to localhost ip "127.0.0.1" and port 9000 

            time.sleep(0.5) # you don't need this, but otherwise we're sending as fast as possible.

    except KeyboardInterrupt:
       print "closing all OSC connections... and exit"
       closeOSC() # finally close the connection before exiting or program.
  
        





""" Below a function dealing with OSC messages RECEIVED into Python.
    Here you can set all the responders you need to deal with the incoming
    OSC messages.
"""

def checkcheckcheck(addr, tags, data, source):
    print "CHECK CHECK CHECK..."
    print "received new osc msg from %s" % getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags :%s" % tags
    print "the actual data is : %s" % data





if __name__ == '__main__': myTest()
