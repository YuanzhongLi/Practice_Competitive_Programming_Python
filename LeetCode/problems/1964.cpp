#define All(x) x.begin(), x.end()

// 0-indexed
template<class I, class BiOp>
class SegTree {
  int n;
  std::vector<I> dat;
  BiOp op;
  I e;
public:
  SegTree(int n_, BiOp op, I e) : op(op), e(e) {
    n = 1;
    while (n < n_) { n *= 2; } // n is a power of 2
    dat.resize(2 * n);
    for (int i = 0; i < 2 * n - 1; i++) {
      dat[i] = e;
    }
  }
  /* ary[k] <- v */
  void update(int k, I v) {
    k += n - 1;
    dat[k] = v;
    while (k > 0) {
      k = (k - 1) / 2;
      dat[k] = op(dat[2 * k + 1], dat[2 * k + 2]);
    }
  }
  void update_array(const vector<I> vals, int k=0) {
    for (int i = 0; i < vals.size(); ++i) {
      update(k + i, vals[i]);
    }
  }
  // Updates all elements. O(n)
  void update_all(const I *vals, int len) {
    for (int k = 0; k < std::min(n, len); ++k) {
      dat[k + n - 1] = vals[k];
    }
    for (int k = std::min(n, len); k < n; ++k) {
      dat[k + n - 1] = e;
    }
    for (int b = n / 2; b >= 1; b /= 2) {
      for (int k = 0; k < b; ++k) {
	      dat[k + b - 1] = op(dat[k * 2 + b * 2 - 1], dat[k * 2 + b * 2]);
      }
    }
  }
  // l,r are for simplicity
  I querySub(int a, int b, int k, int l, int r) const {
    if (a >= b) return e; // case by case
    if (r <= a || b <= l) return e;
    if (a <= l && r <= b) return dat[k];
    I vl = querySub(a, b, 2 * k + 1, l, (l + r) / 2);
    I vr = querySub(a, b, 2 * k + 2, (l + r) / 2, r);
    return op(vl, vr);
  }
  // [a, b)
  I query(int a, int b) const {
    return querySub(a, b, 0, 0, n);
  }
};

struct MAX {
  int operator() (int a, int b) const {
    return max(a, b);
  }
};

class Solution {
public:
    map<int, int> compress(vector<int>& ary) {
      set<int> se;
      for (int num: ary) {
        se.insert(num);
      }
      vector<int> unique_ary(se.size());
      int i = 0;
      for (int num: se) {
        unique_ary[i] = num; i++;
      }
      sort(All(unique_ary));
      i = 0;
      map<int, int> ret;
      for (int num: unique_ary) {
        ret[num] = i; i++;
      }

      return ret;
    }

    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        int n = obstacles.size();
        map<int, int> mp = compress(obstacles);
        int m = mp.size();
        SegTree<int, MAX> seg(m, MAX(), 0);
        vector<int> ans(n);
        int i = 0;
        for (int ob: obstacles) {
          int compressed_ob = mp[ob];
          int v = seg.query(0, compressed_ob + 1) + 1;
          seg.update(compressed_ob, v);
          ans[i] = v; i++;
        }
        return ans;
    }
};
