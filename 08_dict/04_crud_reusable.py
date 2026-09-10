def generate_id(items):
    return max(item["id"] for item in items) + 1


def find_item_by_id(id, items):
    for item in items:
        if item["id"] == id:
            return item


def update_item(id, payload, items):
    item = find_item_by_id(id, items)
    if item:
        item.update(payload)
        return item


def create_item(payload, items):
    items.append({"id": generate_id(items), **payload})
    return items[-1]


def remove_item(id, items):
    item = find_item_by_id(id, items)
    if item:
        items.remove(item)
        return True
    return False
