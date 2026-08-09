# import file function
def load_file(path):
    with open(path, "r") as cadFile:
        data = cadFile.readlines()       
    return data           # data's job is done, handed off

#retreive pcb name will be used for f1 and file save name
def get_pcb_name(data):
    #itterate over data 
    for line in data:
        #identify pcb name line  
        if line.startswith("Pcb name"):
            #format line removing carrige return and spaces
            split = split_name(line)
            #remove 4.3mm from split list
            split.pop(0)
            #add F3 prefix to start of list 
            split.insert(0,"F1")
            return split
        
            
        
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
        #remove 4.3mm from split list
            split.pop(0)
        #add F3 prefix to start of list 
            split.insert(0,"F3")
        # IF value in line is a number - format number
            formatted_value = is_valid_number(split)
            fid_clean.append(formatted_value)

        # stop at [Bottom side] to exclude bottom-side components (v1 = top-side only)
        if line.startswith("[Bottom side]"):
            break
    return fid_clean

# retrieve component data 
def get_component_data(data):
    #store components data once formatted
        component_clean = []
        component_marker = False
        #itterate over data 
        for line in data:
            #use [Components] header as marker for identify start poitnt
            if line.startswith("[Components]"):
                component_marker = True
                # skip the header line itself, don't treat it as data
                continue  
            # stop at [Bottom side] to exclude bottom-side components (v1 = top-side only)
            if line.startswith("[Bottom side]"):
                break
            if line.startswith(";"):
                 # skip column header/comment line
                continue 
             # only process lines once inside the [Components] section not blank
            if component_marker and len(line) > 1:
               
                split = split_name(line)
                formatted_value = is_valid_number(split)
            # re-arrage order to match required output
            #--prefix--|---------X---------|---------Y---------|--------Angle------|0|Prio|-ID-|-Component name---|
            #    F8    |formatted_value[2] |formatted_value[3] |formatted_value[4] |0|  N |  N |formatted_value[1]|
          
                # build F8 line: prefix, X, Y, rotation, hardcoded "0 N N" fields (assumption, see notes), part name
                f8_value = ["F8", formatted_value[2], formatted_value[3], formatted_value[4], "0", "N", "N", formatted_value[1]]              
                component_clean.append(f8_value)
            #--prefix--|--Ref----|
            #   "F9"   |formatted_value[0] 
                # build F9 line: prefix, component reference (e.g. LED1)
                f9_value = ["F9", formatted_value[0]]
                component_clean.append(f9_value)
        return component_clean




# ************* helper functions ******************
# remove white space 
def split_name(line):
    # split line into fields on the "|" delimiter
    line_list = line.split("|")
    clean_list = []
    for word in line_list:
        # strip leading/trailing whitespace and newline chars
        remove_white_space = word.strip()
        # skip empty strings (e.g. trailing "|" with nothing after it)
        if len(remove_white_space):
           clean_list.append(remove_white_space)      

    return clean_list

#check if value is number
def is_valid_number(split):  
    #store new list item
    value_list = []   
    #itterat over line
    for value in split:
        # if value is number pass to convert to microns for formatting 
        try:
            # succeeds only if value is a valid number string
            is_float = float(value)
            # convert mm -> µm and store
            formatted_number = convert_to_microns(is_float)
            value_list.append(formatted_number)

        except ValueError:
            # not a number (e.g. label text) - keep as-is
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
def main():
    path = "test_files/LED-0134-001 iss 1.txt"
    # single disk read - lines reused by every extraction function below
    data = load_file(path)
    f1 = get_pcb_name(data)
    f3 = get_fiducials(data)
    # F4-F7 have no known meaning in source data (single sample, unresolved) - hardcoded as constants
    f4_to_f7 = [["F4", 0, 0,],["F5", 0, 0,],["F6", 0, 0,],["F7", 0, 0,],]
    f8_and_f9 = get_component_data(data)
    end_marker = ["E"]
    # use pcb name (f1[1]) as output filename
    save_name = f"{f1[1]}.pcb"
    # assemble all sections in required output order: F1, F3 x3, F4-F7, F8/F9 pairs, E
    file = [f1] + f3 + f4_to_f7 + f8_and_f9 + end_marker
    # open once, write every line while file stays open (avoids truncating on each write)
    with open(f"{save_name}", "w", encoding="utf-8") as f:
        for line in file:
            # convert each item to string and join with spaces to build the output line
            newline = " ".join(str(word) for word in line)
            f.writelines(f"{newline}\n")

main()