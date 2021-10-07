#################################################
#   Class that store the Supervisor information #
#   The information that will be storage        #
#       Supervisor ID                           #
#       Supervisor Description                  #
#       Supervisor Operational Status           #
#       Supervisor Serial Number                #
#       Supervisor Vendor                       #
#################################################

#####################
# Class Declaration #
#####################

class Supervisor:
        
    def __init__(self, Supervisor_ID, Description, Operational_Status, PowerStatus, Serial_Number, Vendor, Model, Hardware_Version, UP_Time):
        self.__Supervisor_ID = Supervisor_ID
        self.__Description = Description
        self.__Operational_Status = Operational_Status
        self.__PowerStatus = PowerStatus
        self.__Serial_Number = Serial_Number
        self.__Vendor = Vendor
        self.__Model = Model
        self.__Hardware_Version = Hardware_Version
        self.__UP_Time = UP_Time

    #ACI Supervisor ID
    __Supervisor_ID = ""

    #ACI Supervisor Description
    __Description = ""

    #ACI Supervisor Operational Status
    __Operational_Status = ""

    #ACI Supervisor Power Status
    __PowerStatus = ""

    #ACI Supervisor Serial Number
    __Serial_Number = ""

    #ACI Supervisor Vendor
    __Vendor = ""

    #ACI Supervisor Model
    __Model = ""

    #ACI Supervisor Hardware Version
    __Hardware_Version = ""

    #ACI Supervisor UP Time
    __UP_Time = ""

    ###############
    # Get Methods #
    ###############

    #Return Supervisor ID
    def getSupervisor_ID(self):
        return self.__Supervisor_ID
    
    #Return Supervisor Description
    def getDescription(self):
        return self.__Description

    #Return Supervisor Operational Status
    def getOperational_Status(self):
        return self.__Operational_Status

    #Return Supervisor Power Status
    def getPowerStatus(self):
        return self.__PowerStatus

    #Return Supervisor Serial Number
    def getSerial_Number(self):
        return self.__Serial_Number
    
    #Return Supervisor Vendor
    def getVendor(self):
        return self.__Vendor

    #Return Supervisor Model
    def getModel(self):
        return self.__Model
    
    #Return Supervisor Hardware Version
    def getHardwareVersion(self):
        return self.__Hardware_Version

    #Return Supervisor UP Time
    def getUpTime(self):
        return self.__UP_Time