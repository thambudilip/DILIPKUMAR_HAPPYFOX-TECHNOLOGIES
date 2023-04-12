#atmoperations.py---file name and acts as module name
from bankexcept import DepositError,WithdrawError, InSuffFundError
bal=500.00
def  deposit():
	damt=float(input("Enter How much u want to Deposit:")) # ValueError
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("Ur Account XXXXX123 Credited with INR:{}".format(damt))
		print("Now Ur Current Bal INR:{}".format(bal))

def  withdraw():
	global bal
	wamt=float(input("Enter How much u want to Withdraw:")) # ValueError
	if(wamt<=0):
		raise WithdrawError
	elif((wamt+500)>bal):
		raise InSuffFundError
	else:
		bal=bal-wamt
		print("Ur Account XXXXX123 Debited with INR:{}".format(wamt))
		print("Now ur Current Bal INR:{}".format(bal))

def balenq():
	print("Current Bal in Ur Account INR:{}".format(bal))
