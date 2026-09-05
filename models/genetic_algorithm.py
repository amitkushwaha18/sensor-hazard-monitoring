"""Small GA demonstration for hyperparameter-search explanation/demo."""
import random
SPACE={'cnn_filters':[16,32,64],'lstm_units':[32,64,128],'dropout':[.1,.2,.3],'learning_rate':[1e-3,5e-4,1e-4]}
def score(cfg):
    # Demo objective only: represents a search procedure, NOT measured model accuracy.
    return 1/(1+abs(cfg['cnn_filters']-32)/32+abs(cfg['lstm_units']-64)/64+abs(cfg['dropout']-.2)+abs(cfg['learning_rate']-.001)*100)
def run(generations=8,population=12,seed=42):
    random.seed(seed); pop=[{k:random.choice(v) for k,v in SPACE.items()} for _ in range(population)]
    for _ in range(generations):
        pop=sorted(pop,key=score,reverse=True)[:max(2,population//3)]
        while len(pop)<population:
            p=random.choice(pop).copy(); k=random.choice(list(SPACE)); p[k]=random.choice(SPACE[k]); pop.append(p)
    return max(pop,key=score),score(max(pop,key=score))
if __name__=='__main__': print(run())
