#include <stdio.h>
#include <stdlib.h>

struct string_pair {
    char *str1;
    char *str2;
};




int main ( int argc, char **argv ) {

    test_case tests;
    bool is_permutation;
    char *str1;
    char *str2;


    
    for ( int i = 0; i < 256; i++ ) {
	str1 = tests[i];
	printf("str1: %s", str1);
    }

    return EXIT_SUCCESS;
}
