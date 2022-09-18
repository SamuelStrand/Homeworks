# Поиск палиндрома с использованием рекурсии
def recursion(word) -> bool:
    word = str(word)
    word = str(word.lower().strip())
    if len(word) < 1:
        return True
    else:
        if word[0] == word[-1]:
            return recursion(word[1:-1])
        else:
            return False


# Поиск палиндрома с использованием цикла и рекурсии
def recursion_with_loop(word) -> bool:
    word = str(word)
    word = word.lower().strip()
    letter_arr = []
    for letter in word:
        letter_arr.append(letter)
    if len(letter_arr) < 1:
        return True
    else:
        if letter_arr[0] == letter_arr[-1]:
            return recursion_with_loop(word[1:-1])

        else:
            return False


class Palindrome:
    def __init__(self, word):
        self.word = str(word).lower().strip()

    # Поиск палиндрома без использования рекурсии
    def is_palindrome(self):
        if self.word == self.word[::-1]:
            return True
        else:
            return False


obj = Palindrome(321321)

if __name__ == '__main__':
    print(recursion('А роза упала на лапу Азора'))
    print(recursion_with_loop(12321))
    print(obj.is_palindrome())
