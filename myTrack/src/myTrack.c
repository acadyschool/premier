#include <stdio.h>
#define LENGHT 100
#define EXIST(n)((n == -1)?0 : 1)
#include <stdlib.h>
#include <assert.h>


typedef struct _Cell{
    void * adress; //l’adresse renvoyée
    size_t bloc; //la taille du bloc alloué
    int allocation; //un booléen, mis à true à l’allocation et qui passera à false à la libération
}_Cell;


typedef struct _Environement{
    _Cell * _array;//un moyen quelconque de stocker les cellules 
    int _taille_courant;//la taille actuelle de tableau
    size_t _allocation_total;//les quantités totales de mémoire allouée
    size_t _liberation_total;//les quantités totales de mémoire libérée
    int _compteur_failure_free;//les appels de free qui échouent
    int _compteur_sucess_free;//un pour les appels de free "réussis"
    int _compteur_malloc;//les appels de malloc "réussis"
    int _capacity_max;  // la capacité max du tableau


}_Environement;

static _Environement _table_save;//la table d’enregistrement des cellule
static int _FLAGS = 0;




static void displayTableSave();
static _Environement initialisationEnvironement(){
    /*
    initialisation de la table d'enregistrement
    */
    _Environement _table_save;
    _table_save._compteur_malloc = 0;
    _table_save._allocation_total = 0;
    _table_save._compteur_failure_free = 0;
    _table_save._compteur_sucess_free = 0;
    _table_save._liberation_total = 0;
    _table_save._taille_courant = 0;
    _table_save._array = calloc(LENGHT , sizeof(_Cell));
    _table_save._capacity_max = LENGHT;

    if(!_table_save._array){
        fprintf(stderr , "erreur d'allocation pour la table d'enregistrement \n");
        exit(1);
    }
    int valid = atexit(displayTableSave);
    assert(valid == 0);
    _FLAGS = 1;
    return _table_save;

}

static int research(void * p){
    /*
    on recherche l'adresse dans le tableau de cellule 
    l’adresse créée existe déjà dans la table on renvoie 
    l'indice de du tableau sinon -1
    */
    for(int i = 0 ; i < _table_save._taille_courant ; i++){
        if(p == _table_save._array[i].adress)
            return i;
    }

    return -1;
}

static _Cell * overflowArray(_Environement *_table_save ,int index){
    /*
    réallouer une zone mémoire
    si il n'y a plus de place dans le tableau
    */
    if(index == _table_save->_capacity_max){
        _Cell * tmp = calloc(_table_save->_capacity_max * 2 , sizeof(_Cell));
        if(!tmp)
            exit(1);
        
        for (int i = 0; i < _table_save->_capacity_max; i++)
        {
            tmp[i].adress = _table_save->_array[i].adress;
            tmp[i].bloc =  _table_save->_array[i].bloc;
        }
        
        _table_save->_capacity_max *= 2;
        return tmp;
        
    }
    return _table_save->_array;
}



static void insertArray(_Environement *_table_save , void * p , size_t bloc){
    /*
    insert l'adresse dans la table de cellule 
    si l'adresse existe déjà on la met à jour 
    sinon on crée une nouvelle cellule
    */
    int index = research(p);
   
    index = (EXIST(index))? index : _table_save->_taille_courant;
    _table_save->_array = overflowArray(_table_save , index);

    _table_save->_array[index].adress = p;

    _table_save->_array[index].bloc += bloc;
    _table_save->_array[index].allocation = 1;
    
    _table_save->_taille_courant = (!EXIST(index))? _table_save->_taille_courant: 
                                                _table_save->_taille_courant + 1;
    _table_save->_allocation_total += bloc;
    _table_save->_compteur_malloc++; 
   

    
}

extern void * _my_malloc(char* fich, const char* fonc, int line, size_t size){
    /*
    création du clone de malloc 
    */
    void * p = malloc(size);
    if(!_FLAGS)
        _table_save = initialisationEnvironement();
    

    if(!p){
        fprintf(stderr , "p est null\n");
        exit(1);
    }
    insertArray(&_table_save , p ,size);
    fprintf(stdout , "in file <%s> function <%s> line <0%d>(call#%d) malloc(%ld)->%p\n" ,fich,
                                                                                        fonc
                                                                                        ,line
                                                                                        ,_table_save._compteur_malloc, size 
                                                                                        , p);

    return p;
}


extern void * _my_realloc(char* fich, const char* fonc, int line,void * pointer , size_t bloc){
    /*
    création du clone de malloc 
    */
    void * p = realloc(pointer , bloc);

    if(!_FLAGS)
        _table_save = initialisationEnvironement();

    if(!p){
        fprintf(stderr , "p est null\n");
        exit(1);
    }
    insertArray(&_table_save , p ,bloc);
    fprintf(stdout , "in file <%s> function <%s> line <0%d>(call#%d) realloc(%ld)->%p\n" ,fich,
                                                                                        fonc,
                                                                                        line
                                                                                        ,_table_save._compteur_malloc,bloc 
                                                                                        , p);

    return p;
}

