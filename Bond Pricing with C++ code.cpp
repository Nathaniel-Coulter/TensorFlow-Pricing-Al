//  main.cpp 

//  DiscreteBondPrice 

// 

//  Created by Brian Byrne on 10/12/2015. 

 

#include <cmath> 

#include <iostream> 

using namespace std; 

 

double PVB(double Face,double cr,double r,int m, double T) 

{ 

    // store the value of the bond 

    double BV=0.; 

    // add in coupons 

    int TNC=T*m; 

    double cpn = (cr/m)*Face; 

    for(int i=1;i<=TNC; i++) 

	{ 

        double ti=double(i)/double(m); 

    	BV = BV + cpn*pow((1+r/m),-ti*m); 

         

	} 

    // finally add principle 

     

	BV = BV + Face*pow((1+r/m),-T*m); 

    return BV; 

} 

 

int main() 

{ 

    double Face = 100; 

    double cr = 0.1; 

    double r =0.1; 

    int m = 2; 

    double T =3; 

     

    cout << " The Present Value of the Discrete bond is " << PVB(Face, cr, r, m, T) <<endl; 

    system ("PAUSE"); 

     

} 