# exercise_03_05.py, Chapter 03, Python Crash Course
#
# Changing Guest List: You just heard that one of your guests
# can't make the dinner, so you need to send out a new set of
# invitations. You'll have to think of someone else to invite.
#
#   - Start with your program from Exercise 3.4. Add a print
#     statement at the ene of your program stating the name 
#     of the guest who can't make it.
#
#   - Modify your list, replacing the name of the guest who 
#     can't make it with the name of the new person you are
#     inviting.
#
#   - Print a second set of invitation messages, one for each
#     person who is still in your list.

guest_list = ['benjamin franklin', 'frederick douglass', 
              'samuel clemens', 'alan turing', 
              'gene roddenberry', 'mel brooks']

print("\n")
print("Dinner Invitations: ")
print("-----------------------------------------------------------------------------------------------")
print("Dear, Mr. " + guest_list[0].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[1].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[2].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[3].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[4].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[5].title() + "! You are cordially invited to The Dinner of the Minds.")

print("\n")
cancellation = guest_list.pop(5)
print("Dinner Cancellation: ")
print("-----------------------------------------------------------------------------------------------")
print("Unfortunately, Mr. " + cancellation.title() + " won't be able to attend The Dinner of the Minds.")

print("\n")
guest_list.insert(5, 'dennis ritchie')
print("Update Dinner Invitations: ")
print("----------------------------------------------------------------------------------------------")
print("Dear, Mr. " + guest_list[0].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[1].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[2].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[3].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[4].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[5].title() + "! You are cordially invited to The Dinner of the Minds.")
print("\n")



