// misc routines 
//

#include "distributions.hpp"
#include "math.h" // for RAND, and rand, and tgamma

//
// Box-Muller algo for random gaussian draws
//
double sampleNormal() 
{
  double u = ((double) rand() / (RAND_MAX)) * 2 - 1;
  double v = ((double) rand() / (RAND_MAX)) * 2 - 1;
  double r = u * u + v * v;
  if (r == 0 || r > 1) return sampleNormal();
  double c = sqrt(-2 * log(r) / r);
  return u * c;
}

double uniform()
{
  return rand()*1.0 /RAND_MAX;
}

double gauss(double mu, double sigma, double x)
{
  double a = 1/(sigma*sqrt(2*M_PI)) * exp(-pow((x-mu),2)/(2*sigma*sigma));
  return a;
}

double beta(double x, double a, double b)
{
  if(a<0)
    {
      std::cout << "error! a<0!" << std::endl;
      exit(1);
    }

  if(b<0)
    {
      std::cout << "error! b<0!" << std::endl;
      exit(1);
    }

  if(1.0<x || x<0.0)
    {
      //std::cout << "error! x not between [0,1]" << std::endl;
      //std::cout << x << std::endl;
      //exit(1);
      return 0;
    }

  return tgamma(a+b)/(tgamma(a)*tgamma(b)) * pow(x,(a-1.0)) * pow((1-x),(b-1.0));
}

//
// nick 
// 
//
