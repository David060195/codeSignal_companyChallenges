import re 
import ast
def shoppingList(items):
    m = re.findall(r'[\d\.\d]+', items)
    ans = 0
    for number in m:
        ans += ast.literal_eval(number.strip("."))
    return ans
