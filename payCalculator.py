from http.client import PAYMENT_REQUIRED


def calculatePay():
    
    # This first line is provided for you
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    if (hrs > 40.0):
        OTpay = (rate*.5)*(hrs-40)
    pay = ((rate*hrs) + OTpay)
    print ("pay", str(pay))
        
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()