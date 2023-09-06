metal_cost = eval(input())
tip = eval(input())
tax = eval(input())
tip_calc = (metal_cost/100)*(tip)
tax_calc = (tax/100)*(metal_cost)
total_price = metal_cost+tip_calc+tax_calc
print(round(total_price))
