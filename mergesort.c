// working it takes numbers from a file and out puts a file in sorted order 
// usage ./a.out <inputfile.txt>




#include <stdio.h>
void merge(int arr[],int l,int m,int h){
    int L[m-l+1],R[h-m];
    for(int i=0;i<m-l+1;i++){
        L[i]=arr[i+l];
    }
    for(int i=0;i<h-m;i++){
        R[i]=arr[m+1+i];
    }
    int i=0,j=0,g=l;
    while(i<m-l+1&&j<h-m){
        if(L[i]<=R[j]){
            arr[g]=L[i];
            i++;
            g++;
        }
        else{
            arr[g]=R[j];
            g++;
            j++;
        }
    }
    while(i<m-l+1){
        arr[g]=L[i];
        g++;
        i++;
    }
    while(j<h-m){
        arr[g]=R[j];
        g++;
        j++;

    }

}
void mergesort(int arr[],int l,int h){
 if(l<h){
     int m;
     m=(l+h)/2;
     mergesort(arr,l,m);
     mergesort(arr,m+1,h);
     merge(arr,l,m,h);
 }
}
int main(int argc , char* argv[]) {
    FILE* my_file;
    my_file= fopen(argv[1],"r");
    int i,n=0;
    while(fscanf(my_file, "%d\n", &i) != EOF)
    {
        n+=1;
    }
    fseek(my_file,0,SEEK_SET);
    int arr[n];
    int k=0;
    while(fscanf(my_file, "%d\n", &i) != EOF)
    {
        arr[k]=i;
        k++;
    }
    fclose(my_file);
    mergesort(arr,0,n-1);
    my_file=fopen("mergesort.txt","w");
    for (int j=0;j<n;j++){
        if(j<n-1){fprintf(my_file,"%d\n",arr[j]);}
        else{fprintf(my_file,"%d",arr[j]);}
    }
    fclose(my_file);
    return 0;
}
