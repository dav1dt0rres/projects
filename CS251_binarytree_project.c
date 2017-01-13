#include <stdlib.h>
#define _GNU_SOURCE
#include <string.h>
#include <assert.h>
#include <stdio.h>



typedef struct tree_node						///nodes whose addresses are pointed to by the pointer. (The pointer contains the address to another node.)
{
int movie_id;
char movie_name[250];
struct tree_node *left;
struct tree_node *right;
}tree_node;

int count(tree_node *Tree){
	if (Tree==NULL){
		return 0;
	}	
	else{
		return 1+count(Tree->left)+count(Tree->right)	;
	}
	
}

tree_node *compare(tree_node *T,tree_node *Node){
	tree_node *cur;
	tree_node *before;
	if (T==NULL){
		T=Node;
		printf("first inputted root movie id : %d\n" ,T->movie_id) ;
		return T;
	}
	before=NULL;
	cur=T;
	while(cur!=NULL){
		if(cur->movie_id > Node->movie_id){
			before=cur;
			cur=cur->left;
		}
		else {
			before=cur;
			cur=cur->right;
		}
	
	}
	if (before->movie_id > Node->movie_id){
		before->left=Node;
	}
	else{
		before->right=Node;
	}
	printf("movie id : %d\n" ,Node->movie_id) ;
	return T;
	
}


tree_node *insert(char *filename ){					///Remmeber T points to the root of the tree

	
FILE *infile ;
char line[250];
int linesize = sizeof(line) / sizeof(line[0]);
char *token;
tree_node *root=NULL;	

infile=fopen(filename,"r");	
 if (infile == NULL)
  {
    printf("**Error: unable to open '%s'\n\n", filename);
    exit(-1);
  }
fgets(line, linesize,infile);
fgets(line, linesize,infile);	

while(!feof(infile)){

	tree_node *node;
	node = (tree_node*) malloc ( sizeof (tree_node) ); ///create a node to be inserted eventually when the right time comes.
	//here 'root' is the new node that will be added. 
	
	token=strtok(line,",");
	
	assert(token!=NULL);
	node->movie_id=atoi(token);
	printf("movie id : %d\n" ,node->movie_id) ;
	
	token = strtok(NULL, ",");
	strcpy(node->movie_name, token);
	printf("movie name : %d\n" ,node->movie_name) ;
	
	node->left=NULL;
	node->right=NULL;
	
	root=compare(root,node);
	fgets(line, linesize,infile);	
}	
	
	fclose(infile);
	return root ;


	
}
	
tree_node *search(tree_node *T, int id){
	
	if (T==NULL){
		printf("Tree empty");
	}
	tree_node *curr;
	curr=T;
	while(curr!=NULL){
		if (curr->movie_id>id){
			curr=curr->left;
		}
		if (curr->movie_id<id){
			curr=curr->right;
		}
		
		else{
			printf("found match");
			return curr;
		}
		
	}
	
	printf("did not find movie");
}

int main(){
	tree_node *T;
	T= insert("C:\\Users\\David\\Desktop\\movies.txt");
	
	
	
}