extern void * _my_calloc(char* fich, const char* fonc, int line,size_t elementCount, size_t elementSize){
    /*
    création du clone de malloc 
    */
    void * p = calloc(elementCount , elementSize);

    if(!_FLAGS)
        _table_save = initialisationEnvironement();

    if(!p){
        fprintf(stderr , "p est null\n");
        exit(1);
    }
    insertArray(&_table_save , p ,elementCount);
    fprintf(stdout , "in file <%s> function <%s> line <0%d>(call#%d) calloc(%ld)->%p\n" ,fich,
                                                                                        fonc,
                                                                                        line,
                                                                                        _table_save._compteur_malloc,elementCount , p);

    return p;
}

static void echange(_Cell *a , _Cell *b){
    /*
    echange les valeurs dans un tableau de cellule
    */
    _Cell tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}

static void clear(_Environement * _table_save ,int index){
    /*
    supprime la cellule dans la fonction free
    si le free s'est mal passé alors on incrémente 
    la variable compteur failure free
    sinon 
    on retire la cellule et increment la variable 
    réussite
    */
    if(index == -1){
        _table_save->_compteur_failure_free++;
        return;
    }
 
    _table_save->_array[index].adress = NULL;
    _table_save->_array[index].allocation = 0;
     _table_save->_liberation_total += _table_save->_array[index].bloc;
    _table_save->_array[index].bloc= 0;

    for(int i = index + 1 ; i < _table_save->_taille_courant; i++){
        echange(&_table_save->_array[i - 1] , &_table_save->_array[i]);
    }
    _table_save->_taille_courant--;
    _table_save->_compteur_sucess_free++;
   

}

extern void _my_free(char* fich, const char* fonc, int line,void * adress){
    /*
    création du clone de free 
    */
    int index = research(adress);

    if(!_FLAGS)
        _table_save = initialisationEnvironement();

    if(index == -1){
        clear(&_table_save ,index);
        fprintf(stdout , "in file <%s> function <%s> line <0%d>(call#%d) free(%p) ERREUR : adresse illégale -> ignoré\n" ,fich,
                                                                                                                        fonc,
                                                                                                                        line,
                                                                                                                        _table_save._taille_courant + 1 ,adress);
        return;
    }

    clear(&_table_save ,index);
    fprintf(stdout , "in file <%s> function <%s> line <0%d>(call#%d) free(%p)\n" ,fich,
                                                                                fonc,
                                                                                line,
                                                                                index + 1 
                                                                                ,adress);
    free(adress);
}


static void cleanEnvironment(_Environement * _table_save);



static void displayTableSave(){
    /*
    affiche la table d'enregistrement 
    */
    fprintf(stdout , "---------------------------------------\n" );
    fprintf(stdout , "BILAN FINAL\n" );
    fprintf(stdout , "total mémoire allouée  : %ld octet%s\n" ,
                                         _table_save._allocation_total
                                         , (_table_save._allocation_total > 1)?
                                         "s" : "");
    fprintf(stdout , "total mémoire libérée  : %ld octet%s\n", _table_save._liberation_total
                                                        ,(_table_save._liberation_total > 1)?
                                                        "s" : "");

    //fprintf(stdout , "ratio : %d\n", _table_save._compteur_sucess_free);
    fprintf(stdout , "<malloc>               : %d appel%s\n" , _table_save._compteur_malloc ,
                                                            (_table_save._compteur_malloc > 1)?
                                                            "s" : "");
    fprintf(stdout , "<free>                 : %d appel%s correct\n" , _table_save._compteur_sucess_free,
                                                                    (_table_save._compteur_sucess_free > 1)?
                                                                    "s" : "");
    fprintf(stdout , "                       : %d appel%s incorrect\n" , _table_save._compteur_failure_free,
                                                                        (_table_save._compteur_failure_free > 1)?
                                                                        "s" :"");

    fprintf(stdout , "---------------------------------------\n" );

    cleanEnvironment(&_table_save);
}




static void cleanEnvironment(_Environement * _table_save){
    /*vide l'environement*/
     _table_save->_compteur_malloc = 0;
    _table_save->_allocation_total = 0;
    _table_save->_compteur_failure_free = 0;
    _table_save->_compteur_sucess_free = 0;
    _table_save->_liberation_total = 0;
    _table_save->_taille_courant = 0;
    _table_save->_capacity_max = 0;
    _table_save->_array = NULL;
    free(_table_save->_array);

}
