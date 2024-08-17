def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    total_words = word_count(file_contents)
    char_count = char_counts(file_contents)
    char_list = []
    dict_to_list(char_count, char_list)
    char_list.sort(reverse=True, key=sort_char_count_on)
    build_report(char_list, total_words)

def word_count(text):
  words = len(text.split())
  return words

def char_counts(string):
  lowered_string = string.lower()
  chars = {}
  for char in lowered_string:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  return chars

def dict_to_list(dict, list):
  for char in dict:
    my_dict = {"char": char, "num": dict[char]}
    if char.isalpha():
      list.append(my_dict)

def sort_char_count_on(dict):
  return dict["num"]

def build_report(list, words):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{words} words found in the document\n")
  for char in list:
    letter = char["char"]
    number = char["num"]
    print(f"The '{letter}' character was found {number} times")
  print("--- End report ---")

if __name__ == '__main__':
  main()