import sys, ntpath, csv

def get_list():
    return_list = []
    try:
        if len(sys.argv) > 1:
            return_list = read_from_csv(sys.argv[1])
        elif input("Get file? (y/n): ") == "y":
            return_list = read_from_csv(input("Input file: "))
        else:
            return_list = [input("Single input: ").replace(" ", "").split(',')]
    finally:
        return return_list

def get_list_and_file():
    return_list = []
    return_file = None
    try:
        if len(sys.argv) > 1:
            return_file = sys.argv[1]
            return_list = read_from_csv(return_file)
        elif input("Get file? (y/n): ") == "y":
            return_file = input("Input file: ")
            return_list = read_from_csv(return_file)
        else:
            return_list = [input("Single input: ").replace(" ", "").split(',')]
    finally:
        return return_list, return_file

def read_from_csv(csv_file):
    '''Turns a CSV file into a list.'''
    csv_file = csv_file.replace('"', '')
    try:
        return_list = list()
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                return_list.append(row)
            return return_list
    except IOError as e:
        print("I/O error({0} : {1})".format(e.errno, e))
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError: {0}".format(e))
    finally:
        return return_list
    
def write_to_csv(filename, content):
    '''Turns a list into a CSV file.'''
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in content:
            writer.writerow(row)
            
def save_file(data, addname="_output", name=None, prompt=True):
    if not prompt or input("Save file? (y/n): ") == "y":
        if len(sys.argv) > 1:
            filename = sys.argv[1]
        elif name == None:
            filename = "{}\\{}".format(ntpath.split(sys.argv[0])[0], input("Output name: ") + ".csv")
        else:
            filename = "{}\\{}".format(ntpath.split(sys.argv[0])[0], name + ".csv")
        head, tail = ntpath.split(filename)
        new_filename = "{}\\{}{}{}".format(head, tail[:len(tail)-4], addname, tail[len(tail)-4:])
        write_to_csv(new_filename, data)
        return new_filename

def get_token(filename):
    '''Opens a file and returns the first line of the file.'''
    f = open("{}".format(filename))
    token = f.readline()
    f.close()
    return token
