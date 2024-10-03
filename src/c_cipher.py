import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

"""
    Name:    Cassidy Goss
    Date:    20240930
    Course Number:    138
    Class Section:    EN
"""

def encrypt(email):
    """
    TODO: What is the objective? 
    The objective is to encrypt the email variable with the pseudocode shifting each element up three.
    Args:
        TODO: what arguments and data types are expected? (i.e., email)
    The expected arguments are "new_ascii" which updates the element, and shift it down three. 
    "email_lst" converts the ascii into a string. 
    "len_flag" which validates the length of the variable "email"
    The data types expected are string for the email variable. Boolean for the anum_flag.
    Returns:
        TODO: what varibale and data types are being returned?   
    #The variable returned is after the psuedocode is implemented changing the email variable to shift up three. The expected data type is a string.
    """
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = not email[:3].isalpha() or not email[3:].isdigit() 

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    email_lst = list(email)
        
    # TODO: complete line(s) below, convert EACH new element into a string
    new_ascii = ord(email_lst[0]) + 3    # NOTE: here we extract and update element at 0 
    email_lst[0] = chr(new_ascii)   # NOTE: here we convert our ASCII into string
    
    new_ascii = ord(email_lst[1]) + 3    # NOTE: here we extract and update element at 1 
    email_lst[1] = chr(new_ascii)   
    
    new_ascii = ord(email_lst[2]) + 3    # NOTE: here we extract and update element at 2 
    email_lst[2] = chr(new_ascii)    
    
    new_ascii = ord(email_lst[3]) + 3    # NOTE: here we extract and update element at 3 
    email_lst[3] = chr(new_ascii) 
    
    new_ascii = ord(email_lst[4]) + 3    # NOTE: here we extract and update element at 4 
    email_lst[4] = chr(new_ascii)    
    
    new_ascii = ord(email_lst[5]) + 3    # NOTE: here we extract and update element at 5 
    email_lst[5] = chr(new_ascii)  
        
    # TODO: fix line below, convert list into a string
    email_str = ''.join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email):
    """
    TODO: What is the objective? 
    #The objective is to apply the decrypt pseudocode to email and shift down three. 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)
    #The expected arguments are "new_ascii" which updates the element, and shift it down three. 
    # "email_lst" converts the ascii into a string. 
    #"len_flag" which validates the length of the variable "email"
    #The data types expected are string for the email variable. Boolean for the anum_flag.

    Returns:
        TODO: what varibale and data types are being returned?   
    #The variable returned is after the psuedocode is implemented changing the email variable to shift down three. The expected data type is a string. 
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = not (email[:3].isalpha() or not email[3:].isdigit())

    if len_flag:                         # input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    #string into a list.
    email_lst = list(email)

    # TODO: apply the encrypt pseudocode but shift down 3
    new_ascii = ord(email_lst[0]) - 3    # NOTE: here we extract and update element at 0 
    email_lst[0] = chr(new_ascii)        # NOTE: here we convert our ASCII into string
    
    new_ascii = ord(email_lst[1]) - 3    # NOTE: here we extract and update element at 1 
    email_lst[1] = chr(new_ascii)   
    
    new_ascii = ord(email_lst[2]) - 3    # NOTE: here we extract and update element at 2 
    email_lst[2] = chr(new_ascii)    
    
    new_ascii = ord(email_lst[3]) - 3    # NOTE: here we extract and update element at 3 
    email_lst[3] = chr(new_ascii) 
    
    new_ascii = ord(email_lst[4]) - 3    # NOTE: here we extract and update element at 4 
    email_lst[4] = chr(new_ascii)    
    
    new_ascii = ord(email_lst[5]) - 3    # NOTE: here we extract and update element at 5 
    email_lst[5] = chr(new_ascii)  
    
    email_str = ''.join(email_lst)
    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email
    return retVal
