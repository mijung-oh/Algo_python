#include <stdio.h>

using namespace std;
int count = 0;
int BRD[17][17] = { 0, };
int N;

int state_move[3][6] = {
  {0, 1, 1, 1, 0, 0},
  {1, 0, 1, 1, 0, 0},
  {0, 1, 1, 0, 1, 1}
};

void dfs(int x, int y, int state) {
	if (x == N - 1 && y == N - 1) {
		count++;
		return;
	}

	for (int i = 0; i < sizeof(state_move[state]) - 1; i += 2) {
		if (state == 0 && i == 4) break;
		if (state == 1 && i == 4) break;
		int newX = x + state_move[state][i];
		int newY = y + state_move[state][i + 1];

		int nextState = 0;
		if (state_move[state][i] == 0 && state_move[state][i + 1] == 1) nextState = 0;
		else if (state_move[state][i] == 1 && state_move[state][i + 1] == 0) nextState = 1;
		else if (state_move[state][i] == 1 && state_move[state][i + 1] == 1) nextState = 2;

		if (newX >= 0 && newX < N && newY >= 0 && newY < N && BRD[newX][newY] == 0) {
			if (nextState == 0) dfs(newX, newY, 0);
			else if (nextState == 1) dfs(newX, newY, 1);
			else if (nextState == 2 && newX - 1 >= 0 && newY - 1 >= 0 && BRD[newX - 1][newY] == 0 && BRD[newX][newY - 1] == 0) dfs(newX, newY, 2);
		}
	}
}


int main() {
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &BRD[i][j]);
		}
	}
	if (BRD[N - 1][N - 1] == 1) printf(0);
	else {
		dfs(0, 1, 0);
		printf("%d", count);
	}
}
