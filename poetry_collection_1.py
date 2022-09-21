import requests
from poem import Poem


class PoetryCollection1:
    def __init__(self, collection_name, poem_json_list):
        self.name = collection_name
        self.poem_list = []
        for poem_json in poem_json_list:
            new_poem = Poem(poem_json)
            self.poem_list.append(new_poem)

    def __str__(self):
        return self.name + ": A collection of " + str(len(self.poem_list)) + " poems"

    def find_longest_poem(self):
        """:return: the longest Poem in this collection, or None if the collection has no poems"""
        pass

    def count_poems_for_author(self, author):
        """:return: the number of poems in this collection by the given author"""
        pass

    def find_author_with_most_poems(self):
        """:return: the author who has the most poems in this collection"""
        pass


def main():
    response = requests.get("https://poetrydb.org/poemcount/3162")
    poems_json = response.json()
    all_poems = PoetryCollection1("All poems from poetrydb.com", poems_json)
    print(all_poems)
    print(all_poems.find_longest_poem())
    print(all_poems.count_poems_for_author("Walt Whitman"))
    print(all_poems.find_author_with_most_poems())


if __name__ == "__main__":
    main()
