import operator
W= input('Please enter a string ')
def most_frequent(string):
      d = dict()
      for key in string:
         if key not in d:
                d[key] = 1
            else:
                 d[key] += 1
             
       cd = sorted(d.itemd(),key=operator.itemgetter(1),reverse=True)
       return cd
       print (most_frequent(W))
