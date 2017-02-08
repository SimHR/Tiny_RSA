#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

long long find_coprime(long long oilerP)
{
    long long val1 = oilerP;
    long long val2 = 2;

    int i = 1;
    int count = 0;

    long long gcd = 0;

    while(1)
    {
       for(i = 1; i <= val2; i++)
        {
            if((val1 % i == 0) && (val2 % i ==0))
                count++;
        }

        if(count != 1)
        {
            val2++;
            count = 0; //Reset count
        }

        else
            break;
    }

    return val2;
}

long long find_mod_inverse(long long e, long long oilerP)
{
    long long check = 0;
    long long mod_d = 1;

    while(check != 1)
    {
        check = (e * mod_d) % oilerP;
        mod_d++;
    }

    return mod_d-1;
}

long long prime_generator(void)
{

    int prime = 2;
    int last_prime = 0;

    srand(time(NULL));

    int prime_num = (rand() % 100) + 10;
    int prime_check = 0;

    int i = 1;
    int j = 0;

    for(j = 0; j < prime_num;)
    {

        if(prime % 2 == 0)  //If prime is evennumber, pass the other logic, (for performence) 
        {
            prime++;
            continue;
        }

        for(i = 1; i <= prime; i++)
        {
            if(prime % i == 0)
                prime_check++;
        }

        if(prime_check == 2)
        {
            j++;
            last_prime = prime;
        }

        prime_check = 0;
        prime++;
    }
    
    return last_prime;
}
