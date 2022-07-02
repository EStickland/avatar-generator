import numpy as np
from PIL import Image


##############  CUSTOM VARIABLES ##################

# What is the path of the image you would like your avatar to be based on?
path_to_source_image = ''

# Where would you like the avatar to be saved? 
# Please include the name of the file and extension e.g. '.png' or '.jpg'
path_to_output_image = ''

# How many boxes should be the image be slit into (across)
# The optimal value will depend on the image and how complex the shape is
# Try testing a few numbers out
num_boxes = 12

# Colour of avatar
colour = [241,199,45] # yellow

################################################################################################

def configureImage(path=path_to_source_image):
    source_image = Image.open(path_to_source_image)
    array_avatar = np.array(source_image)

    width_length = round(array_avatar.shape[1]/num_boxes,0)
    x_start = np.around(np.arange(0, array_avatar.shape[1], round(array_avatar.shape[1]/num_boxes,0)),0).tolist()
    x_start[-1] = array_avatar.shape[1] - round(array_avatar.shape[1]/num_boxes,0)

    y_start = np.around(np.arange(0, array_avatar.shape[0], round(array_avatar.shape[1]/num_boxes,0)),0).tolist()
    y_start[-1] = array_avatar.shape[0] - round(array_avatar.shape[1]/num_boxes,0)

    return array_avatar,width_length, x_start, y_start

def image2Avatar(array_avatar, width_length,colour, x_start, y_start, start_background_colour=[0,0,0], output_background_colour= [237,237,237]):
    for y in y_start:
        y_box_start = y
        for x in x_start:
            x_box_start = x
            background_count= 0
            image_count= 0
            for a in array_avatar[int(y_box_start):int(y_box_start+width_length)]:
                    for b in a[int(x_box_start):int(x_box_start+width_length)]:
                            if (b[0] ==start_background_colour[0]) and (b[1] ==start_background_colour[1]) and (b[2] ==start_background_colour[2]):
                                background_count+=1
                            else:
                                image_count+=1
            if background_count > (image_count):
                new_colour = [output_background_colour[0],output_background_colour[1],output_background_colour[2],255]
            else: 
                new_colour = [colour[0],colour[1],colour[2],255]
            for y2 in range(int(y_box_start),int(y_box_start+width_length)):
                array_avatar[y2][int(x_box_start):int(x_box_start+width_length)] = np.array(new_colour)
            background_count= 0
            image_count= 0
    return array_avatar


array_avatar,width_length, x_start, y_start = configureImage()
array_avatar = image2Avatar(array_avatar,width_length, colour,x_start, y_start)

final_image = Image.fromarray(array_avatar)
final_image = final_image.save(path_to_output_image)