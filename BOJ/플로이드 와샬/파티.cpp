#include <stdio.h>
#define INF 100001

int dist[1001][1001];

int main() {
	int n, m, x, a, b, t, answer = 0;
	scanf("%d %d %d", &n, &m, &x);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			dist[i][j] = INF;
		}
		dist[i][i] = 0;
	}
	for (int i = 0; i < m; i++) {
		scanf("%d %d %d", &a, &b, &t);
		dist[a-1][b-1] = t;
	}
	for (int k = 0; k < n; k++) {
		for (int i = 0; i < n; i++) {
			if (dist[i][k] == INF) {
				continue;
			}
			for (int j = 0; j < n; j++) {
				if (dist[i][j] > dist[i][k] + dist[k][j]) {
					dist[i][j] = dist[i][k] + dist[k][j];
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (answer < dist[i][x-1] + dist[x-1][i]) {
			answer = dist[i][x-1] + dist[x-1][i];
		}
	}
	printf("%d", answer);
	return 0;
}