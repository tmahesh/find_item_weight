from itertools import combinations
sku_weights = {}

#test data 
data = [{'skus':['a','b'], 'weight':3}, {'skus':['b'], 'weight':1},{'skus':['b'], 'weight':2}, {'skus':['a','b','c','d'], 'weight':10}, {'skus':['a','d'], 'weight':5}, {'skus':['a','b'], 'weight':4}]

def mycombinations(x):
    return [c for i in range(1,len(x)) for c in combinations(x,i)]

def update(sku, weight):
  if sku not in sku_weights:
    v = {'count': 1, 'weight': weight}   
  else:
    v = sku_weights[sku]
    v['weight'] = (v['weight']*v['count'] + weight)/(v['count']+1)
    v['count'] = v['count'] + 1
  sku_weights[sku] = v

def initialise(data):
  for e in data:
    skus = tuple(e['skus'])               
    update(skus,e['weight'])

def diff(a,b):
  delta = list(set(a) - set(b))
  delta.sort()
  return tuple(delta)

def process():
  for skus in [*sku_weights.keys()]:
    for combo in mycombinations(skus): 
      if combo in sku_weights:
        delta = diff(skus,combo)
        #print("can update", delta, sku_weights[skus]['weight'], "-" ,sku_weights[combo]['weight'])
        if delta not in sku_weights:
          delta_weight = sku_weights[skus]['weight'] - sku_weights[combo]['weight']
          if delta_weight > 0:
            update(delta , delta_weight) 

initialise(data)
for i in range(5):
  process()

#print(sku_weights)
for skus in sku_weights:
  if len(skus) == 1:
    print(skus[0], sku_weights[skus]['weight'])
