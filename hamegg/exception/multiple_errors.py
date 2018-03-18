dict_input = {"data":"AAA"}

try:
    f = open("non-existingFile.txt", 'rw')
    data = dict_input['data']
    f.write(data)
    f.close()
except KeyError:
    print "KeyError!"
except (IOError, TypeError):
    print "cannot open file"
except:
    print "other errors"