#######################################################################
#   Class that will store all the information about the Fabric Module #
#######################################################################

#####################
# Class Declaration #
#####################

class FabricModule:

    def __init__(self, Description, Hardware_Version, FabricModuleID, mfgTm, modTs, Model, OperStatus, pwrSt, rdSt, SerialNumber, Type, upTs, Vendor):
        self.__Description = Description
        self.__Hardware_Version = Hardware_Version
        self.__FabricModuleID = FabricModuleID
        self.__mfgTm = mfgTm
        self.__modTs = modTs
        self.__Model = Model
        self.__OperStatus = OperStatus
        self.__pwrSt = pwrSt
        self.__rdSt = rdSt
        self.__SerialNumber = SerialNumber
        self.__Type = Type
        self.__upTs = upTs
        self.__Vendor = Vendor

    #Fabric Module Description
    __Description = ""

    #Fabric Module Hardware Version
    __Hardware_Version = ""

    #Fabric Module ID
    __FabricModuleID = ""

    #Fabric Module Manufacturing Time
    __mfgTm = ""

    #Fabric Module last time this object was modified
    __modTs = ""

    #Fabric Module Model
    __Model = ""

    #Fabric Module Operational Status
    __OperStatus = ""

    #Fabric Module Power Status
    __pwrSt = ""

    #Fabric Module HA Status
    __rdSt = ""

    #Fabric Module Serial Number
    __SerialNumber = ""

    #Fabric Module Type
    __Type = ""

    #Fabric Module Uptime
    __upTs = ""

    #Fabric Module Vendor
    __Vendor = ""

    ###############
    # Get Methods #
    ###############

    #Method that return Fabric Module Description
    def getDescription(self):
        return self.__Description
    
    #Method that return Fabric Module Hardware Version
    def getHardwareVersion(self):
        return self.__Hardware_Version

    #Method that return Fabric Module ID
    def getFabricModuleID(self):
        return self.__FabricModuleID

    #Method that return Fabric Module Manufacturing Time
    def getManufacturingTime(self):
        return self.__mfgTm
    
    #Method that return Fabric Module last time modified
    def getLasttimemodified(self):
        return self.__modTs
    
    #Method that return Fabric Module Model
    def getModel(self):
        return self.__Model

    #Method that return Fabric Module Operational Status
    def getOperationalStatus(self):
        return self.__OperStatus

    #Method that return Fabric Module Power Status
    def getPowerStatus(self):
        return self.__pwrSt
    
    #Method that return Fabric Module HA Status
    def getHA_Status(self):
        return self.__rdSt

    #Method that return Fabric Module Serial Number
    def getSerialNumber(self):
        return self.__SerialNumber

    #Method that return Fabric Module Type
    def getType(self):
        return self.__Type

    #Method that return Fabric Module Uptime
    def getFabricModuleUptime(self):
        return self.__upTs

    #Method that return Fabric Module Vendor
    def getVendor(self):
        return self.__Vendor