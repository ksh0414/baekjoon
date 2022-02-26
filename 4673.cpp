#include <iostream>

int main()
{
    bool arr[10001] = {false};

    int next_index;
    int temp = 0;
    for(int i=1; i<=10000; i++)
    {  
        next_index = i;
        temp = i;
        while(temp > 0)
        {
            next_index += temp % 10;
            temp /= 10;
        }
        if(next_index<=10000)
            arr[next_index] = true;
    }

    for(int i=1; i<=10000; i++)
        if(!arr[i])
            printf("%d\n", i);
}