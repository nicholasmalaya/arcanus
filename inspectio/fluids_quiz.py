import quiz

def loadProblems(a):

  a.problems.append(quiz.Problem(
    "What is the Reynolds Number?",
    "I don't know.",
    "A non-dimensional ratio of the product of the velocity and the length scale, divided by the viscosity.",
    "The ratio of momentum diffusivity (viscosity) and mass diffusivity,",
    "B"))

  a.problems.append(quiz.Problem(
    "What is the momentum thickness?",
    "The transverse distance by which the boundary should be displaced to compensate for the reduction in momentum of the flowing fluid on account of boundary layer formation.",
    "B",
    "C",
    "A"))
  
  a.problems.append(quiz.Problem(
    "What is the drag equation?",
    "A",
    "B",
    "C",
    "A"))
  
  a.problems.append(quiz.Problem(
    "What is Bernoulli's equation?",
    "A",
    "B",
    "C",
    "A"))
  
  a.problems.append(quiz.Problem(
    "What are the assumptions underlying the bernoulli equation?",
    "Steady state flow, no friction, constant density, points are on streamline.",
    "B",
    "C",
    "A"))

  a.problems.append(quiz.Problem(
    "What does Eulerian Method imply?",
    "Fixed points in space.",
    "B",
    "C",
    "A"))

  a.problems.append(quiz.Problem(
    "What does Lagrangian Method imply?",
    "Following particles as they move.",
    "B",
    "C",
    "A"))

  a.problems.append(quiz.Problem(
    "What are the units of viscosity (kinematic)?",
    "meters squared per second.",
    "B",
    "C",
    "A"))

  a.problems.append(quiz.Problem(
    "What is a steamline?",
    "A line that is everywhere tangent to the velocity field.",
    "B",
    "C",
    "A"))
  
  a.problems.append(quiz.Problem(
    "What is the material derivative?",
    "D()/Dt = d()/dt + u d()/dx + v d()/dy + w d()/dz",
    "B",
    "C",
    "A"))


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
