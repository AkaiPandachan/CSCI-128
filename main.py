'''
Docstring for CSCI-128-Combined_Create_Project.CSCI-128-main.main
'''
"""
permissions file format:
Program Name,Citizen Name,ID Number,Date of Birth,Mothers Maiden Name,Name of First Pet
{name},'Allowed','Allowed','Allowed','Not Allowed','Not Allowed'

"""



def get_perms(permissions_filename, program_name):
  '''
  Collects data permissions data from the file 'permissions_filename' for the program 'program_name'
  
  :param permissions_filename: Name of file containing data permissions info for several programs
  :param program_name: Name of program to collect data permissions for
  :return: Dictionary containing pairs of data type and program access level, ex: 
      {'Program Name':'Visitor Identification System', 'Citizen Name':'Allowed', 'ID Number':'Allowed', 'Mothers Maiden Name':'Not Allowed'}
  :rtype: list | None
  '''
  
  with open(permissions_filename) as f:
    permissions = f.readlines()
  for i in range(len(permissions)):
    permissions[i] = permissions[i].split(',')
  header = permissions[0]
  for line in permissions:
    if line[0] == program_name.strip().lower():
      return {header[i].strip():line[i].strip() for i in range(len(header))}



def collect_privacy_info(filename):
  '''
  Parses the file 'filename' and returns a list of identified types of data
  ie. citizen's name, id number, mother's maiden name, etc.
  
  :param filename: Name of 
  :return: Description
  :rtype: list | None
  '''
  
  pass



def audit(permissions_filename, programs):
  '''
  Docstring for audit
  
  :param permissions_filename: Name of the file containing permissions info for several programs
  :param programs: A list of the names of the programs needing to be audited
  :return: A list of lists containing the name of the file and the results for 
  :rtype: list | None
  '''
  
  results = {}
  for name in programs:
    perms = get_perms(permissions_filename, name)
    privacy_info = collect_privacy_info(name)
    result = []
    for i, data_type in enumerate(perms[1:]):
      pass
  data = 0
  audit_passed = False



'''
if __name__ == "__main__":
  perms = input('Permissions File> ').strip()
  num_programs = int(input("Number of Programs> "))
  names = []
  for i in range(num_programs):
    names.append(input(f'Name {i+1}> ').strip())
'''




#'''
#get_perms test:
program = 'quantum_cryptography_model'
perms_filename = 'CSCI-128-Combined_Create_Project/CSCI-128-main/perms1.csv'
permissions = get_perms(perms_filename, program)
print(type(permissions))
for key, entry in permissions.items():
  print(key + ': ' + entry)    
'''prints:
{
'Program Name':'quantum_cryptography_model',
'Citizen Name':'Allowed',
'ID Number':'Allowed',
'Date of Birth':'Allowed',
'Mothers Maiden Name':'Not Allowed',
'Name of First Pet':'Not Allowed',
'Social Score':'Not Allowed',
'Credit Balance':'Not Allowed'
}
'''




'''
Main Test
Inputs:
Permissions File> perms1.csv
Number of Programs> 1
Name 1> quantum_cryptography_model


Outputs:
file: results.txt
contents: 
quantum_cryptography_model: Failed
Unauthorized Data Type: Credit Balance
'''