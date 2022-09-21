import requests
from poem import Poem


class PoetryCollection2:
    def __init__(self, poem_json_list):
        self.author_to_poem = {}
        for poem_json in poem_json_list:
            new_poem = Poem(poem_json)
            current_author = new_poem.author
            if current_author not in self.author_to_poem:
                self.author_to_poem[current_author] = []
            current_author_list = self.author_to_poem[current_author]
            current_author_list.append(new_poem)

    def find_longest(self):
        pass

    def poem_count_for_author(self, author):
        pass

    def most_poems_for_author(self):
        pass


def main():
    response = requests.get("https://poetrydb.org/poemcount/3162")
    poems_json = response.json()
    all_poems = PoetryCollection2(poems_json)
    print(all_poems.find_longest())
    print(all_poems.poem_count_for_author("Emily Dickinson"))
    print(all_poems.most_poems_for_author())


if __name__ == "__main__":
    main()
