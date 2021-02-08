def div(a,b):
    if a<b:
        a,b = b,a
    print(a/b)
# def smart_div(func):
#     def inner_div(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner_div
# div1= smart_div(div)
# div1(3,12)
div(12,3)