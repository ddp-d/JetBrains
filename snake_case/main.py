phrase = input()

snake_case = ""
snake_case = snake_case + phrase[0].lower()
for c in phrase[1:]:
    if c.isupper():
        snake_case = snake_case + "_"
        snake_case = snake_case + c.lower()
    else:
        snake_case = snake_case + c

print(snake_case)
