from sys import maxsize

class Node(object):
    def __init__(self , i_depth , i_Playernum , i_sticksRemaining , i_value =0):
        self.i_depth = i_depth
        self.i_Playernum = i_Playernum
        self.i_sticksRemaining = i_sticksRemaining
        self.i_value = i_value
        self.children = []
        self.CreateChildren()

##creation du noeud
    def CreateChildren(self):
        if self.i_depth >= 0:
            for i in range(1,3):
                v = self.i_sticksRemaining - i
                self.children.append(Node(self.i_depth - 1 , -self.i_Playernum , v , self.RealVal(v)))


    def RealVal(self , value):
        if(value == 0):
            return maxsize * self.i_Playernum
        elif (value < 0):
            return maxsize * -self.i_Playernum
        return 0



##  Algorithme MinMax

def MinMax(node , i_depth , i_PlayerNum):
        ##Si on a arriver a la fin ou si on a sur un noued gangant
        if(i_depth == 0 ) or (abs(node.i_value) == maxsize):
            return node.i_value
        i_BestValue = maxsize * -i_PlayerNum
        ##maxsize est egale l'infini
        for i in range(len(node.children)):
            child = node.children[i]
            i_val = MinMax(child, i_depth - 1, -i_PlayerNum)
            ##Si i_val est proche de  l'infini on le stock dans best valeur
            if(abs(maxsize * i_PlayerNum - i_val) < abs(maxsize * i_PlayerNum - i_BestValue)):
                i_BestValue = i_val

        return i_BestValue


def WinCheck(i_sticks , i_PlayerNum):
    if i_sticks <=0 :
        print("*"*30)
        if i_PlayerNum > 0:
            if i_sticks == 0:
                print("\t You Won")
            else:
                print("\t Too Many You Loose")
        else:
            if i_sticks == 0:
                print("\t Computer Wins Next Time :)")
            else:
                print("Eror")
        print("*"*30)
        return 0
    return 1

if __name__ == '__main__':
    i_StickTotal = 11 ##Totalite de sticks dans le jeu
    i_depth = 3
    i_curPlayer = 1
    print("***Instructions**** \n \t ***U need to pick the last stick to win u can only choose 1 or 2 ***")
    while(i_StickTotal > 0):
        print("\n sticks remain" + str(i_StickTotal) + "How many you wat to pick ?")
        i_choice = input("\n \t 1 or 2 \n")
        i_StickTotal -= int(float(i_choice))
        if WinCheck(i_StickTotal , i_curPlayer):
            ##Ici on va retourner d 'un utilisateur a un autre
            ##J'ai encore looper pour savoir
            i_curPlayer *= -1
            node = Node(i_depth , i_curPlayer , i_StickTotal)
            BestChoice = -100
            i_BestValue = -i_curPlayer * maxsize
            for i in range(len(node.children)):
                n_child = node.children[i]
                i_val = MinMax(n_child , i_depth , i_curPlayer)
                if (abs(i_curPlayer * maxsize - i_val) <= abs(i_curPlayer * maxsize - i_BestValue)):
                    i_BestValue = i_val
                    BestChoice = i

            BestChoice+= 1
            print("Computer Choose"+ str(BestChoice) + "\t Based on value" + str(i_BestValue))
            i_StickTotal -= BestChoice
            WinCheck(i_StickTotal , i_curPlayer)
            i_curPlayer *= -1
