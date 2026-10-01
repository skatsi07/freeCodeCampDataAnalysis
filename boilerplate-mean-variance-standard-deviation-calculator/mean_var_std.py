import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    numparr = np.array([list[0:3], list[3:6], list[6:9]])

    #calculating the values
    mean = [numparr.mean(axis=0), numparr.mean(axis=1), numparr.mean()]
    variance = [numparr.var(axis=0), numparr.var(axis=1), numparr.var()]
    std = [numparr.std(axis=0), numparr.std(axis=1), numparr.std()]
    maxim = [numparr.max(axis=0), numparr.max(axis=1), numparr.max()]
    minim = [numparr.min(axis=0), numparr.min(axis=1), numparr.min()]
    total = [numparr.sum(axis=0), numparr.sum(axis=1), numparr.sum()]

    #creating the dictionary
    calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": std,
        "maximum": maxim,
        "minimum": minim,
        "sum": total
    }
    

    return calculations