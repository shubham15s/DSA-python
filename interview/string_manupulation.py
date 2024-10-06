string_input = '''John,25,New York
Anna,30,Los Angeles
Mike,22,New York
Sara,28,Los Angelest
David,35,Chicago'''

# Split the input by lines
lines = [line.strip() for line in string_input.strip().split("\n") if line]

sdict = {}

for line in lines:
    name, age, city = line.split(",")
    age = int(age)  
    
    if city not in sdict:
        sdict[city] = []
    sdict[city].append((name, age))

print(sdict)
