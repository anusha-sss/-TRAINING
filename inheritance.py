class mammal:
    def walk(self):
        print("walk")


class dog(mammal):
    def bark(self):
        print("bark")

class cat(mammal):
    pass


dog1 = dog()
dog1.walk()
dog1.bark()

cat1 = cat()
cat1.walk()



