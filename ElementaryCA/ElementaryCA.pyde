#CA variables

w = 1
rows = 2000
cols = 2000

#ruleset = [0,0,0,0,0,0,1,1] 
ruleset = [0,1,0,1,1,0,1,0] # rule 90
#ruleset = [0,0,0,1,1,1,1,0] # rule 30


def rules(a,b,c):
    return ruleset[7 - (4*a + 2*b + c)] # 2^2*a + 2^1*b + 2^0*c
# if ruleset = [0,0,0,0,0,0,0,1] return ruleset[7-0-0-0] = 1; return ruleset[7-0-0-1] = 0;
def generate():
    for i, row in enumerate(cells): #look at first row
        for j in range(1,len(row)-1):
            left = row[j-1]
            me = row[j]
            right = row[j+1]
            if i < len(cells) -1:
                cells[i+1][j] = rules(left,me,right)
    return cells
    
               

def setup():
    noStroke()
    global cells
    size(1000,700)
    #first row
    cells = []
    for r in range(rows):
        cells.append([])
        for c in range(cols):
            cells[r].append(0)
    cells[0][cols//2] = 1
    cells = generate()
    
def draw():
    background(255)
    for i, cell in enumerate(cells): #rows
        for j, v in enumerate(cell): #columns
            if v == 1:
                fill(0)
            else:fill(255)
            rect(j*w-(cols*w-width)/2,w*i-1,w,w)
    
