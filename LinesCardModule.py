#####################################################################################
#   Class that will store and work with Line Card Module Information on Cisco aci   #
#####################################################################################

##################
# Import Section #
##################

import requests
import json
from LineCard import LineCard

#####################
# Class Declaration #
#####################

class LinesCardModule:

    def __init__(self, ACI_IP, ACI_Cookie, Node_ID):
        self.__ACI_IP_ADDR = ACI_IP
        self.__ACI_Cookie = ACI_Cookie
        self.__Node_ID = Node_ID
        self.__LineCard_List = []
        self.__getLineCardModuleInfo()

    #########################
    # Attributes Definition #
    #########################

    #ACI IP Address
    __ACI_IP_ADDR = ""

    #ACI Cookie for querys
    __ACI_Cookie = ""

    #ACI Node ID
    __Node_ID = ""

    #List that will store all LineCards Info in Objects
    __LineCard_List = []

    ###############
    # Get Methods #
    ###############

    #Get the Fan List
    def getLineCardList(self):
        return self.__LineCard_List
    
    #Return Number of Fan Lists
    def getNumLineCardList(self):
        return len(self.__LineCard_List)

    ###############################################
    # Return Line Cards Attributes based on Index #
    ###############################################

    #Return Line Card ID based on index
    def getID(self, index):
        return self.__LineCard_List[index].getID()

    #Return Line Card Description based on index
    def getDescription(self, index):
        return self.__LineCard_List[index].getDescription()

    #Return Line Card Hardware Version based on index
    def getHardwareVersion(self, index):
        return self.__LineCard_List[index].getHardwareVersion()
    
    #Return Line Card Model based on index
    def getModel(self, index):
        return  self.__LineCard_List[index].getModel()
    
    #Return Line Card Operational Status based on index
    def getOperationalStatus(self, index):
        return self.__LineCard_List[index].getOperationalStatus()
    
    #Return Line Card Power Status based on index
    def getPowerStatus(self, index):
        return self.__LineCard_List[index].getPowerStatus()
    
    #Return Line Card Serial Number based on index
    def getSerialNumber(self, index):
        return self.__LineCard_List[index].getSerialNumber()
    
    #Return Line Card Vendor based on index
    def getVendor(self, index):
        return self.__LineCard_List[index].getVendor()
    
    #Return Line Card Up Time based on index
    def getUpTime(self, index):
        return self.__LineCard_List[index].getUpTime()

    ##########################################################
    # Private Method to request the information in Cisco ACI #
    ##########################################################
    
    def __get_request(self, url):
	    responds = requests.get(url, cookies=self.__ACI_Cookie, verify=False)
	    json_obj = json.loads(responds.content)
	    return json_obj
    
    ######################################
    # Get Line Module Units Information  #
    ######################################

    def __getLineCardModuleInfo(self):
        #URL that will provide all the information about the FANs
        URL = "https://%s/api/node/mo/topology/pod-1/node-%s.json?query-target=subtree&target-subtree-class=eqptLC" % (self.__ACI_IP_ADDR, self.__Node_ID)
 
        #Variable that store all the FANs information in JSON format
        LineCardJson = self.__get_request(URL)

        for i in range(0,int(LineCardJson['totalCount'])):
            #Description, Hardware_Version, Model, Operational_Status, Power_Status, Serial_Number, Vendor, UP_Time):
            self.__LineCard_List.append( LineCard ( LineCardJson['imdata'][i]['eqptLC']['attributes']['id'],
                                                    LineCardJson['imdata'][i]['eqptLC']['attributes']['descr'],
                                                    LineCardJson['imdata'][i]['eqptLC']['attributes']['hwVer'],
                                                    LineCardJson['imdata'][i]['eqptLC']['attributes']['model'],
                                                    LineCardJson['imdata'][i]['eqptLC']['attributes']['operSt'],
                                                    LineCardJson['imdata'][i]['eqptLC']['attributes']['pwrSt'],
                                                    LineCardJson['imdata'][i]['eqptLC']['attributes']['ser'],
                                                    LineCardJson['imdata'][i]['eqptLC']['attributes']['vendor'],
                                                    LineCardJson['imdata'][i]['eqptLC']['attributes']['upTs']))