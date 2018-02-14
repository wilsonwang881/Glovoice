

dil=[1,2,3,4,5,6]

def display_input(in_list):
        
        print ("thumb sensor value: ",in_list[0] )
        print ("index finger sensor value: ",in_list[1])
        print ("middle finger sensor value: ",in_list[2])
        print ("ring finger sensor value: ",in_list[3])
        print ("pinky sensor value: ",in_list[4] )
        print ("gyroscope sensor value: ",in_list[5])

def analyze_data_sensor(data_in,boundary_upper,boundary_lower):
    bool_out = True
    
    if data_in < boundary_lower:
          bool_out = True
    elif data_in > boundary_upper:
          bool_out = True
    else:
          bool_out = True
    return bool_out




display_input(dil)
bool_out = False
bool_out = analyze_data_sensor(dil[0],10,0)
print(bool_out)


        
        



