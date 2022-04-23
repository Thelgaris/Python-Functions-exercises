# Your code goes here:
def render_person(name, birth_year, color_eyes, age, gender):
    sentence =  f'{name} is a {age} old {gender} born in {birth_year} with {color_eyes} eyes'
    return sentence

# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))