tel = {'jack': 4098, 'sape': 4139, 'guido': 4127}
print("sape" in tel)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print(q, "→", a)
