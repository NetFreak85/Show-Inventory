# coding=utf-8
#***********************************************************************************************************************#
#    This check all the Serial Numbers in the Fabric (Cisco Application Centric Infraestructure)                        #
#	    The Script will check every single node in the fabric and will Check                                            #
#           Chassis Serial Number, ID, Model, Status, Vendor, etc.                                                      #
#           Supervisor Serial Numbers, Operational status, Power Status, Supervisor ID, Vendor, etc.                    #
#           Line Cards Serial Numbers, Description, Model, Vendor, Operational Status, etc.                             #
#           Power Supply Serial Numbers, Status, Operational Status, Model, Vendor, etc.                                #
#   --usage:                                                                                                            #
#             ./ShowInv.py                                                                                              #
#         or  python ShowInv.py                                                                                         #
#                                                                                                                       #
# date:  20/09/2021 Created                                                                                             #
#***********************************************************************************************************************#

##################
# Import Section #
##################

import Constant
from Inventory import Inventory

#Main program
if __name__ == '__main__':

    #Generating Inventory variable
    Inventory = Inventory(Constant)

    #Export Cisco ACI Inventory via JSON file
    Inventory.ExportInventoryJsonFormat()