#bankexcept.py--file name and acts as module name
class DepositError(Exception):pass
class WithdrawError(Exception):pass
class  InSuffFundError(BaseException):pass