// adding template 
//
// USING gsl random number generator

#include "distributions.hpp"
#include <fstream>
#include <algorithm> // for std:min

using namespace std; 

int main()
{
  //
  // initial guess, at step zero
  //
  double guess;
  double ratio; 
  
  double q = -2.7; 
  double qtilde;
  int acc = 0; // accepted samples 

  //
  // "greedyness"
  //
  double nu = 3.0;

  //
  // true mean and std. 
  //
  double mu  = -10.0;
  double std = 1.0;

  //
  // number of mcmc steps
  //
  int steps = 1e5;

  //
  // need to sanity check initial guess!
  //
  if(gauss(mu,std,q) < 1e-12)
    {
      cout << "Bad initial guess, results are unreliable" << endl;
      cout << gauss(mu,std,q) << endl;
      exit(1);
    }
     
  //
  // begin markov chain steps
  //  
  cout << "Beginning Markov Chain" << endl;
  ofstream myfile;
  myfile.open ("gauss.dat");

  for(int i=0;i<steps;i++)
    {
      // update mean and draw proposal 
      qtilde = nu*nu*(sampleNormal())+q;

      // reject or accept?
      guess = uniform();
      ratio = std::max(std::min(gauss(mu,std,qtilde)/gauss(mu,std,q), 1.0),0.0);
      //cout << "guess " << guess << " ratio: " << ratio << std::endl;

      if(guess < ratio)
	{
	  // accept!
	  q=qtilde;
	  acc++;
	}

      myfile << q << endl;

    }// done with mcmc loop
  myfile.close();  

  //
  // print statistics
  //
  cout << "Generating Statistics" << endl;
  cout << "Acceptance Ratio " << ((double)(acc))/((double)(steps)) << endl;

  // steady as she goes...
  cout << "exiting with no errors" << endl;
  return(0);
}

//
// nick
// started: 11/14/14
//
