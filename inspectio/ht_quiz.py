import quiz

def loadProblems(a):

  a.problems.append(quiz.Problem(
    "What is the Schmidt Number?",
    "I don't know.",
    "A non-dimensional ratio of the product of the velocity and the length scale, divided by the viscosity.",
    "The ratio of momentum diffusivity (viscosity) and mass diffusivity,",
    "C"))  

  a.problems.append(quiz.Problem(
    "What is the Peclet Number?",
    "I don't know.",
    "A non-dimensional ratio of the product of the velocity and the length scale, divided by the viscosity.",
    "LU/alpha: advection transport divided by diffusive transport",
    "C"))  
    
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
