#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======
devChk
======

   :Nom du fichier:     devChk.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            201600706

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.4
    
####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 Module
   
####

Liste des Class
===============

Ensemble de class permettant le control et le debug.


"""
#################### Taille maximum des commentaires (90 caracteres)######################

from os import system


class C_DebugMsg(object) :
    """ 
        Class permettant d'intercepter et d'afficher les message de debug.

    Cette Class doit être instancier dans la fonction **__init__()** pour une Class
    et instancier en premier dans la fontion **main()** pour les fonctions
    n'appartenenant pas a une Class.
            
    Le constructeur a un argument par defaut de type **booleen** qui est predefinis
    sur **True**. Si se parametres est a **False**,
    l'ensemble des messages seront masques.
    
    Creation de l'instance :
    ::
    
        i_monIstanceDbg = C_DebugMsg( [booleen (facultatif si == True)] )

    """
    
    def __init__(self, v_affichage = True) :
        """ Init variables """
        self.affichage = v_affichage
        self.debugNumber = 0
        
    def __del__(self) :
        """destructor
        
            il faut utilise :
            ::
            
                del [nom_de_l'_instance]
        """
        v_className = self.__class__.__name__
        print("\n\t\tL'instance de la class {} est terminee".format(v_className))
        
    def dbgPrint(self, v_chk, v_varName, v_varValue) :
        """
        Intercept les messages pour les formater de facon homogene.
        
            Pour permettre de masquer les messages d'une seule fonction a la fois,
        il est conseille d'ajouter une variable local initialisee a **True**
        et de l'appeler a chaque fois que le debug et necessaire. Cette variable doit etre
        mise a **False** pour que l'affichage local soit desactive.
        
        Ex: ::
                
                # Affichage active
                v_dbg = True
                i_monIstanceDbg.dbgPrint(   v_dbg, 
                                        ["chaine_de_caractere"],
                                        [la_variable_a_controller]
                                    )
                                    
                # Affichage desactive
                v_dbg = False
                i_monIstanceDbg.dbgPrint(   v_dbg, 
                                        ["chaine_de_caractere"],
                                        [la_variable_a_controller]
                                    )
                                    
        Pour desactiver l'affichage d'un seul message a la fois, on peut remplacer la
        variable locale par une valeur **booleen**. On peut aussi simplement commenter
        la ligne du message de debug.
        
        Ex: ::
        
                # Affichage desactive par une valeur booleen
                v_dbg = True
                i_monIstanceDbg.dbgPrint(   False, 
                                        ["chaine_de_caractere"],
                                        [la_variable_a_controller]
                                    )
                                    
                # Affichage desactive en commentant la ligne
                v_dbg = True
                # i_monIstanceDbg.dbgPrint(   v_dbg, 
                                        # ["chaine_de_caractere" ou varialbe_de_reference],
                                        # [la_variable_a_controller]
                                    # )
        """
        if v_chk and self.affichage :
            self.debugNumber += 1
            print("dbgMsg[{}] : {} - {}".format(self.debugNumber, v_varName, v_varValue))
        
####
        
class C_GitChk(object) :
    """
        Class permettant de tester la branch (git) sur la quelle on se trouve,
    et nous informe si nous ne sommes pas sur la branch 'Master',
    afin d'éviter les opérations malheureuses.
    
    Cette Class doit être instancier dans la fonction **main()**.
    
    Le constructeur a un argument par defaut de type **booleen** qui est predefinis
    sur **True**. Si se parametres est a **False**, l'ensemble des messages seront masques.
    
    Creation de l'instance :
    ::
    
        i_monIstanceGitChk = C_GitChk( [booleen (facultatif si == True)] )

    """
    def __init__(self, control = True) :
        """ Init variables """
        self.controlActif = control
        
    def __del__(self) :
        """destructor
        
            il faut utilise :
            ::
            
                del [nom_de_l'_instance]
        """
        v_className = self.__class__.__name__
        print("\n\t\tL'instance de la class {} est terminee".format(v_className))
        
    def f_gitBranchChk(self):
        """ 
        identifie la branch courante et emet une alerte
        si elle est differente de '* master'
        
        N.B : Cette fonction doit être appeler sinon aucune action ne sera effectuée.
        """
        if self.controlActif :
            system("git branch > chkBranch")
            v_chaine = "* master"
            v_chk = True
            v_chaineIsTrue = True
            
            try :
                v_localLib = open("./chkBranch")
                
                for line in v_localLib : 
                    if not v_chaine in line : 
                        v_chaineIsTrue = False
                    else :
                        v_chaineIsTrue = True
                        break

            except FileNotFoundError :
                print("fichier non trouve")
                v_chk = False
                
            finally :
                if v_chk : v_localLib.close()
                
            if not v_chaineIsTrue :
                print   (" #################################################\n",
                         "#                                               #\n",
                         "# Attention, vous n'êtes sur la branch 'master' #\n",
                         "#                                               #\n",
                         "#################################################\n"
                        )

        else :
            print(" le control de branch est desactive")
    
 ####

def main():
    """ 
    Fonction principale 
    
    Cette Fonction ne sert que pour tester les différentes Class
    et méthode de ce projet.
    """
    system("cls")
    i_git = C_GitChk(False)
    i_git.f_gitBranchChk()
    
if __name__ == '__main__':
    main()