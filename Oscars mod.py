from simpleOSC import initOSCClient, initOSCServer, setOSCHandler, sendOSCMsg, closeOSC, \
     createOSCBundle, sendOSCBundle, startOSCServer
import time

initOSCClient()

while True:
     sendOSCMsg("/test", [444])
     time.sleep(0.5)

                                                             # create and send a bundle
            # bundle = createOSCBundle("/test/bndlprt1")
            # bundle.append(666)                             # 1st message appent to bundle
            # bundle.append("the number of the beast")       # 2nd message appent to bundle
            # sendOSCBundle(bundle)                          # !! it sends by default to localhost ip "127.0.0.1" and port 9000
            # closeOSC() # finally close the connection before exiting or program.



            # if __name__ == '__main__': myTest()
