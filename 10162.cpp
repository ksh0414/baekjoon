#include <iostream>

int main()
{
    int t;
    std::cin >> t;
    
    if(t%10)
    {
        std::cout << -1;
        return 0;
    }
    
    int times[] = {300, 60, 10};
    int res[3] = {0, };
    int count = 0;
    for(int i=0; t>0; i++)
    {
        count = t / times[i];
        if(count)
        {
            res[i] = count;
            t -= times[i]*count;
        }
    }

    for(auto c : res)
        std::cout << c << " ";
}