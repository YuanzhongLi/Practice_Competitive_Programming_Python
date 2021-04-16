#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    multiset<int> s1, s2;
    int k;
    vector<double> medianSlidingWindow(vector<int>& A, int kin) {
        k = kin;
        int N = A.size();
        for (int i=0; i<k; i++) add(A[i]);
        vector<double> ans;
        ans.push_back(get_med());
        for (int i=k; i<N; i++) {
            add(A[i]);
            remove(A[i-k]);
            ans.push_back(get_med());
        }
        return ans;
    }

    double get_med() {
        auto iter1 = s1.rbegin();
        int n1 = *iter1;
        if (k&1) {
            return (double)n1;
        } else {
             auto iter2 = s2.begin();
             int n2 = *iter2;
             return ((double)n1+(double)n2)/2.0;
        }
    }

    void add(int x) {
        if (s1.empty()) {
            s1.insert(x);
        } else if (s2.empty()) {
            auto iter1 = s1.rbegin();
            int n1 = *iter1;
            if (x < n1) {
                s1.erase(s1.find(n1));
                s1.insert(x);
                s2.insert(n1);
            } else {
                s2.insert(x);
            }
        } else {
            auto iter1 = s1.rbegin();
            int n1 = *iter1;
            auto iter2 = s2.begin();
            int n2 = *iter2;
            if (n1 <= x && x <= n2) {
                if (s1.size() == s2.size()) s1.insert(x);
                else s2.insert(x);
            } else if (x < n1) {
                if (s1.size() == s2.size()) s1.insert(x);
                else {
                    s1.erase(s1.find(n1));
                    s1.insert(x);
                    s2.insert(n1);
                }
            } else { // x > n2
                if (s1.size() == s2.size()) {
                    s2.erase(s2.find(n2));
                    s2.insert(x);
                    s1.insert(n2);
                } else s2.insert(x);
            }
        }
    }

    void remove(int x) {
        auto iter1 = s1.rbegin();
        int n1 = *iter1;
        auto iter2 = s2.begin();
        int n2 = *iter2;
        if (x <= n1) { // x in s1
            if (s1.size() == s2.size()) {
                s2.erase(s2.find(n2));
                s1.erase(s1.find(x));
                s1.insert(n2);
            } else s1.erase(s1.find(x));
        } else { // x in s2
            if (s1.size() == s2.size()) s2.erase(s2.find(x));
            else {
                s1.erase(s1.find(n1));
                s2.erase(s2.find(x));
                s2.insert(n1);
            }
        }
    }
};
