# My first git pitch
---
A little bit of python code:  
```
## This is an infinite list generator

def infinite_gen(gen):
    return gen + 1

i = 0
while i < 5:
    i = infinite_gen(i)
    print("Increment: {}".format(i))
```
h
---
Import code  from file

---?code=migration.py&lang=python  
@[27] Import requied libs  
@[30-33] The main cli command  
@[36-43] The `generate` subcommand  
@[96] Add the subcommand  
---
# Thank you