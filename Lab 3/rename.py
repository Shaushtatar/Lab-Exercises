#used provided article https://www.tutorialspoint.com/rename-multiple-files-using-python#:~:text=To%20rename%20files%20in%20Python,the%20destination_address%20(new%20name).

import os
path = "C:\\Users\\billy\\OneDrive\\Documents\\GitHub\\Lab-Exercises\\Lab 3\\Rorschach Images\\"
i = 0
for filename in os.listdir(path):
    my_dest = f"Ror{i}.png"
    my_source = path + filename
    my_dest = path + my_dest
    os.rename(my_source, my_dest)
    i+=1