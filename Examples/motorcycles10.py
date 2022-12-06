# motorcycles10.py, Chapter 03, Python Crash Course
# program prints a list, removes an item from a list,
# prints the list again, and prints an explanation
# for the item removal

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")



