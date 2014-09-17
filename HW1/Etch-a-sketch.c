#include <stdio.h>
#include <string.h>

#define SIZE	8

int board[SIZE][SIZE];
void printBoard(){
	int i,j;
	for (i=0;i<SIZE;i++){
		for (j=0;j<SIZE;j++){
			if (board[i][j])
				putchar('X');
			else 
				putchar('-');
		}
		putchar('\n');
	}
}

int main(){
	char* op;
	int currentx = 0;
	int currenty = 0;
	memset(board, 0, sizeof(board));
	board[currentx][currenty] = 1;
	do {
		printBoard();
		putchar('\n');
		op = fgets(op, 10, stdin);
		if (*op == 'w'){
			if (currentx != 0)
				currentx--;
		}
		else if (*op == 's'){
			if (currentx != SIZE-1)
				currentx++;
		}
		else if (*op == 'a'){
			if (currenty != 0)
				currenty--;
		}
		else if (*op == 'd'){
			if (currenty != SIZE-1)
				currenty++;
		}
		else if (*op == 'c'){
			memset(board, 0, sizeof(board));
		
		}
		board[currentx][currenty] = 1;

	}while (*op != 'q');
}

