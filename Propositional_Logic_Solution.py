
from Agent import * # See the Agent.py file
from pysat.solvers import Glucose3

#### All your code can go here.

#### You can change the main function as you wish. Run this program to see the output. Also see Agent.py code.

#Use the satsolver. Put the new found clauses into the model and then to determine whether the agent
#can percieve gold or not by putting not of the gold clause into the model and see if its satisfiable
#If unsatisfiable- gold is present else not.
#Do this until no new safe cells can be inferred by the algo.
#For going from 1 safe cell to another, use BFS for finding the path.
#Query the KB as KB.add_clause(Mine(x,y)) and solve(KB). If this returns unsatisfiable,then Mine cannot be present at (x,y) and therefore (x,y) is a safe cell.  

#1-25 -: correspond to locations
#1-25 -: correspond to mines in those locations
#26-50 -: correspond to percept = 0 in corresponding locations.
#51 - 75 -: percept =4 in corresponding locations
#76-100 -: percept =1 in the corresponding locs
#101-125 -: percept = 3 in the corresponding locs.
#126-150 -: percept = 2 in their corresponding locs.
#151 for Gold

def get_key(val,my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
 
    return None



def main():
    kb = Glucose3()

    mapping = {}
    cells = 1
    for i in range(5):
        for j in range(5):
            mapping[j+1,i+1] = cells
            cells+=1



    
    # percept(x,y) = 0 <-> ~Mine(x+1,y) and ~Mine(x-1,y) and ~Mine(x,y+1) and ~Mine(x,y-1)
    clauses = []


    for i in range(25):
        loc = get_key(i+1,mapping)
        x = loc[0]
        y = loc[1]
        percept0 = 26 +i
    
        if (x-1==0 and y-1==0):
            kb.add_clause([-percept0,-6])
            kb.add_clause([-percept0,-2])
            kb.add_clause([percept0,6,2])
            clauses.append([-percept0,-6])
            clauses.append([-percept0,-2])
            clauses.append([percept0,6,2])
            
            
        elif (x+1==6 and y-1==0):
            kb.add_clause([-percept0,-4])
            kb.add_clause([-percept0,-10])
            kb.add_clause([percept0,4,10])
            clauses.append([-percept0,-4])
            clauses.append([-percept0,-10])
            clauses.append([percept0,4,10])
            
        elif (x-1==0 and y+1==6):
            kb.add_clause([-percept0,-16])
            kb.add_clause([-percept0,-22])
            kb.add_clause([percept0,16,22])
            clauses.append([-percept0,-16])
            clauses.append([-percept0,-22])
            clauses.append([percept0,16,22])
            
        elif  (x+1==6 and y+1==6):
            kb.add_clause([-percept0,-20])
            kb.add_clause([-percept0,-24])
            kb.add_clause([percept0,20,24])
            clauses.append([-percept0,-20])
            clauses.append([-percept0,-24])
            clauses.append([percept0,20,24])

        elif (y-1==0):
            m1 = mapping[x-1,y]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept0,-m1])
            kb.add_clause([-percept0,-m2])
            kb.add_clause([-percept0,-m3])
            kb.add_clause([percept0,m1,m2,m3])
            clauses.append([-percept0,-m1])
            clauses.append([-percept0,-m2])
            clauses.append([-percept0,-m3])
            clauses.append([percept0,m1,m2,m3])

        elif (x-1==0):
            m1 = mapping[x,y-1]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept0,-m1])
            kb.add_clause([-percept0,-m2])
            kb.add_clause([-percept0,-m3])
            kb.add_clause([percept0,m1,m2,m3])
            clauses.append([-percept0,-m1])
            clauses.append([-percept0,-m2])
            clauses.append([-percept0,-m3])
            clauses.append([percept0,m1,m2,m3])

        elif (y+1 ==6):
            m1 = mapping[x+1,y]
            m2 = mapping[x-1,y]
            m3 = mapping[x,y-1]

            kb.add_clause([-percept0,-m1])
            kb.add_clause([-percept0,-m2])
            kb.add_clause([-percept0,-m3])
            kb.add_clause([percept0,m1,m2,m3])
            clauses.append([-percept0,-m1])
            clauses.append([-percept0,-m2])
            clauses.append([-percept0,-m3])
            clauses.append([percept0,m1,m2,m3])
        
        elif (x+1==6):
            m1 = mapping[x,y-1]
            m2 = mapping[x-1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept0,-m1])
            kb.add_clause([-percept0,-m2])
            kb.add_clause([-percept0,-m3])
            kb.add_clause([percept0,m1,m2,m3])
            clauses.append([-percept0,-m1])
            clauses.append([-percept0,-m2])
            clauses.append([-percept0,-m3])
            clauses.append([percept0,m1,m2,m3])
        
        else:
            m1 = mapping[x,y-1]
            m2 = mapping[x,y+1]
            m3 = mapping[x-1,y]
            m4 = mapping[x+1,y]

            kb.add_clause([-percept0,-m1])
            kb.add_clause([-percept0,-m2])
            kb.add_clause([-percept0,-m3])
            kb.add_clause([-percept0,-m4])
            kb.add_clause([percept0,m1,m2,m3,m4])
            clauses.append([-percept0,-m1])
            clauses.append([-percept0,-m2])
            clauses.append([-percept0,-m3])
            clauses.append([-percept0,-m4])
            clauses.append([percept0,m1,m2,m3,m4])

    
    # percept4(x,y) <-> m(x-1,y) and m(x+1,y) and m(x,y-1) and m(x,y+1)

    for i in range(25):
        loc = get_key(i+1,mapping)
        x = loc[0]
        y = loc[1]
        percept4 = 51 +i

        if (x-1!=0 and y-1 != 0 and x+1!=6 and y+1!=6):
            m1 = mapping[x,y-1]
            m2 = mapping[x,y+1]
            m3 = mapping[x-1,y]
            m4 = mapping[x+1,y]

            kb.add_clause([-percept4,m1])
            kb.add_clause([-percept4,m2])
            kb.add_clause([-percept4,m3])
            kb.add_clause([-percept4,m4])
            kb.add_clause([percept4,-m1,-m2,-m3,-m4])
            clauses.append([-percept4,m2])
            clauses.append([-percept4,m1])
            clauses.append([-percept4,m3])
            clauses.append([-percept4,m4])
            clauses.append([percept4,-m1,-m2,-m3,-m4])
     
     #percept1(x,y) <=> (m(x-1,y) or m(x+1,y) or m(x,y+1) or m(x,y-1)) and (m(x-1,y) -> ~m(x+1,y) and ~m(x,y+1) and ~m(x,y-1)) and so on

    for i in range(25):
        loc = get_key(i+1,mapping)
        x = loc[0]
        y = loc[1]
        percept1 = 76 +i

        if (x-1==0 and y-1==0):
            kb.add_clause([-percept1,2,6])
            kb.add_clause([-percept1,-2,-6])
            kb.add_clause([percept1,-2,6])
            kb.add_clause([percept1,2,-6])
            clauses.append([-percept1,2,6])
            clauses.append([-percept1,-2,-6])
            clauses.append([percept1,-2,6])
            clauses.append([percept1,2,-6])
        
        elif (x+1==6 and y-1==0):
            kb.add_clause([-percept1,4,10])
            kb.add_clause([-percept1,-4,-10])
            kb.add_clause([percept1,-4,10])
            kb.add_clause([percept1,4,-10])
            clauses.append([-percept1,4,10])
            clauses.append([-percept1,-4,-10])
            clauses.append([percept1,-4,10])
            clauses.append([percept1,4,-10])

        elif (x-1==0 and y+1==6):
            kb.add_clause([-percept1,22,16])
            kb.add_clause([-percept1,-22,-16])
            kb.add_clause([percept1,-22,16])
            kb.add_clause([percept1,22,-16])
            clauses.append([-percept1,22,16])
            clauses.append([-percept1,-22,-16])
            clauses.append([percept1,-22,16])
            clauses.append([percept1,22,-16])
        
        elif (x+1==6 and y+1==6):
            kb.add_clause([-percept1,24,20])
            kb.add_clause([-percept1,-24,-20])
            kb.add_clause([percept1,-24,20])
            kb.add_clause([percept1,24,-20])
            clauses.append([-percept1,24,20])
            clauses.append([-percept1,-24,-20])
            clauses.append([percept1,-24,20])
            clauses.append([percept1,24,-20])
        
        elif (y-1==0):
            m1 = mapping[x-1,y]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept1,m1,m2,m3])
            kb.add_clause([-percept1,-m1,-m2])
            kb.add_clause([-percept1,-m1,-m3])
            kb.add_clause([-percept1,-m3,-m2])
            kb.add_clause([percept1,m1,-m2,m3])
            kb.add_clause([percept1,-m1,m2,m3])
            kb.add_clause([percept1,m1,m2,-m3])
            clauses.append([-percept1,m1,m2,m3])
            clauses.append([-percept1,-m1,-m2])
            clauses.append([-percept1,-m1,-m3])
            clauses.append([-percept1,-m3,-m2])
            clauses.append([percept1,m1,-m2,m3])
            clauses.append([percept1,-m1,m2,m3])
            clauses.append([percept1,m1,m2,-m3])

        elif (x-1==0):
            m1 = mapping[x,y-1]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept1,m1,m2,m3])
            kb.add_clause([-percept1,-m1,-m2])
            kb.add_clause([-percept1,-m1,-m3])
            kb.add_clause([-percept1,-m3,-m2])
            kb.add_clause([percept1,m1,-m2,m3])
            kb.add_clause([percept1,-m1,m2,m3])
            kb.add_clause([percept1,m1,m2,-m3])
            clauses.append([-percept1,m1,m2,m3])
            clauses.append([-percept1,-m1,-m2])
            clauses.append([-percept1,-m1,-m3])
            clauses.append([-percept1,-m3,-m2])
            clauses.append([percept1,m1,-m2,m3])
            clauses.append([percept1,-m1,m2,m3])
            clauses.append([percept1,m1,m2,-m3])
        
        elif (x+1==6):
            m1 = mapping[x,y-1]
            m2 = mapping[x-1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept1,m1,m2,m3])
            kb.add_clause([-percept1,-m1,-m2])
            kb.add_clause([-percept1,-m1,-m3])
            kb.add_clause([-percept1,-m3,-m2])
            kb.add_clause([percept1,m1,-m2,m3])
            kb.add_clause([percept1,-m1,m2,m3])
            kb.add_clause([percept1,m1,m2,-m3])
            clauses.append([-percept1,m1,m2,m3])
            clauses.append([-percept1,-m1,-m2])
            clauses.append([-percept1,-m1,-m3])
            clauses.append([-percept1,-m3,-m2])
            clauses.append([percept1,m1,-m2,m3])
            clauses.append([percept1,-m1,m2,m3])
            clauses.append([percept1,m1,m2,-m3])

        elif (y+1==6):
            m1 = mapping[x-1,y]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y-1]

            kb.add_clause([-percept1,m1,m2,m3])
            kb.add_clause([-percept1,-m1,-m2])
            kb.add_clause([-percept1,-m1,-m3])
            kb.add_clause([-percept1,-m3,-m2])
            kb.add_clause([percept1,m1,-m2,m3])
            kb.add_clause([percept1,-m1,m2,m3])
            kb.add_clause([percept1,m1,m2,-m3])
            clauses.append([-percept1,m1,m2,m3])
            clauses.append([-percept1,-m1,-m2])
            clauses.append([-percept1,-m1,-m3])
            clauses.append([-percept1,-m3,-m2])
            clauses.append([percept1,m1,-m2,m3])
            clauses.append([percept1,-m1,m2,m3])
            clauses.append([percept1,m1,m2,-m3])

        else:
            m1 = mapping[x,y-1]
            m2 = mapping[x,y+1]
            m3 = mapping[x-1,y]
            m4 = mapping[x+1,y]

            kb.add_clause([-percept1,m1,m2,m3,m4])
            kb.add_clause([-percept1,-m1,-m2])
            kb.add_clause([-percept1,-m1,-m3])
            kb.add_clause([-percept1,-m1,-m4])
            kb.add_clause([-percept1,-m3,-m2])
            kb.add_clause([-percept1,-m4,-m2])
            kb.add_clause([-percept1,-m3,-m4])
            kb.add_clause([percept1,m1,-m2,m3,m4])
            kb.add_clause([percept1,-m1,m2,m3,m4])
            kb.add_clause([percept1,m1,m2,-m3,m4])
            kb.add_clause([percept1,m1,m2,m3,-m4])
            clauses.append([-percept1,m1,m2,m3,m4])
            clauses.append([-percept1,-m1,-m2])
            clauses.append([-percept1,-m1,-m3])
            clauses.append([-percept1,-m1,-m4])
            clauses.append([-percept1,-m3,-m2])
            clauses.append([-percept1,-m4,-m2])
            clauses.append([-percept1,-m3,-m4])
            clauses.append([percept1,m1,-m2,m3,m4])
            clauses.append([percept1,-m1,m2,m3,m4])
            clauses.append([percept1,m1,m2,-m3,m4])
            clauses.append([percept1,m1,m2,m3,-m4])

    for i in range(25):
        loc = get_key(i+1,mapping)
        x = loc[0]
        y = loc[1]
        percept3 = 101 +i

        if (y-1==0 and x-1!=0 and x+1!=6):
            m1 = mapping[x-1,y]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept3,m1])
            kb.add_clause([-percept3,m2])
            kb.add_clause([-percept3,m3])
            kb.add_clause([percept3,-m1,-m2,-m3])
            clauses.append([-percept3,m1])
            clauses.append([-percept3,m2])
            clauses.append([-percept3,m3])
            clauses.append([percept3,-m1,-m2,-m3])

        elif (x==1 and y!=1 and y!=5):
            m1 = mapping[x,y-1]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept3,m1])
            kb.add_clause([-percept3,m2])
            kb.add_clause([-percept3,m3])
            kb.add_clause([percept3,-m1,-m2,-m3])
            clauses.append([-percept3,m1])
            clauses.append([-percept3,m2])
            clauses.append([-percept3,m3])
            clauses.append([percept3,-m1,-m2,-m3])
        
        elif (x==5 and y!=1 and y!=5):
            m1 = mapping[x,y-1]
            m2 = mapping[x-1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([-percept3,m1])
            kb.add_clause([-percept3,m2])
            kb.add_clause([-percept3,m3])
            kb.add_clause([percept3,-m1,-m2,-m3])
            clauses.append([-percept3,m1])
            clauses.append([-percept3,m2])
            clauses.append([-percept3,m3])
            clauses.append([percept3,-m1,-m2,-m3])
        
        elif (y==5 and x!=1 and x!=5):
            m1 = mapping[x,y-1]
            m2 = mapping[x-1,y]
            m3 = mapping[x+1,y]

            kb.add_clause([-percept3,m1])
            kb.add_clause([-percept3,m2])
            kb.add_clause([-percept3,m3])
            kb.add_clause([percept3,-m1,-m2,-m3])
            clauses.append([-percept3,m1])
            clauses.append([-percept3,m2])
            clauses.append([-percept3,m3])
            clauses.append([percept3,-m1,-m2,-m3])

        elif (y!=1 and x!=1 and x!=5 and y!=5):
            m1 = mapping[x,y-1]
            m2 = mapping[x,y+1]
            m3 = mapping[x-1,y]
            m4 = mapping[x+1,y]

            kb.add_clause([m1,m2,-percept3])
            kb.add_clause([m1,m3,-percept3])
            kb.add_clause([m1,m4,-percept3])
            kb.add_clause([m2,m3,-percept3])
            kb.add_clause([m2,m4,-percept3])
            kb.add_clause([m3,m4,-percept3])
            kb.add_clause([m1,m2,m3,-percept3])
            kb.add_clause([m1,m2,m4,-percept3])
            kb.add_clause([m1,m3,m4,-percept3])
            kb.add_clause([m2,m3,m4,-percept3])
            kb.add_clause([m1,m2,m3,m4,-percept3])
            kb.add_clause([-m1,-m2,-m3,-m4,-percept3])
            kb.add_clause([m1,-m2,-m3,-m4,percept3])
            kb.add_clause([-m1,m2,-m3,-m4,percept3])
            kb.add_clause([-m1,-m2,m3,-m4,percept3])
            kb.add_clause([-m1,-m2,-m3,m4,percept3])
            clauses.append([m1,m2,-percept3])
            clauses.append([m1,m3,-percept3])
            clauses.append([m1,m4,-percept3])
            clauses.append([m2,m3,-percept3])
            clauses.append([m2,m4,-percept3])
            clauses.append([m3,m4,-percept3])
            clauses.append([m1,m2,m3,-percept3])
            clauses.append([m1,m2,m4,-percept3])
            clauses.append([m1,m3,m4,-percept3])
            clauses.append([m2,m3,m4,-percept3])
            clauses.append([m1,m2,m3,m4,-percept3])
            clauses.append([-m1,-m2,-m3,-m4,-percept3])
            clauses.append([m1,-m2,-m3,-m4,percept3])
            clauses.append([-m1,m2,-m3,-m4,percept3])
            clauses.append([-m1,-m2,m3,-m4,percept3])
            clauses.append([-m1,-m2,-m3,m4,percept3])

    #adding percept2 clauses.
    

    for i in range(25):
        loc = get_key(i+1,mapping)
        x = loc[0]
        y = loc[1]
        percept2 = 126 +i
    
        if (x-1==0 and y-1==0):
            kb.add_clause([2,-percept2])
            kb.add_clause([6,-percept2])
            kb.add_clause([-2,-6,percept2])
            clauses.append([2,-percept2])
            clauses.append([6,-percept2])
            clauses.append([-2,-6,percept2])

        elif (x==5 and y==1):
            kb.add_clause([4,-percept2])
            kb.add_clause([10,-percept2])
            kb.add_clause([-4,-10,percept2])
            clauses.append([4,-percept2])
            clauses.append([10,-percept2])
            clauses.append([-4,-10,percept2])

        elif (x==1 and y==5):
            kb.add_clause([16,-percept2])
            kb.add_clause([22,-percept2])
            kb.add_clause([-16,-22,percept2])
            clauses.append([16,-percept2])
            clauses.append([22,-percept2])
            clauses.append([-16,-22,percept2])
        
        elif (x==5 and y==5):
            kb.add_clause([24,-percept2])
            kb.add_clause([20,-percept2])
            kb.add_clause([-24,-20,percept2])
            clauses.append([24,-percept2])
            clauses.append([20,-percept2])
            clauses.append([-24,-20,percept2])

        elif (y==1):
            m1 = mapping[x-1,y]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([m1,m2,-percept2])
            kb.add_clause([m2,m3,-percept2])
            kb.add_clause([m1,m3,-percept2])
            kb.add_clause([m1,m2,m3,-percept2])
            kb.add_clause([-m1,-m2,-m3,-percept2])
            kb.add_clause([-m1,-m2,m3,percept2])
            kb.add_clause([m1,-m2,-m3,percept2])
            kb.add_clause([-m1,m2,-m3,percept2])
            clauses.append([m1,m2,-percept2])
            clauses.append([m2,m3,-percept2])
            clauses.append([m1,m3,-percept2])
            clauses.append([m1,m2,m3,-percept2])
            clauses.append([-m1,-m2,-m3,-percept2])
            clauses.append([-m1,-m2,m3,percept2])
            clauses.append([m1,-m2,-m3,percept2])
            clauses.append([-m1,m2,-m3,percept2])

        elif (x==1):
            m1 = mapping[x,y-1]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([m1,m2,-percept2])
            kb.add_clause([m2,m3,-percept2])
            kb.add_clause([m1,m3,-percept2])
            kb.add_clause([m1,m2,m3,-percept2])
            kb.add_clause([-m1,-m2,-m3,-percept2])
            kb.add_clause([-m1,-m2,m3,percept2])
            kb.add_clause([m1,-m2,-m3,percept2])
            kb.add_clause([-m1,m2,-m3,percept2])
            clauses.append([m1,m2,-percept2])
            clauses.append([m2,m3,-percept2])
            clauses.append([m1,m3,-percept2])
            clauses.append([m1,m2,m3,-percept2])
            clauses.append([-m1,-m2,-m3,-percept2])
            clauses.append([-m1,-m2,m3,percept2])
            clauses.append([m1,-m2,-m3,percept2])
            clauses.append([-m1,m2,-m3,percept2])
        
        elif (y==5):
            m1 = mapping[x-1,y]
            m2 = mapping[x+1,y]
            m3 = mapping[x,y-1]

            kb.add_clause([m1,m2,-percept2])
            kb.add_clause([m2,m3,-percept2])
            kb.add_clause([m1,m3,-percept2])
            kb.add_clause([m1,m2,m3,-percept2])
            kb.add_clause([-m1,-m2,-m3,-percept2])
            kb.add_clause([-m1,-m2,m3,percept2])
            kb.add_clause([m1,-m2,-m3,percept2])
            kb.add_clause([-m1,m2,-m3,percept2])
            clauses.append([m1,m2,-percept2])
            clauses.append([m2,m3,-percept2])
            clauses.append([m1,m3,-percept2])
            clauses.append([m1,m2,m3,-percept2])
            clauses.append([-m1,-m2,-m3,-percept2])
            clauses.append([-m1,-m2,m3,percept2])
            clauses.append([m1,-m2,-m3,percept2])
            clauses.append([-m1,m2,-m3,percept2])

        elif (x==5):
            m1 = mapping[x,y-1]
            m2 = mapping[x-1,y]
            m3 = mapping[x,y+1]

            kb.add_clause([m1,m2,-percept2])
            kb.add_clause([m2,m3,-percept2])
            kb.add_clause([m1,m3,-percept2])
            kb.add_clause([m1,m2,m3,-percept2])
            kb.add_clause([-m1,-m2,-m3,-percept2])
            kb.add_clause([-m1,-m2,m3,percept2])
            kb.add_clause([m1,-m2,-m3,percept2])
            kb.add_clause([-m1,m2,-m3,percept2])
            clauses.append([m1,m2,-percept2])
            clauses.append([m2,m3,-percept2])
            clauses.append([m1,m3,-percept2])
            clauses.append([m1,m2,m3,-percept2])
            clauses.append([-m1,-m2,-m3,-percept2])
            clauses.append([-m1,-m2,m3,percept2])
            clauses.append([m1,-m2,-m3,percept2])
            clauses.append([-m1,m2,-m3,percept2])

        else:
            m1 = mapping[x,y-1]
            m2 = mapping[x-1,y]
            m3 = mapping[x,y+1]
            m4 = mapping[x+1,y]

            kb.add_clause([m1,m2,m3,-percept2])
            kb.add_clause([m1,m2,m4,-percept2])
            kb.add_clause([m1,m3,m4,-percept2])
            kb.add_clause([m2,m3,m4,-percept2])
            kb.add_clause([m1,m2,m3,m4,-percept2])
            kb.add_clause([-m1,-m2,-m3,m4,-percept2])
            kb.add_clause([-m1,-m2,m3,-m4,-percept2])
            kb.add_clause([-m1,m2,-m3,-m4,-percept2])
            kb.add_clause([m1,-m2,-m3,-m4,-percept2])
            kb.add_clause([-m1,-m2,-m3,-m4,-percept2])
            kb.add_clause([-m1,-m2,m3,m4,percept2])
            kb.add_clause([-m1,m2,-m3,m4,percept2])
            kb.add_clause([-m1,m2,m3,-m4,percept2])
            kb.add_clause([m1,-m2,-m3,m4,percept2])
            kb.add_clause([m1,-m2,m3,-m4,percept2])
            kb.add_clause([m1,m2,-m3,-m4,percept2])
            clauses.append([m1,m2,m3,-percept2])
            clauses.append([m1,m2,m4,-percept2])
            clauses.append([m1,m3,m4,-percept2])
            clauses.append([m2,m3,m4,-percept2])
            clauses.append([m1,m2,m3,m4,-percept2])
            clauses.append([-m1,-m2,-m3,m4,-percept2])
            clauses.append([-m1,-m2,m3,-m4,-percept2])
            clauses.append([-m1,m2,-m3,-m4,-percept2])
            clauses.append([m1,-m2,-m3,-m4,-percept2])
            clauses.append([-m1,-m2,-m3,-m4,-percept2])
            clauses.append([-m1,-m2,m3,m4,percept2])
            clauses.append([-m1,m2,-m3,m4,percept2])
            clauses.append([-m1,m2,m3,-m4,percept2])
            clauses.append([m1,-m2,-m3,m4,percept2])
            clauses.append([m1,-m2,m3,-m4,percept2])
            clauses.append([m1,m2,-m3,-m4,percept2])

    #GOLD:
    kb.add_clause([-57,151])
    kb.add_clause([-58,151])
    kb.add_clause([-59,151])
    kb.add_clause([-62,151])
    kb.add_clause([-63,151])
    kb.add_clause([-64,151])
    kb.add_clause([-67,151])
    kb.add_clause([-68,151])
    kb.add_clause([-69,151])
    clauses.append([-57,151])
    clauses.append([-58,151])
    clauses.append([-59,151])
    clauses.append([-62,151])
    clauses.append([-63,151])
    clauses.append([-64,151])
    clauses.append([-67,151])
    clauses.append([-68,151])
    clauses.append([-69,151])


    # ag = Agent()
    # print('curLoc',ag.FindCurrentLocation())
    # print('Percept ',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Up')
    # print('Percept ',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Up')
    # print('Percept ',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Right')
    # print('Percept ',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Right')
    # print('Percept ',ag.PerceiveCurrentLocation())

    def LocToMat(loc):
        return [5-loc[1],loc[0]-1]

    def MoveaccPlan(Plan):
        for i in Plan:
            ag.TakeAction(i)

    def SafeCells():
        for i in range(5):
            for j in range(5):
                if world[i][j]==2:
                    return True

    




    class BFSElement:
        def __init__(self, i, j):
            self.i = i
            self.j = j
    
    R, C = 5,5

    def findPath(M,curr):
        q = []
        q.append([BFSElement(curr[0],curr[1]),[]])
        
        
        while (len(q) != 0 and SafeCells()):

            x = q[0][0]
            path = q[0][1]
            pathr = []
            pathl = []
            pathu = []
            pathd = []
        
            for i in range(len(path)+1):
                if i==len(path):
                    pathr.append("Right")
                    pathl.append("Left")
                    pathu.append("Up")
                    pathd.append("Down")
                else:
                    pathr.append(path[i])
                    pathl.append(path[i])
                    pathu.append(path[i])
                    pathd.append(path[i])
            q = q[1:]
    
            i = x.i
            j = x.j

            if (i < 0 or i >= R or j < 0 or j >= C):
                continue
    
            # if they are unvisited (value is 0).
            if (M[i][j] == 0):
                continue

            if (M[i][j] == 2):
                return path
            
            q.append([BFSElement(i,j+1),pathr])
            q.append([BFSElement(i,j-1),pathl])
            q.append([BFSElement(i-1,j),pathu])
            q.append([BFSElement(i+1,j),pathd])

        return None
    
    def CheckGold():
        g1 = Glucose3()
            
        for i in range(len(clauses)):
            g1.add_clause(clauses[i])
            
        g1.add_clause([-151])
        satis = g1.solve()
        if satis==False:
            return True
        return False

    def GoldLocation():
        # kb.add_clause([-57,151])
        # kb.add_clause([-58,151])
        # kb.add_clause([-59,151])
        # kb.add_clause([-62,151])
        # kb.add_clause([-63,151])
        # kb.add_clause([-64,151])
        # kb.add_clause([-67,151])
        # kb.add_clause([-68,151])
        # kb.add_clause([-69,151])
        g1 = Glucose3()
        for i in range(len(clauses)):
            g1.add_clause(clauses[i])
        g1.add_clause([-57])
        satis = g1.solve()
        if satis==False:
            return [2,2]
        g2 = Glucose3()
        for i in range(len(clauses)):
            g2.add_clause(clauses[i])
        g2.add_clause([-58])
        satis = g2.solve()
        if satis==False:
            return [3,2]
        g3 = Glucose3()
        for i in range(len(clauses)):
            g3.add_clause(clauses[i])
        g3.add_clause([-59])
        satis = g3.solve()
        if satis==False:
            return [4,2]

        g4 = Glucose3()
        for i in range(len(clauses)):
            g4.add_clause(clauses[i])
        g4.add_clause([-62])
        satis = g4.solve()
        if satis==False:
            return [2,3]

        g5 = Glucose3()
        for i in range(len(clauses)):
            g5.add_clause(clauses[i])
        g5.add_clause([-63])
        satis = g5.solve()
        if satis==False:
            return [3,3]

        g6 = Glucose3()
        for i in range(len(clauses)):
            g6.add_clause(clauses[i])
        g6.add_clause([-64])
        satis = g6.solve()
        if satis==False:
            return [4,3]

        g7 = Glucose3()
        for i in range(len(clauses)):
            g7.add_clause(clauses[i])
        g7.add_clause([-67])
        satis = g7.solve()
        if satis==False:
            return [2,4]
        
        g8 = Glucose3()
        for i in range(len(clauses)):
            g8.add_clause(clauses[i])
        g8.add_clause([-68])
        satis = g8.solve()
        if satis==False:
            return [3,4]
        
        g9 = Glucose3()
        for i in range(len(clauses)):
            g9.add_clause(clauses[i])
        g9.add_clause([-69])
        satis = g9.solve()
        if satis==False:
            return [4,4]


    def CheckSafes():
        
        for i in range(25):
            g1 = Glucose3()
            loc = get_key(i+1,mapping)
            e = loc[0]
            f = loc[1]
            a,b = LocToMat([e,f])
            for j in range(len(clauses)):
                g1.add_clause(clauses[j])
            g1.add_clause([i+1])
            satis = g1.solve()
            if satis==False:
                kb.add_clause([-i-1])
                clauses.append([-i-1])
                if world[a][b]==0:
                    world[a][b] = 2






        

#1-25 -: correspond to locations
#1-25 -: correspond to mines in those locations
#26-50 -: correspond to percept = 0 in corresponding locations.
#51 - 75 -: percept =4 in corresponding locations
#76-100 -: percept =1 in the corresponding locs
#101-125 -: percept = 3 in the corresponding locs.
#126-150 -: percept = 2 in their corresponding locs.
#151 for Gold


    
    ag = Agent()
    world = [[0, 0, 0,0,0],
             [0, 0, 0,0,0],
             [0, 0, 0,0,0],
             [0, 0, 0,0,0],
             [1, 0, 0,0,0]]

    
   

    if (ag.PerceiveCurrentLocation()==0):
        kb.add_clause([-2])
        kb.add_clause([-6])
        clauses.append([-2])
        clauses.append([-6])

        e,f = ag.FindCurrentLocation()
        i,j = LocToMat([e,f])
        world[i][j] = 2

        while SafeCells():
            
        
            e,f = ag.FindCurrentLocation()
            value = mapping[e,f]
            i,j = LocToMat([e,f])
            world[i][j] = 1
            
            p = ag.PerceiveCurrentLocation()
            if(p==0):
                #Percept0()
                kb.add_clause([value+25])
                clauses.append([value+25])
            elif (p==1):
                #Percept1()
                kb.add_clause([value+75])
                clauses.append([value+75])
            elif (p==2):
               # Percept2()
               kb.add_clause([value+125])
               clauses.append([value+125])
            elif (p==3):
                kb.add_clause([value+100])
                clauses.append([value+100])
            
            CheckSafes()
            
            if CheckGold():
                location = GoldLocation()
                print("Gold is present in room ("+str(location[0])+","+str(location[1])+")")
                break
            else:
                path = findPath(world,[i,j])
                if path==None:
                    continue
                for i in path:
                    ag.TakeAction(i)
                
                    
        else:
            print("Gold could not be detected after visting all the safe rooms.")
    
            

    
    else:
        print("Gold could not be detected after visting all the safe rooms.")

if __name__=='__main__':
    main()
