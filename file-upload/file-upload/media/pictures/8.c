#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>

int main()
{
	pid_t pid;
	pid=fork();
	if(pid<0)
	{
		printf("error occured while forking");
		exit(-1);
	}
	else if(pid==0)
	{
		printf("child process:\n ID:%d parentID:%d",getpid(),getppid());
	}
	else
	{
		wait(NULL);
		printf("\n Parent process:\n ID:%d ChildID:%d",getpid(),pid);
		exit(0);
	}
}
