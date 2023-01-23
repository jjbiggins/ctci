#include <stdio.h>
#include <stdlib.h>


int main ( int argc, char **argv ) {


    char test_string_pairs[6][7] = {
	{"abcd", "bacd"},
	{"3563476", "7334566"},
	{"wef34f", "wffe34"},
	{"abcd", "d2cba"},
	{"2354", "1234"},
	{"dcw4f", "dcw5f"}
    };


    char *str1;
    
    for ( int i = 0; i < sizeof(test_string_pairs); i++ ) {
	// printf("str1: %s\n", test_string_pairs[i][0]);
	printf("str1: %s\n", test_string_pairs[i]);
    }

};
