#program for arbitrary keyword arguments
def subjects(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
subjects(Sub1="Python", Sub2="Kisw", Sub3="Cre", Sub4="Math")        