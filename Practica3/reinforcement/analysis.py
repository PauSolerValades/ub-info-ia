# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question3():
    answerEpsilon = 0.0
    answerLearningRate = 1.0
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

    """

    """
if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(
            "No es possible que creui el pont. Quan epsilon = 0.0, vol dir que el nostre algorisme sempre esta explorant, intentant trobar quina es la ruta mes optima per aconseguir el problema.L'aplha=1 ens esta dient que els estats que hem investigat previament no compten per RES a l'aprenentatge que estem realitzant. Conclusio: si amb aquests parametres (que implquen que l'algorisme nomes esta intentant trobar una resposta, ni de bon tros la mes optima) no es capac de trobar la repsosta amb iteracions INDETERMINADES, es impossible que per altres valors que poguem posar en trobara una solucio."
            ))
