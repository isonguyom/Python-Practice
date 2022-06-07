class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    # Change name method
    def change_name(self, new_name):
        self.name = new_name
    
    # Change age method
    def change_age(self, new_age):
        self.age = new_age

    # Add new track method
    def add_track(self, new_track):
        self.tracks.append(new_track)

    # Get student score method
    def get_score(self):
        return self.score



# Try
Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.get_score())