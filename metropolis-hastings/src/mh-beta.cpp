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
  
  double q = 0.4; 
  double qtilde;
  int acc = 0; // accepted samples 

  //
  // "greedyness"
  //
  double nu = 0.1;

  //
  // number of mcmc steps
  //
  int steps = 1e5;

  // beta params
  double a = 2.0;
  double b = 5.0;
     
  //
  // begin markov chain steps
  //  
  cout << "Beginning Markov Chain" << endl;
  ofstream myfile;
  myfile.open ("beta.dat");

  for(int i=0;i<steps;i++)
    {
      // update mean and draw proposal 
      qtilde = nu*nu*(sampleNormal())+q;
      //cout << "qtilde " << qtilde << endl;

      // reject or accept?
      guess = uniform();      
      ratio = std::max(std::min(beta(qtilde,a,b)/beta(q,a,b), 1.0),0.0);
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
