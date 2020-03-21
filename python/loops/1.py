shopping_list=['milk','pasta','eggs','spam','bread','rice']

item_to_find="pasta"
found_at=None

for index in range(len(shopping_list)):
    if shopping_list[index]==item_to_find:
        found_at=index
print(f"Item found at position {index}")