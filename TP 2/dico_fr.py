dico = {"hello": "bonjour", "ball": "ballon", "computer": "ordinateur"}

dico_new = {}
for key, value in dico.items():
    dico_new[value] = key
    
print(dico_new)