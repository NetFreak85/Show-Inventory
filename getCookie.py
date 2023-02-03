# coding=utf-8
import requests
import urllib3
urllib3.disable_warnings()

#Method to request tokens to the Cisco APICs
def get_cookie(ip, user, passwd, Token_url):
	try:
		#URL that help with the token generation
		auth_url = Token_url % ip

		#Payload
		auth_xml = "<aaaUser name='%s' pwd ='%s'/>" % (user, passwd)
		
		#Post Method to retrieve the token from APICs
		session = requests.post(auth_url, data=auth_xml, verify=False, timeout=8)
		
		# If Username or password are incorrect the script stop with exit code 1
		if session.status_code != 200:
			print ("ERROR: Username/Password incorrect")
			exit(1)
		return session.cookies
	except requests.exceptions.Timeout:
		return 1
	except requests.exceptions.ConnectionError:
		raise Exception("Connection error can't logging to APIC %s with user %s" % (ip, user))