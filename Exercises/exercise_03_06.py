#
# More Guests: You just found a bigger dinner table, so now
# more space is available. Think of three more guests to
# invite to dinner.
#
#   - Start with your program from Exercise 3-4 or Exercise 3-5.
#     Add a print statement to the end of your program informing
#     people that you found a bigger dinner table.
#
#   - Use insert() to add one new guest to the beginning of your
#     list.
#   
#   - Use insert() to add one new guest to the middle of your 
#     list.
#
#   - Use append() to add one new guest to the end of your list.
#
#   - Print a new set of invitation messages, one for each person
#     in your list.

guest_list = ['benjamin franklin', 'frederick douglass', 
              'samuel clemens', 'alan turing', 
              'gene roddenberry', 'mel brooks']

print("\n")
print("Dinner Invitations: ")
print("------------------------------------------------------------------------------------")
print("Dear, Mr. " + guest_list[0].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[1].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[2].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[3].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[4].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[5].title() + "! You are cordially invited to The Dinner of the Minds.")

print("\n")
print("Update to all guests, a larger table has been found. So, more guests will be invited!")

print("\n")
guest_list.insert(0, 'marcus aurelius')
guest_list.insert(3, 'albert einstein')
guest_list.append('leonard nimoy')

print("\n")
print("Updated Dinner Invitations: ")
print("------------------------------------------------------------------------------------")
print("Dear, Emperor " + guest_list[0].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[1].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[2].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[3].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[4].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Dr. " + guest_list[5].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[6].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[7].title() + "! You are cordially invited to The Dinner of the Minds.")
print("Dear, Mr. " + guest_list[8].title() + "! You are cordially invited to The Dinner of the Minds.")



