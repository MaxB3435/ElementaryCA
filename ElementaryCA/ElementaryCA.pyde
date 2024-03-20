#CA variables

w = 50 
rows = 1
cols = 11

def setup():
    global cells
    size(600,600)
    #first row
    cells = []
    for r in range(rows):
        cells.append([])
        for c in range(cols):
            cells[r].append(0)
    cells[0][cols//2] = 1
    
def draw():
    background(255)
    
    for i, cell in enumerate(cells): #rows
        for j, v in enumerate(cell): #columns
            if v == 1:
                fill(0)
            else: fill(255)
            rect(j*W-(cols*w-width)/2,w*i,w,w)
    
