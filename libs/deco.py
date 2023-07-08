# Higher-order function

def coupon_calculator(func):
    def report_price():
        print("Initial Price = 35.0")
        final_price = func(35.00)
        print(f"Newly Discount Price = {final_price}")
    return report_price

# calculate the price


# def calculate(price):
#     return '{:.2f}'.format(round(price / 2, 2))


# new_price = coupon_calculator(calculate)
# new_price()


# with pie sybtax
# @decorator
@coupon_calculator
def calculate(price):
    return '{:.2f}'.format(round(price / 2, 2))


calculate()
