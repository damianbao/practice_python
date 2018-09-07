import os

#set the working directory as data (chdir = choose directory

os.chdir('data')




def weather_data (t):
    #loop through the files in the working directory

    temps =[]
    
    for f in os.listdir():
        if f[-4:] == '.txt':    # f[-4:] = last 4 char. of f
            f1 = open(f, 'r')
            
            while True:
                line = f1.readline()
                
                if line:
                    line_split = line.split()       # [0] = time, [1] = temp
                    if line_split[0] == t:
                        print (line_split[1])
                else:
                    break
                
            f1.close()          #frees up file name for later use

    return (temps)


weather_data ('1500')



