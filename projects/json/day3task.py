# # Primitive Data Types
# #   Mutable : False

# string1 = 'Ahmad'

# integer1 = 3

# bool1 = True

# none = None

# car1 : 'ford'
# color = 'blue'
# year = 1967


# # Composite / Compound Data Type
# # Some are Mutable: True other Mutable: False



# # ----------Mapping Type
# # Dictionary

# my_car = {
# 'car' : 'ford'
# 'car_color' : 'blue'
# 'year': '1967'
    
#         }

# print(my_car)

# #-----Sequence Types
# # Lists

# my_car_list = ['ford', 'blue', 'red', 1967]
# my_list = [car,colour, year, 1234, my_car]

# # tuples
# #in tuples we can repeat the vales
# my_tuples = (1,1,2,3,'blue','blue')

# #-------Set Types
# #sets
# #unique, unindexed, unordered

# my_set = {1,2,3,4,5}

# #Frozen sets
# my_frozenset = ({1,2,3,4,5,6,7})


# #------Special Data Type
# #Files
# #function
# # #Classes




#Short Exercise:  Create a dictionary that contains information about yourself. add an address section that holds a nested dictionary. print the contents of the dictionary and nested dictionary individually in the terminal.
#
#


# nested_dict = { A: {'firstName': 'Ahmad_Nadeem',
#                           'lastName' : 'Qureshi',
#                           'age' : 50},
#                 B: {'street': 'KoblenzerStr',
#                           'houseNo' : '1223',
#                           'city': 'Koblenz'
#                           }}
# print()
# #print(nested_dict)
# print(nested_dict[A]['lastname'])
# print(nested_dict[B]['city'])
# print()

people = {1: {'name': 'Ahmad_Nadeem', 'age': '50', 'sex': 'Male'},
          2: {'name': 'Abc', 'age': '22', 'sex': 'Female'}}
print()
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
print()
print(people[2]['name'])
print(people[2]['age'])
print(people[2]['sex'])

print()