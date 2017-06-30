#include<iostream>
#include<vector>
#include<climits>

using namespace std;

struct process{
 int arrival,burst,remaining,turnaround,finish,no;
 }*q;
 
 struct order{
 int pno;
 int time;
 };
 
 int g_index=0;
 int n;
 vector<order> gantt;
 
 static int cmp_arrive(const void *p1,const void * p2)
 {
 	process * a=(process*) a;
 	process * b=(process *) b;
 	if(a->arrival<b->arrival) return -1;
 	else if(a->arrival==b->arrival) return 0;
 	else return 1; 	
 }
 
 void gantt_chart()
 {
 	cout<<"\n";
 	for(int i=0;i<g_index;i++)
 		cout<<"P"<<gantt[i].pno+1<<"\t";
 	cout<<endl;
 	for(int i=0;i<g_index;i++)
 		cout<<"@"<<gantt[i].time<<"\t";
        cout<<endl;
 			
 }
 
 
 void display()
 {
 	int avgwt=0;
 	int avgtt=0;
 	for(int i=0;i<n;i++)
 	{
 		q[i].waiting=q[i].finish-q[i].arrival-q[i].burst;
 		q[i].turnaround=q[i].finish-q[i].arrival;
 		avgwt+=q[i].waiting;
 		avgtt+=q[i].turnaround;
 		
 	}
 	cout<<"\n Waiting:"<<avgwt/(float)n<<endl;
 	cout<<"\n turnaround:"<<avgtt/(float)n<<endl;
 }
 
 process * getShortestJob(int curr)
 {
 	int min=INT_MAX;
	int  	
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
