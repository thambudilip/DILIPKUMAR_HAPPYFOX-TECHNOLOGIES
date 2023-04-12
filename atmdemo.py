#atmdemo.py--MAIN PROGRAM
import sys
from atmmenu import menu
from atmoperations import deposit,withdraw,balenq
from bankexcept import DepositError,WithdrawError, InSuffFundError
while(True):
	try:
		menu()
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1: 
				try:
					deposit()
				except ValueError:
					print("\nDon't try to deposit strs,symbols and alpha-numerics")
				except DepositError:
					print("\tDon't try to deposit Zero or -ve Numbers")
			case 2: 
				try:
					withdraw()
				except ValueError:
					print("\nDon't try to withdraw strs,symbols and alpha-numerics")
				except WithdrawError:
					print("\tDon't try to withdraw Zero or -ve Numbers")
				except InSuffFundError:
					print("\nUr Account does not have suff . Funds--read Python Notes")
			case 3: 
				balenq()
			case 4: 
				print("Thx for using this program")
				sys.exit()
			case _:
				print("Ur Selection of operation is wrong-try again")
	except ValueError:
		print("Ur Choice should not be strs, symbols and alpha-numerics")