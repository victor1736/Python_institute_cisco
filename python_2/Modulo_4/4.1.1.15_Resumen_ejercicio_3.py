'''
¿Cuál es el resultado esperado del siguiente código?

R//And*Now*for*Something*Completely*Different

'''
def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))