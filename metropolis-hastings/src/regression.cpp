//
//
// a suite of tests available through 'make check'
//
//
#include "distributions.hpp"

using namespace std; 

int main()
{
  // 
  // evaluate at a few points on a uniform distribution
  //
  int len = 10000;
  double thresh = 1e-5;
  double proposal;

  cout << "Testing uniform distribution draws..." << endl;
  for(int i=0;i<len;i++)
    {
      proposal = uniform();
      if(proposal < 0 | proposal > 1.0) 
	{
	  cout << "regression test failure!" << endl;
	  cout << "The uniform distribution is not being evaluated properly!" << endl;
	  return(1);	  
	}
    }  

  // 
  // evaluate at a few points on a gaussian we know the correct answer 
  //
  cout << "Testing gaussian distribution draws..." << endl;
  if(fabs(gauss(0.0,1.0,0.0) - 0.398942) > thresh)
    {
      cout << "regression test failure!" << endl;
      cout << "The gaussian distribution is not being evaluated properly!" << endl;
      return(1);
    }


  // steady as she goes
  cout << "All tests passed! Congratulations. Have a Markovian Day." << endl;
  return(0);
}

//
// nick 
// 11/14/14
//
