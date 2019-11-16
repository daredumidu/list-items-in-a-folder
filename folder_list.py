import os.path

master_path = 'C:\\VM_Reports\\CTI_WEEKLY_REPORTS\\scheduled\\'
#master_path = 'C:\\VM_Reports\\CTI_WEEKLY_REPORTS\\2019-11-13\\scheduled-new\\'


folder_name = os.listdir(master_path)           # list ltems in folder.

#print (folder_name)

with open('list.txt', 'w') as f:                # get the list to a txt file.
    for item in folder_name:
        f.write("%s\n" % item)