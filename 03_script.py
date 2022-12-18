Topic = """Using str.format()"""
print(Topic)

son_likes = "Alexis my son likes {} and {} and he is {} years old"
print(son_likes.format("Rice", "Beans", 2))
print(type(10))
print("Sammy the {0} has a pet {1}!".format("shark", "pilot fish"))
Alexis = "Sammy the {0} has a pet {1}!"
print(Alexis.format("shark", "pilot fish"))
print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))
print("{:*^20s}".format("Sammy"))
print("Sammy ate {0:5.0f} percent of a pizza!".format(75.765367))
nBalloons = 8
print("Sammy has {} balloons today!".format(nBalloons))
sammy = "Sammy has {} balloons today!"
nBalloons = 8
print(sammy.format(nBalloons))
for i in range(3,13):
    print(i, i*i, i*i*i)
for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))
for i in range(3,13):
    print("{:6d} {:6d} {:6d}".format(i, i*i, i*i*i))
