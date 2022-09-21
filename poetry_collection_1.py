import requests
from poem import Poem


class PoetryCollection1:
    def __init__(self, poem_json_list):
        self.poem_list = []
        for poem_json in poem_json_list:
            new_poem = Poem(poem_json)
            self.poem_list.append(new_poem)

    def find_longest(self):
        pass

    def poem_count_for_author(self, author):
        pass

    def most_poems_for_author(self):
        pass


def main():
    response = requests.get("https://poetrydb.org/poemcount/3162")
    poems_json = response.json()
    all_poems = PoetryCollection1(poems_json)
    print(all_poems.find_longest())
    print(all_poems.poem_count_for_author("Walt Whitman"))
    print(all_poems.most_poems_for_author())


if __name__ == "__main__":
    main()
