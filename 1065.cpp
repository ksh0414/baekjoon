#include <iostream>
#include <string>

int main()
{
    int num;
    std::cin >> num;
    int dis;
    int res = num <= 99 ? num : 99;
    for(int i=100; i<=num; i++)
    {
        std::string temp = std::to_string(i);
        dis = temp[1] - temp[0];
        for(int j=2; j<temp.size(); j++)
            if(temp[j] - temp[j-1] != dis)
                break;
        else
            res += 1;
    }
    std::cout << res;
}