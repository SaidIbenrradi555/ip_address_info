class IpAddress:
    def __init__(self):
        StrIp=input("Enter A valid Ip Address:")
        StrArray=list(StrIp.split("."))
        self.FirstByte=int(StrArray[0])
        self.SecondeByte=int(StrArray[1])
        self.ThrthByte=int(StrArray[2])
        self.FourtByte=int(StrArray[3])
    def ToBinary(self):
        Byte=[self.FirstByte,self.SecondeByte,self.ThrthByte,self.FourtByte]
        IpbinaryByte=[]
        for k in range(len(Byte)):
            IpbinaryByte.append('{0:08b}'.format(Byte[k]))
        return IpbinaryByte 
    def OutputIpToBinary(self):
        print("Ip Address in binary : ")
        Result=self.ToBinary()
        for i in range(len(Result)):
            if i==3:
                print(Result[i],end="")
            else:
                print(Result[i],end=".")
        print("")
            
    #SubnetMask
    def setSubnetMask(self):
        SubnetMask=[0,0,0,0]
        if self.FirstByte>=1 and self.FirstByte<=126:
            for i in range(len(SubnetMask)-3):
                SubnetMask[i]=255
            print("IP Class A:")
            print("Subnet Mask:"+str(SubnetMask[0])+"."+str(SubnetMask[1])+"."+str(SubnetMask[2])+"."+str(SubnetMask[3]))
        if self.FirstByte>=128 and self.FirstByte<=191:
            for i in range(len(SubnetMask)-2):
                SubnetMask[i]=255
            print("IP Class B:")
            print("Subnet Mask:"+str(SubnetMask[0])+"."+str(SubnetMask[1])+"."+str(SubnetMask[2])+"."+str(SubnetMask[3]))
        if self.FirstByte>=192 and self.FirstByte<=223:
            for i in range(len(SubnetMask)-1):
                SubnetMask[i]=255
            print("IP Class C:")
            print("Subnet Mask:"+str(SubnetMask[0])+"."+str(SubnetMask[1])+"."+str(SubnetMask[2])+"."+str(SubnetMask[3]))    
            
    def MaxNetworksHosts(self):
        if self.FirstByte>=1 and self.FirstByte<=126:
            print("Max of Networks:"+ str(pow(2,7))+"\nMax of Hosts per Net: "+str(pow(2,24)-2))
        if self.FirstByte>=128 and self.FirstByte<=191:
            print("Max of Networks:"+ str(pow(2,14))+"\nMax of Hosts per Net: "+str(pow(2,16)-2))
        if self.FirstByte>=192 and self.FirstByte<=223:
            print("Max of Networks:"+ str(pow(2,21))+"\nMax of Hosts per Net: "+str(pow(2,8)-2))
            
                      
           



