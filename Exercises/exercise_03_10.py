# exercise_03_10.py, Chapter 03, Python Crash Course
#
# Every Function: Think of something you could store in a list.
# For example, you could make a list of mountains, rivers, 
# countries, cities, languages, or anything else you'd like.
# Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at
# least once.

programming_languages = ['c', 'basic', 'c++', 'assembly']

# print()

print(programming_languages)

# title()

print(programming_languages[0].title())
print(programming_languages[1].title())
print(programming_languages[2].title())
print(programming_languages[3].title())

# pop()

print(programming_languages)
print(programming_languages.pop())
print(programming_languages)

# insert()

programming_languages.insert(0, 'python')
programming_languages.insert(0, 'java')
print(programming_languages)

# append()

programming_languages.append('assembly')
print(programming_languages)

# remove()

programming_languages.remove('java')
print(programming_languages)

# reverse()

programming_languages.reverse()
print(programming_languages)

# sorted()

print(sorted(programming_languages, reverse=False))
print(programming_languages)

# sort()

programming_languages.sort(reverse=False)
print(programming_languages)



