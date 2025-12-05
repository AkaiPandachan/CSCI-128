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
  header = permissions[0]
  for line in permissions:
    if line[0] == program_name.strip().lower():
      return {header[i]:line[i] for i in range(len(header))}



def collect_privacy_info(filename):
  '''
  Docstring for collect_privacy_info
  
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




if __name__ == "__main__":
  num_programs = int(input("Enter the number of programs to be audited: "))
  names = []
  for i in range(num_programs):
    names.append(input('Enter the name of a program: ').strip())
  
  