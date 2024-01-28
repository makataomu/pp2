class myclass():
  def __len__(self):
    return 0
  
class myclass2():
  pass

myobj = myclass()
print(bool(myobj)) 

print(bool(myclass2())) 