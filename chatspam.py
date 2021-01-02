import amino
import getpass
import os
print("\033[1;36m Amino :  \033[1;34mSirLez \n \n \033[1;36minsta : \033[1;34m SirLe0x \n \n \n")
client=amino.Client()
ss=0
sz=25
nuum=0
tst=False
while tst==False:
	try:
		email=input("\033[1;31m\n# ur Email :\033[1;0m ")
		password=input("\033[1;31m# ur Password :\033[1;0m ")
		client.login(email=email,password=password)
		tst=True
	except:
		tst=False
		print("\n\033[1;33m# Verify ur account! \n")
		exx=input("# continue? \033[1;32m y/n : ")
		if exx=='N' or exx=='n' or exx=='no':
				os._exit(1)


os.system("clear")
prfile=input("\033[1;93m# ur profile url : \033[1;0m")
prfile=client.get_from_code(prfile)

comId=prfile.path[1:prfile.path.index("/")]
subclient=amino.SubClient(comId=comId,profile=client.profile)

prfile=prfile.objectId

os.system("clear")

how=int(input("\033[1;93m# How many people : \033[1;0m"))

hi = 0
while how > hi and len :
	prfile2=input("\033[1;93m# url of the person : \033[1;0m")
	prfile2=client.get_from_code(prfile2)
	prfile2=prfile2.objectId
	hi = hi + 1
os.system("clear")

msg=input("\033[1;93m# message : \033[1;0m")
wt=0
while True:
	subclient.start_chat(userId=[prfile,prfile2],message=msg)
	wt=wt+1
	print("\033[1;92m ",wt,"\033[1;33m-\033[1;92m Done")