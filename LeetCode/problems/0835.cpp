class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();
        vector<vector<int>> img3(3*n, vector<int>(3*n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                img3[n+i][n+j] = img2[i][j];
            }
        }

        int ret = 0;

        for (int sx = 0; sx < 2*n; sx++) {
            for (int sy = 0; sy < 2*n; sy++) {
                int cnt = 0;
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (img1[i][j] == 1 && img3[sx+i][sy+j] == 1) cnt++;
                    }
                }
                ret = max(ret, cnt);
            }
        }

        return ret;
    }
};
