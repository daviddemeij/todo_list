import random
import re
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format("./GoogleNews-vectors-negative300.bin", binary=True)
def remove_by_index_or_name(todo, index_or_name):
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

def add_by_name(todo, name, category):
    if isinstance(name, str):
        if name in todo:
            print("\"{}\" is already in your todo list!".format(name))
        else:
            todo.append(name)
            print("\"{}\" added to \"{}\"!".format(name, category))
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

def get_closest_category(categories, item):
    similarity = {}
    item_words = re.split("-| |/|, ", item)
    item_words = list(filter(lambda x: x.lower() in model.vocab, item_words))
    for category in categories.keys():
        similarity[category] = 0
        for item_word in item_words:
            if len(item_word)>1:
                for keyword in categories[category]:
                    similarity[category] += (model.similarity(keyword.lower(), item_word.lower()) / float(len(categories[category])))
    return max(similarity.keys(), key=(lambda key: similarity[key]))

class todo_list():
    def __init__(self, items=[]):
        self.todo = items
    def __str__(self):
        result = "Todo list:\n"
        for nr, item in enumerate(self.todo):
            result += str(nr+1)+". "+str(item)+"\n"
        return result
    def add(self, items, category):
        if isinstance(items, list):
            for item in items:
                self.todo = add_by_name(self.todo, item, category)
        else:
            self.todo = add_by_name(self.todo, items, category)
    def remove(self, items):
        if isinstance(items, list):
            for item in items:
                if item in self.todo:
                    self.todo = remove_by_index_or_name(self.todo, item)
        else:
            self.todo = remove_by_index_or_name(self.todo, items)

class todo_app():
    def __init__(self, categories={"office/administration": ["office", "administration", "business", "work", "accounting", "report"],
                                   "fun/leisure": ["fun", "leisure", "music", "film", "family", "friends"],
                                   "sports/health": ["sport", "health", "training", "fitness", "workout"]}):
        self.todo_lists = {}
        self.categories = categories
        for category in self.categories.keys():
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
                category = get_closest_category(self.categories, item)
                self.todo_lists[category].add(item, category)
        else:
            category = get_closest_category(self.categories, items)
            self.todo_lists[category].add(items, category)

    def remove(self, items):
        if isinstance(items, list):
            for item in items:
                if isinstance(item, int):
                    category = get_category(self.category_counter, item)
                    self.todo_lists[category].remove(item - self.category_counter[category])
                elif isinstance(item, str):
                    for category in self.categories.keys():
                        self.todo_lists[category].remove(item)
        elif isinstance(items, int):
            category = get_category(self.category_counter, items)
            self.todo_lists[category].remove(items - self.category_counter[category])
        elif isinstance(items, str):
            for category in self.categories:
                self.todo_lists[category].remove(items)
        else:
            print("Wrong input type. Please input a name/index or a list of names/indices")

    def move(self, item_nr, move_to_category):
        if isinstance(item_nr, int):
            if move_to_category in self.categories.keys():
                category = get_category(self.category_counter, item_nr)
                self.todo_lists[move_to_category].add(self.todo_lists[category].todo[item_nr - self.category_counter[category]], move_to_category)
                self.todo_lists[category].remove(item_nr - self.category_counter[category])
            else:
                print("Category not found!")