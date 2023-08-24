from copy import deepcopy
def remove_items(list, item):
    # using list comprehension to perform the task
    res = [i for i in list if i != item]
    return res

class variable():
    def __init__(self,symbol:str,co=[1],ex=[1],const=[0]) -> None:
        self.symbol = symbol
        self.coefficients = co # 0 index is always numerical
        self.exponents = ex
        self.constants = const
    
    def can_be_merged_addition(self,b)->bool:
        if type(b) == variable:
            if b.symbol == self.symbol:
                if b.exponents == self.exponents:
                    return True
        return False
    
    def __repr__(self) -> str:
        cos = str(self.coefficients).replace(',','+',-1).replace('[','(',1).replace(']',')',1).replace(' ','',-1) if self.coefficients != [1] else ''
        exs = '^'+str(self.exponents).replace(',','+',-1).replace('[','(',1).replace(']',')',1).replace(' ','',-1) if self.exponents != [1] else ''
        consts = str(self.constants).replace(' ','',-1).replace(',',' + ',-1).replace('[',' + ',1).replace(']','',1) if self.constants != [0] else ''
        s = f"{cos}{self.symbol}{exs}{consts}"
        return s
    
    def __add__(self,b):
        if type(b) == variable:
            if b.symbol == self.symbol:
                if b.exponents == self.exponents:
                    new_coe = concatanate_vars(self.coefficients,b.coefficients)
                    new_consts = concatanate_vars(self.constants,b.constants)
                    return variable(self.symbol,new_coe,self.exponents,new_consts)
            new_consts = concatanate_vars(self.constants,b.constants)
            b.constants = [0]
            new_consts.append(b)

            new_coe = self.coefficients
            for const in new_consts:
                if self.can_be_merged_addition(const):
                    new_coe = concatanate_vars(self.coefficients,const.coefficients)
                    new_consts.remove(const)
                    break

            return variable(self.symbol,new_coe,self.exponents,new_consts)
        new_consts = concatanate_vars(self.constants,[b]) if type(b) != list else concatanate_vars(self.constants,b)
        return variable(self.symbol,self.coefficients,self.exponents,new_consts)

    def __radd__(self,b):
        if type(b) == variable:
            if b.symbol == self.symbol:
                if b.exponents == self.exponents:
                    return None
        new_consts = concatanate_vars(self.constants,[b]) if type(b) != list else concatanate_vars(self.constants,b)
        return variable(self.symbol,self.coefficients,self.exponents,new_consts)

def concatanate_vars(a:list,b:list)->list:
    """
Adding two list of variables together. If the first list is simplified, then the result will be simplified.
E.g. a = ['3x','x^2','2a'], b = ['x','x','2b']
return ['5x','x^2','2a','2b']
    """
    if type(b) != list:
        b = [b]
    checkl = len(b)
    newl = []
    x = deepcopy(a)
    y = deepcopy(b)
    for var in x:
        for i in range(0,checkl):
            adding = y[i]
            if type(var) == type(adding):
                if type(var) == variable:
                    if var.symbol == adding.symbol:
                        if var.exponents == adding.exponents:
                            var.coefficients = concatanate_vars(var.coefficients,adding.coefficients)
                            var.constants = concatanate_vars(var.constants,adding.constants)
                            y[i] = None
                else:
                    var += adding
                    y[i] = None
        newl.append(var)
    leftover = remove_items(y,None)
    new = []
    while leftover != []:
        new.append(leftover[-1])
        leftover.pop()
        for var in new:
            for i in range(0,len(leftover)):
                adding = leftover[i]
                if type(var) == type(adding):
                    if type(var) == variable:
                        if var.symbol == adding.symbol:
                            if var.exponents == adding.exponents:
                                var.coefficients = concatanate_vars(var.coefficients,adding.coefficients)
                                var.constants = concatanate_vars(var.constants,adding.constants)
                                leftover.remove(leftover[i])
                                break
                    else:
                        var += adding
                        leftover.remove(leftover[i])
                        break
    newl+=new
    return newl

def simplify_add(l:list)->list:
    """
    e.g. [2,'a','8a','a^2',3] -> [5,'9a','a^2']
    time complexity: x!
    """
    if l == []:
        return l
    newl = [l[0]]
    

x = variable('x')
y = variable('y')
print(y+x+y+x)