def function(x0,y0,x1,y1,alpha):
    m=(y1-y0)/(x1-x0)
    f= lambda x: m*(x-x0)+y0
    print(f(alpha))