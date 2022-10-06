
def arithmetic_arranger(problems, *args):
  'This function takes a list of arithmetic problems and reformats them in a specific way'
  
  max_problems = 5
  max_digits = 4
  valid_operators = ["+", "-"]
  calculations = [] # holds all final calculations
  space_between_columns = " " * 4
  arranged_problems = '' # holds the string with the final result

  if len(problems) > max_problems: return "Error: Too many problems."
  
  for count, pair in enumerate(problems):
      calculations.append(pair.split(' '))
      if calculations[count][1] not in valid_operators: return "Error: Operator must be '+' or '-'." 
      try:
        'Check if digits are given'
        calculations[count].append(eval(pair)) # calculates the output of the operation
      except:
        return "Error: Numbers must only contain digits."
      if len(calculations[count][0]) > max_digits or len(calculations[count][2]) > max_digits: return "Error: Numbers cannot be more than four digits."
      calculations[count].append(len(max(pair.split(' '), key=len))) # finds the longest number in terms of digits, this is needed for formatting

  # the following 3 loops add one line of formatted output into arranged_problems string

  for line_one in calculations:
    arranged_problems += f"{line_one[0]:>{line_one[4]+2}}{space_between_columns}"
  arranged_problems = arranged_problems.rstrip() # removes white space after the last line

  arranged_problems += "\n"

  for line_two in calculations:
    arranged_problems += f"{line_two[1]:<2}{line_two[2]:>{line_two[4]}}{space_between_columns}"
  arranged_problems = arranged_problems.rstrip()

  arranged_problems += "\n"

  for line_three in calculations:
    divider = "-" * (line_three[4]+2)
    arranged_problems += f"{divider}{space_between_columns}"
  arranged_problems = arranged_problems.rstrip()

  if len(args)!= 0 and args[0] == True:
    'Check if the optional parameter was passed'

    arranged_problems += "\n"

    for line_four in calculations:
      arranged_problems += f"{line_four[3]:>{line_four[4]+2}}{space_between_columns}"
    arranged_problems = arranged_problems.rstrip()
  return arranged_problems