import importlib
import filechanges

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.priint_changes()
    except:
        pass
    
for i in range(5):
    changes()
    input("Hit enter to reload...")