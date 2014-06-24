import quiz

def loadProblems(a):

  a.problems.append(quiz.Problem(
    "What is an adiabatic wall?",
    "No net heat transfer to or from the working fluid. (Insulated)",
    "B",
    "C",
    "A"))

  a.problems.append(quiz.Problem(
    "What is a control mass?",
    "A closed system: a volume that has no mass transfer.",
    "B",
    "C",
    "A"))
  
  a.problems.append(quiz.Problem(
    "What is Cp?",
    "Specific heat at constant pressure.",
    "B",
    "C",
    "A"))
  
  a.problems.append(quiz.Problem(
    "What is Cv?",
    "Specific heat at constant volume.",
    "B",
    "C",
    "A"))
  
  
  #
  # combustion 
  #
  
  a.problems.append(quiz.Problem(
    "What is a Rich mixture?",
    "A",
    "More fuel than stochiometric equilibrium. ",
    "More air than stochiometric.",
    "B"))
  
  a.problems.append(quiz.Problem(
    "What is the Damkoler number?",
    "A",
    "Ratio of the characteristic fluid time divided by the chemical reaction time.",
    "Ratio of the chemical reaction time divided by the characteristic fluid time.",
    "B"))
  
  a.problems.append(quiz.Problem(
    "What is a Rich mixture?",
    "A",
    "More fuel than stochiometric equilibrium. ",
    "More air than stochiometric.",
    "B"))
  
    
def main():
  a = quiz.App()
  loadProblems(a)    
  a.run()

# steady as she goes  
if __name__ == "__main__":
  main()

#
# nick 
# 4/20/14
#
