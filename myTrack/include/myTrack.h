
#ifndef __MYTRACK_H__
#define __MYTRACK_H__


#include <stdlib.h>




#define malloc(size)        _my_malloc(__FILE__,__func__,__LINE__, size)
#define realloc(ptr,size)   _my_realloc(__FILE__,__func__,__LINE__, ptr ,size)
#define calloc(count,size)  _my_calloc(__FILE__,__func__,__LINE__, count ,size)
#define free(ptr)           _my_free(__FILE__,__func__,__LINE__, ptr)

void* _my_malloc(char* fich, const char* fonc, int line, size_t size);
void* _my_realloc(char* fich, const char* fonc, int line, void * pointer , size_t bloc);
void* _my_calloc(char* fich, const char* fonc, int line, size_t elementCount, size_t elementSize);
void* _my_free(char* fich, const char* fonc, int line, void * adress);


#endif