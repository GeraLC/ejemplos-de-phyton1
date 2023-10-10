class User: 
    
    def __str__(self):
        return "user:"+self.email
    Name=None
    email=None
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def send_email(self):
        if self.email is not None:
            print("sending email"+self.email)
        else:
            print ("error")

class Student(User):
   
   def __repr__(self):
       return F" Student(name='{self.name}'email='{self.email}',id='{self.id}',score='{self.score})"
   
   def is_approved(self):
       return self.score>=8
   score=name
   def __str__(self):
        return "student:"+str(self.id)+","+self.email
   id=None
   def __init__(self,name=None,email=None, id=None, score=name):
    super().__init__(name,email)
