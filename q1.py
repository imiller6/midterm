def computeMinimumPayment( balance ):
	if int(balance) * .021 > 10:
    		return int(balance) * .021
        elif int(balance) == 10:
    		return 10
        else:
    		return int(balance)