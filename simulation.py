import random

def lancer_un_des():
    result = random.randint(1,6)
    return result

def check_for_two(lancer: list):
    if not 2 in lancer:
        return False
    return True

def check_for_win(lancer: list):
    lancer = sorted(lancer)
    if (lancer == [1,2]) or (lancer == [2,6]):
        return True
    return False

def main():
    lancer = []
    des_1 = lancer_un_des()
    des_2 = lancer_un_des()

    lancer.append(des_1)
    lancer.append(des_2)

    # On vérifie si on fait un lancé parfait du 1er coup
    if check_for_win(lancer=lancer) == True:
        return 1

    # On vérifie si on a un 2
    if check_for_two(lancer=lancer) == True:
        # On relance le dernier dés dans l'espoir de faire un 1 ou un 6
        dernier_lancer = lancer_un_des()
        if dernier_lancer in [1,6]:
            return 1
        else:
            return 0
    
    # Si on a pas de 2 :
    # On regarde si on a un 1 ou un 6, auquel cas on lance le dernier dés dans l'espoir de faire un 2 (1/6 chance)
    if (1 in lancer) or (6 in lancer):
        dernier_lancer = lancer_un_des()
        if dernier_lancer == 2:
            return 1
        else:
            return 0
    # Si on a ni 1 ni 6 on relance les 2 dés dans l'espoir de faire un lancé parfait
    else:
        dernier_lancer = []

        dernier_lancer_des_1 = lancer_un_des()
        dernier_lancer_des_2 = lancer_un_des()

        dernier_lancer.append(dernier_lancer_des_1)
        dernier_lancer.append(dernier_lancer_des_2)

        if check_for_win(lancer=dernier_lancer) == True:
            return 1
        else:
            return 0






if __name__ == '__main__':
    # print(lancer_un_des())
    # print(check_for_two([1,4]))
    # print(check_for_win([2,6]))
    result =  []
    for i in range(100000):
        result.append(main())
    
    print(sum(result))

""" 
On trouve 277870 avec 1 000 000 de lancés.
"""