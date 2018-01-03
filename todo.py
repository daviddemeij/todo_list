def remove_by_index_or_name(todo, index_or_name):
    print(index_or_name)
    if isinstance(index_or_name, str):
        if index_or_name in todo:
            todo.remove(index_or_name)
        else:
            print("\"{}\" not found!")
    elif isinstance(index_or_name, int):
        if index_or_name > 0 and index_or_name < len(todo): del todo[index_or_name - 1]
    else:
        print("Wrong input type. Please input a list of strings/indices or a single string/indice.")
    return todo

def add_by_name(todo, name):
    if isinstance(name, str):
        if name in todo:
            print("\"{}\" is already in your todo list!".format(name))
        else:
            todo.append(name)
    else:
        print("Wrong input type. Please input a list of strings or a string.")
    return todo

class todo_list():
    def __init__(self, items=[]):
        self.todo = items

    def add(self, items):
        nr_todo = len(self.todo)
        if isinstance(items, list):
            for item in items:
                self.todo = add_by_name(self.todo, item)
        else:
            self.todo = add_by_name(self.todo, items)
        print("{0} item(s) added to your todo list!".format(len(self.todo) - nr_todo))

    def remove(self, items):
        if isinstance(items, list):
            for item in items:
                if item in self.todo:
                    self.todo = remove_by_index_or_name(self.todo, item)
        else:
            self.todo = remove_by_index_or_name(self.todo, items)

    def __str__(self):
        result = "Todo list:\n"
        for nr, item in enumerate(self.todo):
            result += str(nr+1)+". "+str(item)+"\n"
        return result
