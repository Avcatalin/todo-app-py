languages = ['English', 'German', 'Spanish']

for lang in languages:
    with open(f"{lang}.txt", "w") as file:
        file.write(lang)