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

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)
    # print(word_count(file_contents))
    print(char_counts(file_contents))

if __name__ == '__main__':
  main()