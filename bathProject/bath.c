  
#include <sched.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h> 
#include <stdlib.h>
#include <pthread.h>
#include <sys/mman.h>
#include <sys/sysinfo.h>


typedef struct node{
	int data;
	struct node* next;
}node_t;



void push(node_t* head_ref, int new_data) 
{ 
	    /* 1. allocate node */
	    node_t* new_node = malloc(sizeof(node_t)); 
	    /* 2. put in the data  */
	    new_node->data  = new_data; 
	    /* 3. Make next of new node as head */
	    new_node->next = head_ref; 
	    /* 4. move the head to point to the new node */
	    head_ref = new_node; 
}

void addFileNumsToList(node_t* head, FILE* myFile) {

	if(NULL == myFile){
		fprintf(stderr,"data.txt not found, did you run data.sh?");
		fprintf(stderr,"note: stderr argument means we write to a special 'error' output stream.");
		fprintf(stderr,"Program terminating now...");
		exit(1);
	
	}

	int buffer;
	while(fscanf(myFile,"%d",&buffer) != EOF) {
		push(head,buffer); 
	}

	fclose(myFile);
}

void placeInAverage(int arr[], int user, node_t* head) {
	printf("User: %d\n", user);
	node_t* iterator;
	iterator =  head;
	int total = 0;
	int i = 0;
	while(iterator != NULL) {
		i++;
		printf("%d\n",i);
		total += iterator->data;
		iterator = iterator->next;
	}

	arr[user] = total;
}


int main(int argc, char *argv[]) {
	


	node_t* sheaData = malloc(sizeof(node_t));
	node_t* stanleyData = malloc(sizeof(node_t));
	node_t* kevinData = malloc(sizeof(node_t));
	node_t* bingData = malloc(sizeof(node_t));

	FILE *sheaFile = fopen("./sheaData.txt","r");
	FILE *bingFile = fopen("./bingData.txt","r");
	FILE *kevinFile = fopen("./kevinData.txt","r");
	FILE *stanleyFile = fopen("./stanleyData.txt","r");
	
	addFileNumsToList(sheaData, sheaFile);
	addFileNumsToList(bingData, bingFile);
	addFileNumsToList(stanleyData, kevinFile);
	addFileNumsToList(stanleyData, stanleyFile);
	
	int currentAverages[4];
	placeInAverage(currentAverages,0,sheaData);
	placeInAverage(currentAverages,1,bingData);
	placeInAverage(currentAverages,2,kevinData);
	placeInAverage(currentAverages,3,stanleyData);
	
	for (int i = 0; i< 4; i++) {
		printf("Current Average %d\n",i);
		printf("%d\n",currentAverages[i]);
	}
}




