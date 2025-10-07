#WAF to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 89
    print("$",usd_val,"= ₹",inr_val)

converter(1)
converter(3)
converter(5)
converter(7)
converter(9)