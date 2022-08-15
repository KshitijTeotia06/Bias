import xmltodict
import os



resdict = {}

id = 0
countWork = 0
countNoWork = 0


directory = 'search_result'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    with open(f) as fd:
        try:
            id += 1
            doc = xmltodict.parse(fd.read())
            listOfPatients = doc["clinical_study"]["clinical_results"]["baseline"]["measure_list"]["measure"][1]["class_list"]["class"]["category_list"]["category"]
            # print(type(listOfPatients))
            obj = {}
            for elm in listOfPatients:
                # print(listOfPatients)
                label = elm["title"]
                measurementList = elm["measurement_list"]["measurement"]
                sum = 0
                for i in measurementList:
                    # print(i["@value"])
                    sum += int(i["@value"])
                obj[label] = sum
                # print(measurementList)
                # print(listOfPatients["class"])
                # print(listOfPatients["class_list"])
                # print("finished")
            resdict[id] = obj
            countWork += 1
        except:
            print("ERROR WITH FILE ID ", id)
            countNoWork += 1
    # print(id)

print(resdict)
print()
print("Processed ", countWork, " files successfully")
print("Was not able to process ", countNoWork, " files")