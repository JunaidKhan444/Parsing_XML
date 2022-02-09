#Importing ElementTree 
import xml.etree.ElementTree as ET
#Importing CSV Lib
import csv
#Function to Parse Nested/Single Element
def analyser(sub):
    d = []
    count = 0
    if sub.text == None:
        return ' '
    else:
        for x in sub.iter():
            count = count + 1
            d.append(str(x.text))
        if count == 1:
            return ''.join(d)
        else:
            #removed_spaces = [i.strip() for i in d ]
            del d[0]
            rt = '|'.join(d)
            return rt
    


#Creating Element Tree
tree = ET.parse("SearchResults.xml")
#Root Element
root = tree.getroot()


# open a file for writing
xml_data = open('xml_data.csv', 'w')

# Creating Writing Header on CSV file
csvwriter = csv.writer(xml_data)

# Making a list of Header
file_headers = [x.tag for x in root[1]]
#print(file_headers)

#file_headers = ['nct_id', 'title', 'acronym', 'status', 'study_results', 'conditions', 'interventions', 'outcome_measures', 'sponsors', 'gender', 'min_age', 'max_age','age_groups', 'phases', 'enrollment', 'funded_bys', 'study_types', 'exp_acc_types', 'study_designs', 'other_ids', 'start_date', 'primary_completion_date', 'completion_date', 'study_first_posted', 'last_update_posted', 'locations', 'documents', 'url']

# Displaying the Number of Header
#print(len(file_headers))

# Writing Headers on CSV file
csvwriter.writerow(file_headers)

# Accessing Children of Root Element
for child in root:
    data = []
    #print(child.attrib)
    # Accessing Sub-Children of Children Nodes
    for sub_child in child:
        #print(sub_child)
        # Parsing Each Sub-Children Tag
        dt = analyser(sub_child)
        # Appending Children Text 
        data.append(dt)
    # Writing Children Text to File    
    csvwriter.writerow(data)

# Closing the File        
xml_data.close()

     