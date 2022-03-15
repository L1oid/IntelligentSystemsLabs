last_message = ""

def print_without_duplicates(message):
    global last_message
    if message != last_message:
        print(message)
    last_message = message

print_without_duplicates("привет")
print_without_duplicates("привет")
print_without_duplicates("как дела")
print_without_duplicates("как дела")
print_without_duplicates("ответь")
print_without_duplicates("ответь")
