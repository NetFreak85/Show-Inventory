###########################################################################
#   Class that will store all the information about the System Controller #
###########################################################################

#####################
# Class Declaration #
#####################

class SystemController:

    def __init__(self, Description, Hardware_Version, SystemControllerID, mfgTm, modTs, Model, OperStatus, pwrSt, rdSt, SerialNumber, upTs, Vendor):
        self.__Description = Description
        self.__Hardware_Version = Hardware_Version
        self.__SystemControllerID = SystemControllerID
        self.__mfgTm = mfgTm
        self.__modTs = modTs
        self.__Model = Model
        self.__OperStatus = OperStatus
        self.__pwrSt = pwrSt
        self.__rdSt = rdSt
        self.__SerialNumber = SerialNumber
        self.__upTs = upTs
        self.__Vendor = Vendor

    #########################
    # Attributes Definition #
    #########################

    #Description
    __Description = ""

    #Hardware Version
    __Hardware_Version = ""

    #System Controller ID
    __SystemControllerID = ""

    #Manufacturing Time
    __mfgTm = ""

    #The last time this object was modified
    __modTs = ""

    #System Controller model
    __Model = ""

    #Operational Status
    __OperStatus = ""

    #Power Status
    __pwrSt = ""

    #System Controller HA Status
    __rdSt = ""

    #Serial Number
    __SerialNumber = ""

    #System Controller Uptime
    __upTs = ""

    #Vendor
    __Vendor = ""

    ###############
    # Get Methods #
    ###############

    #Return System Controller Description
    def getDescription(self):
        return self.__Description

    #Return System Controller Hardware Version
    def getHardwareVersion(self):
        return self.__Hardware_Version

    #Return System Controller ID
    def getSystemControllerID(self):
        return self.__SystemControllerID
    
    #Return System Controller manufacturing time
    def getManufacturingTime(self):
        return self.__mfgTm

    #Return System Controller Last time the object was modified
    def getLastTimeModified(self):
        return self.__modTs

    #Return System Controller Model
    def getModel(self):
        return self.__Model

    #Return System Controller Operational Status
    def getOperationalStatus(self):
        return self.__OperStatus
    
    #Return System Controller Power Status
    def getPowerStatus(self):
        return self.__pwrSt
    
    #Return System Controller HA Status
    def getSystemController_HA_Status(self):
        return self.__rdSt

    #Return System Controller Serial Number
    def getSerialNumber(self):
        return self.__SerialNumber

    #Return System Controller Uptime
    def getSystemControllerUptime(self):
        return self.__upTs

    #Return System Controller Vendor Name
    def getVendor(self):
        return self.__Vendor