import os
import glob

# Directory file folder
dirr = 'a'
# Aim directory and the name of the file
var = 'solo'
# Restart the sequential number, if you want 
start = 40
# Sequential number of file
idx = 0
for filename in glob.glob('{}'.format(dirr)+'\*.jpg'): 
    '''
        If there is a restart of the sequential, please uncomment the code bellow !
    '''
    # if(idx == restart):
    #     idx = 0
    #     start+=1

    '''
       You can change the variance of rename as you want bellow !
    '''
    os.rename(r'{}'.format(filename),r'{}'.format(var)+'/'+var+'_{}'.format(start)+'.mp4_frame{}.jpg'.format(idx))
    idx+=1

# Show the last index of the sequential
print()
print("LAST INDEX :",idx-1)
