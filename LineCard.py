###################################################################
#   Class that will store all the information about the Line Card #
###################################################################

#####################
# Class Declaration #
#####################

class LineCard:

    def __init__(self, ID, Description, Hardware_Version, Model, Operational_Status, Power_Status, Serial_Number, Vendor, UP_Time):
        self.__ID = ID
        self.__Description = Description
        self.__Hardware_Version = Hardware_Version
        self.__Model = Model
        self.__Operational_Status = Operational_Status
        self.__Power_Status = Power_Status
        self.__Serial_Number = Serial_Number
        self.__Vendor = Vendor
        self.__UP_Time = UP_Time
        
    #########################
    # Attributes Definition #
    #########################

    #Lines Card Module ID
    __ID = ""

    #Lines Card Module Description
    __Description = "" 

    #Lines Card Module Hardware Version
    __Hardware_Version = ""

    #Lines Card Module Model
    __Model = "" 

    #Lines Card Module Operational Status
    __Operational_Status = "" 

    #Lines Card Module Power Status
    __Power_Status = ""

    #Lines Card Module Serial Number
    __Serial_Number = "" 

    #Lines Card Module Vendor
    __Vendor = ""

     #Lines Card Module Up Time
    __UP_Time = ""

    ###############
    # Get Methods #
    ###############

    #Return Line Card ID
    def getID(self):
        return self.__ID

    #Return Line Card Description
    def getDescription(self):
        return self.__Description

    #Return Line Card Hardware Version
    def getHardwareVersion(self):
        return self.__Hardware_Version
    
    #Return Line Card Model
    def getModel(self):
        return self.__Model
    
    #Return Line Card Operational Status
    def getOperationalStatus(self):
        return self.__Operational_Status
    
    #Return Line Card Power Status
    def getPowerStatus(self):
        return self.__Power_Status
    
    #Return Line Card Serial Number
    def getSerialNumber(self):
        return self.__Serial_Number
    
    #Return Line Card Vendor
    def getVendor(self):
        return self.__Vendor
    
    #Return Line Card Up Time
    def getUpTime(self):
        return self.__UP_Time