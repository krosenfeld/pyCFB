import numpy as np
import itertools

def coffrey(p, w=None):
    """Calculate CFB exactly

    :param p: List of proportions
    :param w: List of weights

    Reference:
        Coffrey, Feingold, and Bromberg (1988) https://doi.org/10.1016/0167-9473(88)90088-6
    """

    # number of elements
    s = len(p)

    # check weights
    if w is None:
        # no weights
        w = 1/s * np.ones(s)
        equal_weights = True
    else:
        equal_weights = False

    assert np.isclose(sum(w), 1)
    assert np.all(p <= 1) & np.all(p >= 0)

    # mean
    pbar = sum([pi * wi for (pi, wi) in zip(p, w)])

    # xnum
    h = sum([wi * (pi - pbar) ** 2 for (pi, wi) in zip(p, w)])

    # xmax
    if equal_weights:
        # equal weight case
        n = np.floor(s * pbar)
        r = s * pbar - n
        hmax = pbar * (1 - pbar) - r * (1 - r) / s
    else:

        # unequal weight case
        hmax = 0
        # permutations of s-1 elements of [0,1]
        pstar = itertools.product([0, 1], repeat=s - 1)
        for p_ in pstar:
            #         print(p_)
            # given these s-1 elements of pstar, solve for p s.t. pbar given w
            for iw in range(s):
                if iw == 0:
                    w_ = w[iw + 1:]
                elif iw == s - 1:
                    w_ = w[:iw]
                else:
                    w_ = w[:iw] + w[iw + 1:]
                ps = (pbar - sum([wi * pi for (pi, wi) in zip(p_, w_)])) / w[iw]
                if (ps < 1) & (ps > 0):
                    h_ = sum([wi * (pi - pbar) ** 2 for (pi, wi) in zip(p_, w_)]) + w[iw] * (ps - pbar) ** 2
                    hmax = max(hmax, h_)

    return np.sqrt(h / hmax)


