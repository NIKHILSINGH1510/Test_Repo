#include <iostream>
using namespace std;

int linear_search(int arr[],int key,int size)
{
    for(int i = 0;i < size;i++)
    {
        if(arr[i]==key)
          return i;
    }
    return -1;
}

int main()
{
    int arr[9] = {2,5,4,8,10,19,13,45,32};
    int index = linear_search(arr,4,9);
    if(index != -1)
    cout<<"ELEMENT IS PRESENT AT INDEX:"<<index;
    else
    cout<<"ELEMENT IS NOT PRESENT";
    return 0;
}