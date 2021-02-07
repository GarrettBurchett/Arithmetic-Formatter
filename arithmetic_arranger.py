def arithmetic_arranger(problems, show_solution=False):
    """
    Will take a list of arithmetic problems and arrange 
    them as they would appear on a grade school assignment
    sheet. The solution will also appear if show_solution is set to True. 

    Only addition and subtraction are valid operators, no number can be greater than 4 digits long, and there can be no more than 5 arithmetic problems entered.
    
    Example: '32 + 8'
    
    Output:   32
            +  8
            ----
    """
    # Can't have more than 5 problems input
    if len(problems) > 5:
      return "Error: Too many problems."
    
    # Create lists to store all of our values
    top_nums, bottom_nums, operators = [], [], []
    results, dashes = [], [] 
    arranged_top, arranged_bottom, arranged_result = [], [], []

    # Loop through the input problems and sort each piece of information into the proper empty list created above.
    for problem in problems:
      entry = problem.split() # This should create a list of [num1, operator, num2]
      
      # Check both entry[0] and entry[2] are numeric and store there values if so.
      if entry[0].isnumeric() and entry[2].isnumeric():
        top_nums.append(entry[0])
        bottom_nums.append(entry[2])
      else:
        return "Error: Numbers must only contain digits."

      # Check the operator is valid.
      if entry[1] in ['+', '-']:
        operators.append(entry[1])
      else:
        return "Error: Operator must be '+' or '-'."
      
      # Calculate the result of the arithmetic problem.
      if entry[1] == '+':
        results.append(int(entry[0]) + int(entry[2]))
      elif entry[1] == '-':
        results.append(int(entry[0]) - int(entry[2]))

      # Check if either number is > 4 digits and get the number of dashes.
      if len(entry[0]) > 4 or len(entry[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
      elif len(entry[0]) >= len(entry[2]):
        dashes.append('-' * (len(entry[0]) + 2))
      else: 
        dashes.append('-' * (len(entry[2]) + 2))

    # Format the top number, operators with the bottom numbers, and the results of each equation.
    for i in range(len(problems)):
      right_aligned_top_num = top_nums[i].rjust(len(dashes[i]))
      right_aligned_bottom_num = operators[i] + ' ' + bottom_nums[i].rjust(len(dashes[i]) - 2)
      right_aligned_result = str(results[i]).rjust(len(dashes[i]))
      
      arranged_top.append(right_aligned_top_num)
      arranged_bottom.append(right_aligned_bottom_num)
      arranged_result.append(right_aligned_result)

    # Align each part of the arithmetic problem so that they are separated by 4 space or tab.
    formatted_top_nums = '    '.join(arranged_top)
    formatted_bottom_nums = '    '.join(arranged_bottom)
    formatted_dashes = '    '.join(dashes)
    formatted_results = '    '.join(arranged_result)

    # Display the correct arithmetic format based on if show_solution is displayed as True or not.
    if show_solution: 
      return f"{formatted_top_nums}\n{formatted_bottom_nums}\n{formatted_dashes}\n{formatted_results}"
    else:
      return f"{formatted_top_nums}\n{formatted_bottom_nums}\n{formatted_dashes}"