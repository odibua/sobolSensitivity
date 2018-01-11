# Generalized Polynomial Chaos Expansion (PCE) for Sobol Indices

This folder performs sensitivity analysis through the sobol indices. This analysis includes both the sensitivity 
of individual inputs and their interactions. In this case, the generalized PCE is constructed using sparse grid
quadratures (smolyak). This process follows the work done in [1].

[1] T. Crestaux, O. Maitre, J-M Martinez, "Polynomial Chaoes expansion for sensitivity analysis," 
    Reliability Engineering and System Safety, 2008 https://www.sciencedirect.com/science/article/pii/S0951832008002561
    
# Testing the function

The file testPCEMethod tests our code on functions with analytical solutions. The user can run this test function in python
from the terminal in the following block of code:

    chooseFunc = sys.argv[1]; p = int(sys.argv[2]); level=int(sys.argv[3]); d=int(sys.argv[4]);
  
The inputs are the function to be tested, the maximum power of an individual polynomial basis, the level of accuracy of
of the sparse integral for a given dimension of the input, and d the dimension of the input. The valid functions are those
in the string below:

    testFuncArr = ['ishigamiFundamental','ishigamiComplex']
  
The block of code below creates a generalized PCE for the function of interest using sparse grid integration.

    beta,polynomial,nodes,weights,powList,integralArr = genPCEIntegral(p,d,level,customLegendre,funcUse);
  
Finally, the below block of code calculates the sobol indices.

      #Declares class that will be used to calculate sobol indices.
      sobolClass = sobolIndices();
      ###
      #Calculates sobol indices, total sobol indices, and total variance. 
      sobolCache,sobolTotalCache,sTot = sobolClass.genSobolPCE(beta,nodes,weights,powList,customLegendre,integralArr)

