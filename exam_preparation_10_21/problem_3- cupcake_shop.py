def stock_availability(inventory: list, delivery_sell, *args):
    if delivery_sell == 'delivery':
        inventory += args
    elif delivery_sell == 'sell':
        if not args:
            inventory = inventory[1:]
            return inventory
        for el in args:
            if isinstance(el, int):
                inventory = inventory[el:]
                break
            while el in inventory:
                inventory.remove(el)
    return inventory
