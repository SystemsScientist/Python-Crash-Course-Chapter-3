# exercise_03_06.py, Chapter 03, Python Crash Course
#
# Shrinking Guest List: You just found out that your new dinner
# table won't arrive in time for the dinner, and you have space 
# for only two guests.
#
#   - Start with your program from Exercise 3-6. Add a new line
#     that prints a message saying that you can invite only two
#     people for dinner.
#
#   - Use pop() to remove guests from your list one at a time
#     until only two names remain in your list. Each time you 
#     pop a name from your list, print a message to that person
#     letting them know you're sorry you can't invite them to
#     dinner.
#
#   - Print a message to each of the two people still on your
#     list, letting them know they're still invited
#
#   - Use del to remove the last two names from your list, so
#     you have an empty list. Print your list to make sure you
#     actually have an empty list at the end of your program.

guest_list = ['benjamin franklin', 'frederick douglass', 
              'samuel clemens', 'alan turing', 
              'gene roddenberry', 'morgan freeman']

print("\n")
print("Dinner Invitations: ")
print("---------------------------------------------------------------------------------------")
print("Dear, Mr. " + guest_list[0].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[1].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[2].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[3].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[4].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[5].title() + "! You are cordially invited to The Dinner of the Minds.")

print("\n")
print("Because of an increase in the number of guests, a larger table has been found.")

print("\n")
guest_list.insert(0, 'marcus aurelius')
guest_list.insert(3, 'albert einstein')
guest_list.append('leonard nimoy')

print("\n")
print("Updated Dinner Invitations: ")
print("---------------------------------------------------------------------------------------")
print("Dear, Emperor " + guest_list[0].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[1].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[2].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[3].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[4].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[5].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[6].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[7].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[8].title() + "! You are cordially invited to The Dinner of the Minds.")

print("\n")
print("Unfortunately, The Dinner of the Minds can only invite two guests.")

print("\n")
cancel_guest = guest_list.pop(0)
print("Dinner Cancellation Notices: ")
print("---------------------------------------------------------------------------------------------------------")
print("Dear, Emperor " + cancel_guest.title() + "! We are sorry that we can't invite you to The Dinner of the Minds.")

cancel_guest = guest_list.pop(0)
print("Dear, Mr. " + cancel_guest.title() + "! We are sorry that we can't invite you to The Dinner of the Minds.")

cancel_guest = guest_list.pop(0)
print("Dear, Mr. " + cancel_guest.title() + "! We are sorry that we can't invite you to The Dinner of the Minds.")

cancel_guest = guest_list.pop(0)
print("Dear, Dr. " + cancel_guest.title() + "! We are sorry that we can't invite you to The Dinner of the Minds.")

cancel_guest = guest_list.pop(0)
print("Dear, Mr. " + cancel_guest.title() + "! We are sorry that we can't invite you to The Dinner of the Minds.")

cancel_guest = guest_list.pop(0)
print("Dear, Dr. " + cancel_guest.title() + "! We are sorry that we can't invite you to The Dinner of the Minds.")

cancel_guest = guest_list.pop(0)
print("Dear, Mr. " + cancel_guest.title() + "! We are sorry that we can't invite you to The Dinner of the Minds.")

print("\n")
print("Update to Remaining Dinner Guests: ")
print("-------------------------------------------------------------------------------------------")
print("Dear, Mr. " + guest_list[0].title() + "! You are still invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[1].title() + "! You are still invited to The Dinner of the Minds.")

print("\n")
del guest_list[0]
del guest_list[0]

print(guest_list)
print("\n")




