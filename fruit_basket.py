# result = 0
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
#
# for key, count in basket_items.items():
#     if key in fruits:
#         result += count
# print(result)
#
# # print fruits and non fruits items
# fruit_count = 0
# not_fruit_count = 0
# for object, count in basket_items.items():
#     if object in fruits:
#         fruit_count += count
#     else:
#         not_fruit_count += count
# print("fruits: {} not fruits: {}" .format(fruit_count, not_fruit_count))

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
fruit_weight = 0
items = []
for fruits_name, fruits_cargo in manifest:
    print('current fruit {}'.format(fruit_weight))
    if fruit_weight >= 50 and fruit_weight<100:
        print('Breaking loop now')
        break
    else:
        print('adding fruits {} {}'.format(fruits_name, fruits_cargo))
        items.append(fruits_name)
        fruit_weight += fruits_cargo


print('Final fruits weight {}'.format(fruit_weight))
print('Fruits items {}' .format(items))