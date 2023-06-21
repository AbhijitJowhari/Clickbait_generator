import torch
import joblib
import torch.nn.functional as F


def generator():
    W = joblib.load('weights.sav')
    seed = joblib.load('seed.sav')
    stoi = joblib.load('stoi.sav')
    itos = joblib.load('itos.sav')

    g = torch.Generator().manual_seed(seed)


    out = []
    ix = 0
    while True:

        # ----------
        # BEFORE:
        #p = P[ix]
        # ----------
        # NOW:
        xenc = F.one_hot(torch.tensor([ix]), num_classes=len(stoi)).float()
        logits = xenc @ W # predict log-counts
        counts = logits.exp() # counts, equivalent to N
        p = counts / counts.sum(1, keepdims=True) # probabilities for next character
        # ----------

        ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
        out.append(itos[ix])
        if ix == 0:
            break
    seed+=1
    joblib.dump(seed,'seed.sav')
    clickbait = ' '.join(out)
    return clickbait