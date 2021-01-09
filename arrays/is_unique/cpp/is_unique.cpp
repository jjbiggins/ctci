#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <iostream>

int main()
{
    char* str;
    str = "ThisisGeeksForGeeks";
    
    static int ascii_chars[128];
    std::cout << strlen(str) << std::endl;
    std::cout << str  << std::endl;
    return 0;
}
        
