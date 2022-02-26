#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    std::cin.ignore(1);
    std::string str;
    int flag = 0;
    int res = n;
    for(int i=0; i<n; i++)
    {
        std::getline(std::cin, str);
        flag = 0;
        for(int index=0; index<str.size(); index++)
        {   
            char temp = str[index];
            if(!(flag & (1 << (str[index]-'a'))))
            {   
                flag |= (1 << str[index]-'a');
                while(str[index] == temp)
                    index++;
                index--;
            }
            else
            {
                --res;
                break;
            }
        }
    }
    std::cout << res;
}