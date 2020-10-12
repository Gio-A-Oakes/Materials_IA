import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image
from ipywidgets import interact


def Create_alloy(N, Xa, n, T, E):
    """
     A random alloy is represented as a 2 dimensional lattice gas in which
     alloying atoms can exchange position with matrix atoms using the
     Metropolis alogorithm. The purpose is to show how alloys become more
     random as the temperature increases.
 
 
     :param N: Size of square matrix
     :param Xa:The fraction of sites occupied by A atoms
     :param n: The number of iterations
     :param T: The temperature (K)
     :param E: A-B interaction energy (eV)
     
     :return alloy: final configuration of A and B atoms

    """
    # Create initial random matrix
    n_a, n_b = int(N**2*Xa), int(N**2*(1-Xa))
    alloy = np.random.permutation(np.append(np.ones(n_a), np.zeros(n_b))).reshape(N,N)
    for i in range(n):
        alloy = MC_swap(alloy, N, E, T)
    return alloy

def MC_swap(alloy, N, E, T):
    """
    Randomly selects an atom and one of its neighbours in a
    matrix and calculates the change in energy if the two atoms were swapped.
    
    The following assignment is used to represent the neighbouring directions:

    1 = up
    2 = right
    3 = down
    4 = left
    """
    
    kT = 8.617332*10**-5*T
    random_atom = np.random.randint(0,N,2)
    atom1 = alloy[random_atom[0],random_atom[1]]
    random_neighbour = np.random.randint(1,5,1)
    
    # Select appropriate neighbour
    if random_neighbour==1:
        row2=(random_atom[0]-2)%N
        column2 = random_atom[1]
    elif random_neighbour==2:
        row2 = random_atom[0]
        column2 = (random_atom[1])%N
    elif random_neighbour==3:
        row2 = (random_atom[0])%N
        column2 = random_atom[1]
    else:
        row2 = random_atom[0]
        column2 = (random_atom[0]-2)%N
    atom2 = alloy[row2, column2]
    
    if atom1==atom2:
        e=0
    else:
        # Need to calculate the energy before and after atom one and two swap
        # Atom 1
        up1= (random_atom[0]-2)%N
        down1 = (random_atom[0]%N)
        left1 = (random_atom[1]-2)%N
        right1 = (random_atom[1]%N)
        # Atom 2
        up2=(row2-2)%N
        down2=(row2%N)
        left2=(column2-2)%N
        right2=(column2%N)

        # Change in energy
        Bonds1 = alloy[down1, random_atom[1]] + alloy[up1, random_atom[1]] + alloy[random_atom[0], right1] + alloy[random_atom[0], left1]
        Bonds2 = alloy[down2, column2] + alloy[up2, column2] + alloy[row2, right2] + alloy[row2, left2]
        
        # Count number of A-B bonds for atoms 1 and 2
        if atom1==0:
            Initial1=Bonds1
            End1=4-Bonds1
            Initial2=4-Bonds2
            End2=Bonds2
        else:
            Initial1=4-Bonds1
            End1=Bonds1
            Initial2=Bonds2
            End2=4-Bonds2
        e = E*(End1+End2-Initial1-Initial2) # Energy difference for swapping atoms
    #Swapping atoms if there is enough energy to do so
    if e<0:
        alloy[random_atom[0],random_atom[1]]=atom2
        alloy[row2, column2]=atom1
    elif np.exp(-e/kT)>np.random.uniform(0,1):
        alloy[random_atom[0],random_atom[1]]=atom2
        alloy[row2, column2]=atom1
    return alloy

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def test2D(alloy, N, Xa):
    """
    Imports the final configuration of alloy and counts the number of A atoms that are neighboured by 0, 1, 2 and 4 B atoms.
    It then plots the the given statistics as a hystogram, which can be used to analyse how random the distribution is
    """
    #Calculating the number of different neighbours
    # Set up an array for counting number of A-B bonds
    n_a, n_b, prob = np.zeros(5), np.zeros(5), np.zeros(5)
    
    for i in range(N):
        for j in range(N):
            # find indacies of up, down, left and right
            up = i - 2 % N
            down = i % N
            left = j - 2 % N
            right = j % N
            # Count number of neighbouring ones
            bond = int(alloy[down,j]+alloy[up,j]+alloy[i,right]+alloy[i,left])
            if alloy[i,j]==0:
                n_a[bond] = n_a[bond] + 1
            else:
                n_b[bond] = n_b[bond] + 1
                
    n=n_a+np.flip(n_b) # Total number of A atoms neighboured by B atoms  
    
    #Calculate the the distribution obtained if the atoms were arranged randomly, i.e. Binomial distribution   
    for i in range(len(prob)):
        Con=nCr(4,i)
        Frac=Xa*Xa**(4-i)*(1-Xa)**i+(1-Xa)*Xa**i*(1-Xa)**(4-i)
        prob[i] = Con*Frac*abs(N)**2

    # Plot bar chart    
    labels = ['0', '1', '2', '3', '4']
    x = np.arange(len(labels))
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, n, width, label='Simulation Result')
    rects2 = ax.bar(x + width/2, prob, width, label='Binomial Distribution')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Frequency')
    ax.set_title('Number of neighbouring points')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
class PDF(object):
  def __init__(self, pdf, size=(200,200)):
    self.pdf = pdf
    self.size = size

  def _repr_html_(self):
    return '<iframe src={0} width={1[0]} height={1[1]}></iframe>'.format(self.pdf, self.size)

  def _repr_latex_(self):
    return r'\includegraphics[width=1.0\textwidth]{{{0}}}'.format(self.pdf)

