# Python set is an unordered list of immutable elements
# Elements in a set are unordered.
# Lements in a set are unique. A set doesn’t allow duplicate elements.

skills = {'Python programming','Databases', 'Software design'}

print(len(skills))
print('Python programming' in skills)

skills.add('Problem solving') # at the begining
skills.remove('Software design')