# import file function
def load_file(path):
    with open(path, "r") as cadFile:
        data = cadFile.readlines()       
    return data           # data's job is done, handed off

# retrieve fuducial data          
def get_fiducials(data):
    #store fudicial data once formatted
    fid_clean = []
    #itterate over data 
    for line in data:
    #identify fiducial lines    
        if line.startswith("4.3MM"):
        #format line removing carrige return and spaces
            split = split_name(line)
        # IF value in line is a number format 
            formatted_value = is_valid_number(split)
            fid_clean.append(formatted_value)


        if line.startswith("[Bottom side]"):
            break
    return fid_clean



# ************* helper functions ******************
# remove white space 
def split_name(line):
    line_list = line.split("|")
    clean_list = []
    for word in line_list:
        remove_white_space = word.strip()
        if len(remove_white_space):
           clean_list.append(remove_white_space)      

    return clean_list

#check if value is number
def is_valid_number(split):  
    #store new list item
    value_list = []   
#itterat over line
    for value in split:
    #if value is number pass to convert to microns for formatting 
        try:
            is_float = float(value)
            formatted_number = convert_to_microns(is_float)
            value_list.append(formatted_number)
           
        except ValueError:            
                 value_list.append(value)
    return(value_list)
      

# convert mm to microns (x1000) and return int
def convert_to_microns(value):
    #times by 1000
    micron_value = value * 1000 
    #convert from float to int 
    micron_value_as_int = int(micron_value)
    #return new value
    return micron_value_as_int




#main
path = "LED-0134-001 iss 1.txt"
data = load_file(path)
get_fiducials(data)




