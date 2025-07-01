val_arr = []
alternate_arr = ["create_arr()", "None"]

val = 0

def create_arr():
    global val
    val_arr.append(val)
    val += 26

    eval(alternate_arr[val>500]);


create_arr()
print(val_arr)