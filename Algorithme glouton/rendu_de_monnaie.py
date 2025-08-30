def rendu_de_monnaie(sum_to_give: list, system: list):
    sum_rest = sum_to_give
    gived = [0] * len(system)
    i = 0
    while sum_rest > 0:
        while system[i] > sum_rest:
            i += 1
        gived[i] = sum_rest // system[i]
        sum_rest = sum_rest % system[i]
    return gived

print(rendu_de_monnaie(43, [200, 100, 50, 20, 10, 5, 2, 1]))