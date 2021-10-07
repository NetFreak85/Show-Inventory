#############################################################################
#   Class that help us to store all the information about the Fans Units    #
#   Information that will be stored:                                        #
#       Fan ID                                                              #
#       Fan Description                                                     #
#       Fan Model                                                           #
#       Fan Serial Number                                                   #
#       Fan Vendor                                                          #
#       Fan Operational Status                                              #
#############################################################################

#####################
# Class Declaration #
#####################

class PowerSupply:

    def __init__(self, ID, Description, Model, Serial_Number, Vendor, Fan_Operational_Status, Hardware_Version):
        self.__ID = ID
        self.__Description = Description
        self.__Model = Model
        self.__Serial_Number = Serial_Number
        self.__Vendor = Vendor
        self.__Fan_Operational_Status = Fan_Operational_Status
        self.__Hardware_Version = Hardware_Version

    #########################
    # Attributes Definition #
    #########################

    #FAN ID Number
    __ID = ""

    #FAN Description
    __Description = "" 

    #FAN Model
    __Model = ""

    #FAN Serial Number
    __Serial_Number = ""

    #FAN Vendor
    __Vendor = ""

    #FAN Operational Status
    __Fan_Operational_Status = ""

    #FAN Hardware Version
    __Hardware_Version = ""

    ###############
    # Get Methods #
    ###############

    #Return FAN ID Value
    def getID(self):
        return self.__ID
    
    #Return FAN Description 
    def getDescription(self):
        return self.__Description
    
    #Return FAN Model
    def getModel(self):
        return self.__Model
    
    #Return FAN Serial Number
    def getSerialNumber(self):
        return self.__Serial_Number
    
    #Return FAN Vendor
    def getVendor(self):
        return self.__Vendor
    
    #Return FAN Operational Status
    def getFanOperationalStatus(self):
        return self.__Fan_Operational_Status

    #Return FAN Hardware Version
    def getHardwareVersion(self):
        return self.__Hardware_Version