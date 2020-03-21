shopping_list=['milk','pasta','eggs','spam','bread','rice']
item_to_find="spam"
found_at=None
if item_to_find in shopping_list:
    found_at=shopping_list.index(item_to_find)
if found_at is not None:
    print(f"item found at position {found_at}")
else:
    print(f"{item_to_find} not found ")