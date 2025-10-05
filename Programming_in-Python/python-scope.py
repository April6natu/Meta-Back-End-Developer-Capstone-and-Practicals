#global scope
my_global = 10

def fn1():
    
    enclosed_v = 8
    #local scope
    
    def fn2():
        local_v = 5
        print('Access to Global', my_global)
        print('Access to enclosed', enclosed_v)
        print('Access to local', local_v)
    
    # Call fn2 to execute the inner function
    fn2()
    print('Enclosed variable:', enclosed_v)
    # print(local_v)  # This would raise an error - local_v is not accessible here

# Call fn1 to execute the function
fn1()