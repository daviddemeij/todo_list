import random
def remove_by_index_or_name(todo, index_or_name):
    print(index_or_name)
    if isinstance(index_or_name, str):
        if index_or_name in todo:
            todo.remove(index_or_name)
            print("\"{}\" removed from your todo list!".format(index_or_name))
    elif isinstance(index_or_name, int):
        if index_or_name >= 0 and index_or_name < len(todo):
            print("\"{}\" removed from your todo list!".format(todo[index_or_name]))
            del todo[index_or_name]
    else:
        print("Wrong input type. Please input a list of strings/indices or a single string/indice.")
    return todo

def add_by_name(todo, name):
    if isinstance(name, str):
        if name in todo:
            print("\"{}\" is already in your todo list!".format(name))
        else:
            todo.append(name)
            print("\"{}\" added to your todo list!".format(name))
    else:
        print("Wrong input type. Please input a list of strings or a string.")
    return todo

def get_category(category_counter, id):
    id_prev = 0
    for key in category_counter.keys():
        if id_prev <= id < category_counter[key]:
            return key_prev
        key_prev = key
    return key_prev

class todo_list():
    def __init__(self, items=[]):
        self.todo = items
    def __str__(self):
        result = "Todo list:\n"
        for nr, item in enumerate(self.todo):
            result += str(nr+1)+". "+str(item)+"\n"
        return result
    def add(self, items):
        if isinstance(items, list):
            for item in items:
                self.todo = add_by_name(self.todo, item)
        else:
            self.todo = add_by_name(self.todo, items)
    def remove(self, items):
        if isinstance(items, list):
            for item in items:
                if item in self.todo:
                    self.todo = remove_by_index_or_name(self.todo, item)
        else:
            self.todo = remove_by_index_or_name(self.todo, items)

class todo_app():
    def __init__(self, categories=["office/administration", "sport/health", "fun/leisure"]):
        self.todo_lists = {}
        self.categories = categories
        for category in self.categories:
            self.todo_lists[category] = todo_list([])
    def __str__(self):
        result = ""
        counter = 1
        self.category_counter = {}
        for nr, key in enumerate(self.todo_lists.keys()):
            self.category_counter[key] = counter
            result += key+"\n"
            for nr, item in enumerate(self.todo_lists[key].todo):
                result += "\t" + str(nr + self.category_counter[key]) + ". " + str(item) + "\n"
                counter += 1
        return result

    def add(self, items):
        if isinstance(items, list):
            for item in items:
                category = random.choice(list(self.todo_lists.keys()))
                self.todo_lists[category].add(item)
        else:
            category = random.choice(list(self.todo_lists.keys()))
            self.todo_lists[category].add(items)

    def remove(self, items):
        if isinstance(items, list):
            for item in items:
                if isinstance(item, int):
                    category = get_category(self.category_counter, item)
                    print(category)
                    self.todo_lists[category].remove(item - self.category_counter[category])
                elif isinstance(item, str):
                    for category in self.categories:
                        self.todo_lists[category].remove(item)
        elif isinstance(items, int):
            category = get_category(self.category_counter, items)
            self.todo_lists[category].remove(items - self.category_counter[category])
        elif isinstance(items, str):
            for category in self.categories:
                self.todo_lists[category].remove(items)
        else:
            print("Wrong input type. Please input a name/index or a list of names/indices")