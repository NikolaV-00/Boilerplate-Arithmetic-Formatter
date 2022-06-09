def arithmetic_arranger(problems, answers=False):
    lineOnePrint = ''
    lineTwoPrint = ""
    dashesPrint = ''
    solutionLinePrint = ''

    # if the number of problems is more than five
    # return the error
    if len(problems) > 5:
        return "Error: Too many problems."

    # read each problem, one by one
    for problem in problems:
        # split the problem to find operation and numbers
        specificProblem = problem.split()
        firstNum = specificProblem[0]
        secondNum = specificProblem[2]
        operation = specificProblem[1]

        # return an error if numbers have more than four digits
        if len(firstNum) > 4 or len(secondNum) > 4:
            return "Error: Numbers cannot be more than four digits."

        # convert strings into floating point numbers
        # return a message if strings contain some
        # character other than digits
        try:
            numOne = float(firstNum)
            numTwo = float(secondNum)
        except ValueError:
            return "Error: Numbers must only contain digits."

        # If the operation is either '+' or '-'
        # do the appropriate calculations
        # return an error otherwise
        if operation == '+' or operation == '-':
            if operation == '+':
                solution = numOne + numTwo
            else:
                solution = numOne - numTwo
        else:
            return "Error: Operator must be '+' or '-'."
        solution = int(solution)

        # length of dashes will be the length of
        # the larger number plus two
        if len(firstNum) > len(secondNum):
            dashLength = len(firstNum) + 2
        else:
            dashLength = len(secondNum) + 2

        # line one will be aligned to the right
        # line two will have the number aligned to the right
        # and the appropriate operation the left
        # number of dashes was defined previously
        # solution will be aligned to the right as well
        lineOne = firstNum.rjust(dashLength)
        lineTwo = operation + secondNum.rjust(dashLength - 1)
        dashes = '-' * dashLength
        solutionLane = str(solution).rjust(dashLength)

        # if the problem is the last one
        # it will not have spaces after lines
        # otherwise they will
        if problem == problems[-1]:
            lineOnePrint += lineOne
            lineTwoPrint += lineTwo
            dashesPrint += dashes
            solutionLinePrint += solutionLane
        else:
            lineOnePrint += lineOne + '    '
            lineTwoPrint += lineTwo + '    '
            dashesPrint += dashes + '    '
            solutionLinePrint += solutionLane + '    '

    # each of the lines will be displayed in new line
    # if the answer is 'True' solution will be displayed
    if answers:
        arranged_problems = lineOnePrint + '\n' + lineTwoPrint + '\n' + dashesPrint + '\n' + solutionLinePrint
    else:
        arranged_problems = lineOnePrint + '\n' + lineTwoPrint + '\n' + dashesPrint

    return arranged_problems