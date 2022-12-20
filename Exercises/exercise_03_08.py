# exercise_03_08.py, Chapter 03, Python Crash Course
#
# Seeing the World: Think of at least five places in the world
# you'd like to visit.

#   - Store the locations in a list. Make sure the list is not
#     alphabetical order

country_list = ['thailand', 'brazil', 'uae', 'south korea', 'colombia']

#   - Print your list in its original order. Don't worry about
#     printing the list neatly, just print it as a raw Python
#     list

print(country_list)

#   - Use sorted() to print your list in alphabetical order 
#     without modifying the actual list

print(sorted(country_list))

#   - Show that your list is still in its original order by
#     printing it

print(country_list)

#   - Use sorted() to print your list in reverse alphabetical
#     order without changing the order of the original list

print(sorted(country_list, reverse=True))

#   - Show that your list is still in its original order by 
#     printing it again

print(country_list)

#   - Use reverse() to change the order of your list. Print
#     the list to show that its order has changed

country_list.reverse()
print(country_list)

#   - Use reverse() to change the order of your list again.
#     Print the list to show it's back to its original order

country_list.reverse()
print(country_list)

#   - Use sort() to change your list so it's stored in 
#     alphabetical order. Print the list to show that its
#     order has been changed

country_list.sort(reverse=False)
print(country_list)

#   - Use sort() to change your list so it's stored in
#     reverse alphabetical order. Print the list to show
#     that its order has changed

country_list.sort(reverse=True)
print(country_list)



