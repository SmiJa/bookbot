def word_count(text):
  words = len(text.split())
  return words

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)
    print(word_count(file_contents))

if __name__ == '__main__':
  main()