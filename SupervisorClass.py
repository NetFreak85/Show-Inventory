#############################################################################################
#   Class that will storage and print information about the supervisors in the Cisco ACI    #
#############################################################################################

##################
# Import Section #
##################

import requests
import json
from Supervisor import Supervisor

#####################
# Class Declaration #
#####################

class SupervisorClass:

    def __init__(self, ACI_IP, ACI_Cookie, Node_ID):
        self.__ACI_IP_ADDR = ACI_IP
        self.__ACI_Cookie = ACI_Cookie
        self.__Node_ID = Node_ID
        self.__Internal_Supervisor_List = []
        self.__getSupervisorInfo()
    
    #########################
    # Attributes Definition #
    #########################
    
    #ACI IP Address
    __ACI_IP_ADDR = ""

    #ACI Cookie for querys
    __ACI_Cookie = ""

    #ACI Node ID
    __Node_ID = ""

    #Supervisor List
    __Internal_Supervisor_List = []

    ####################################
    # Return Supervisor based on Index #
    ####################################

    #Return Internal Supervisor List
    def getSupervisorList(self):
        return self.__Internal_Supervisor_List

    #Return Number of Supervisors
    def getNumSupervisors(self):
        return len(self.__Internal_Supervisor_List)

    #Return Supervisor ID
    def getSupervisor_ID(self, index):
        return self.__Internal_Supervisor_List[index].getSupervisor_ID()
    
    #Return Supervisor Description
    def getDescription(self, index):
        return self.__Internal_Supervisor_List[index].getDescription()

    #Return Supervisor Operational Status
    def getOperational_Status(self, index):
        return self.__Internal_Supervisor_List[index].getOperational_Status()

    #Return Supervisor Power Status
    def getPowerStatus(self, index):
        return self.__Internal_Supervisor_List[index].getPowerStatus()

    #Return Supervisor Serial Number
    def getSerial_Number(self, index):
        return self.__Internal_Supervisor_List[index].getSerial_Number()
    
    #Return Supervisor Vendor
    def getVendor(self, index):
        return self.__Internal_Supervisor_List[index].getVendor()
    
    #Return Supervisor Model
    def getModel(self, index):
        return self.__Internal_Supervisor_List[index].getModel()

    #Return Supervisor UP Time
    def getUpTime(self, index):
        return self.__Internal_Supervisor_List[index].getUpTime()
    
    #Return Supervisor Hardware Version
    def getHardwareVersion(self, index):
        return self.__Internal_Supervisor_List[index].getHardwareVersion()


    ##########################################################
    # Private Method to request the information in Cisco ACI #
    ##########################################################
    
    def __get_request(self, url):
	    responds = requests.get(url, cookies=self.__ACI_Cookie, verify=False)
	    json_obj = json.loads(responds.content)
	    return json_obj

    ###############################
    # Get Supervisors Information #
    ###############################

    def __getSupervisorInfo(self):
        #URL that will provide all the information about the FANs
        URL = "https://%s/api/node/mo/topology/pod-1/node-%s.json?query-target=subtree&target-subtree-class=eqptSupC" % (self.__ACI_IP_ADDR, self.__Node_ID)

        #Variable that store all the FANs information in JSON format
        SUPERVISOR_INFO = self.__get_request(URL)

        #Object creation with for loop
        for i in range(0,int(SUPERVISOR_INFO['totalCount'])):
            self.__Internal_Supervisor_List.append( Supervisor ( SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['id'], 
                                                                 SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['descr'], 
                                                                 SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['operSt'],
                                                                 SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['pwrSt'],
                                                                 SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['ser'],
                                                                 SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['vendor'],
                                                                 SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['model'],
                                                                 SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['hwVer'],
                                                                 SUPERVISOR_INFO['imdata'][i]['eqptSupC']['attributes']['upTs']))