// adding template 
//
// USING gsl random number generator

#include "distributions.hpp"
#include <fstream>
#include <algorithm> // for std:min
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <omp.h>

using namespace std; 


int main()
{
  std::string s;
  std::stringstream out;

  //
  // initial guess, at step zero
  //
  double guess;
  double ratio; 
  
  double q = -10.7; 
  double qtilde;
  int acc = 0; // accepted samples 

  //
  // "greedyness"
  //
  double nu = 2.0;

  //
  // true mean and std. 
  //
  double mu  = -10.0;
  double std = 1.0;

  // file name strings
  //
  string base = "gauss";
  string end  = ".dat";
  string fl;
  

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

  // OMP\_GET\_NUM\_PROCS != OMP\_GET\_MAX\_THREADS 
  omp_set_num_threads(2);
  int chains = omp_get_max_threads();
  //int chains = 1;
  cout << "Running with " << chains << " OMP threads" << endl;

  //
  // number of mcmc steps
  //
  int steps = 1e7;
  int omp_steps = steps/chains;

  // -----------------------------------------------------------------
  // This block can be executed in parallel!!!!!!!!!!!!
  // -----------------------------------------------------------------

  //#pragma omp parallel for 
#pragma omp parallel for
  for(int j=0;j<chains;j++)
    {
      q = q + double(j);
      cout << "Beginning Markov Chain #" << j << endl;
      ofstream myfile;

      out << j;
      s = out.str();
      myfile.open ((base+s+end).c_str());     
      
      for(int i=0;i<steps;i++)
	{
	  // update mean and draw proposal 
	  qtilde = nu*nu*(sampleNormal())+q;
	  
	  // reject or accept?
	  guess = uniform();
	  ratio = std::max(std::min(gauss(mu,std,qtilde)/gauss(mu,std,q), 1.0),0.0);
	  
	  if(guess < ratio)
	    {
	      // accept!
	      q=qtilde;
	      acc++;
	    }
	  
	  myfile << q << endl;
	  
	}// done with mcmc loop
      myfile.close();  
    }
  
  //
  // print statistics
  //
  cout << "Generating Statistics" << endl;
  cout << "Acceptance Ratio " << ((double)(acc))/(chains*(double)(steps)) << endl;

  // steady as she goes...
  cout << "exiting with no errors" << endl;
  return(0);
}

//
// nick
// started: 11/14/14
//
