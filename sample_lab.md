# Lab 5 Sample: Store Manager Cart System

Suppose you are the manager of the UOG Convenience Store. Finals week is busy and students keep coming in for quick items. You want a simple system to show them random items from different categories and let them build their shopping cart.

You will make a program called `store_manager.py` that will do the following:

- Stores a collection of store items organized by category using a **dictionary**. The dictionary is structured where your keys are the categories and the values are a list of items. Each item is stored as a list `[name, price]`. Below is an example (you may use it as well)

```python
category_to_items = {
    "snacks": [
        ["Potato Chips", 2.49],
        ["Chocolate Bar", 1.99],
        ["Instant Noodles", 1.25],
        ["Gummy Bears", 2.99],
        ["Cookies", 3.49],
        ["Beef Jerky", 4.25]
    ],
    "drinks": [],
    "food": [],
    "school supplies": [],
    "merch": []
}
```

- Create a shop manager where it edits a list of items the user is buying!