import string

user_input = input("Введите буквы через дефис 2 буквы по примеру (a-c, b-K и т.д.): ")

letters = string.ascii_letters
start_letter = user_input[0]
end_letter = user_input[2]

start_index = letters.index(start_letter)
end_index = letters.index(end_letter)

result = letters[start_index:end_index + 1]

print(result)
