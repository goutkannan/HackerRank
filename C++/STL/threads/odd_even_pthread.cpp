#include<iostream>
#include<pthread.h>
using namespace std; 

pthread_mutex_t myMutex; 

void *even(void *arg)
{
	for(int i=0; i< (long)arg; ++i)
	{
	    //pthread_mutex_lock( reference of the mutex variable) 
	    pthread_mutex_lock(&myMutex);	
		if(i%2 == 0)	
			cout<<i<<endl;
	    pthread_mutex_unlock(&myMutex);
	}
	pthread_exit(0);
}
void *odd(void *arg)
{
	for(int i=0; i< (long)arg; ++i)
	{
	     pthread_mutex_lock(&myMutex);
		if(i%2 !=0)	
			cout<<i<<endl;

	    pthread_mutex_unlock(&myMutex);
	}
	pthread_exit(0);
}

int main()
{
	pthread_t t_even;
	pthread_t t_odd; 
	long num = 20;
	pthread_mutex_init(&myMutex, 0);
	//pthread create - pthread id, stack size, function/worker id, args as void* )
	pthread_create(&t_even, NULL, &even, (void *)num);
 	pthread_create(&t_odd, NULL, &odd, (void *)num);
	//join the worker threads with the main thread 
	pthread_join(t_even, 0);
	pthread_join(t_odd, 0);
 	pthread_mutex_destroy(&myMutex);

	return 0; 
}
