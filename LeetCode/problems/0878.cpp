#include <bits/stdc++.h>
using namespace std;

#define All(x) x.begin(), x.end()

template<std::int_fast64_t Modulus>
class modint {
  using i64 = int_fast64_t;

  public:
  i64 a;

  constexpr modint(const i64 x = 0) noexcept {
    this -> a = x % Modulus;
    if(a < 0){
      a += Modulus;
    }
  }
  // constexpr i64 &value() const noexcept {return a;}
  constexpr const i64 &value() const noexcept {return a;}
  constexpr modint operator+(const modint rhs) const noexcept {
    return modint(*this) += rhs;
  }
  constexpr modint operator-(const modint rhs) const noexcept {
    return modint(*this) -= rhs;
  }
  constexpr modint operator*(const modint rhs) const noexcept {
    return modint(*this) *= rhs;
  }
  constexpr modint operator/(const modint rhs) const noexcept {
    return modint(*this) /= rhs;
  }
  constexpr modint &operator+=(const modint rhs) noexcept {
    a += rhs.a;
    if(a >= Modulus) {
      a -= Modulus;
    }
    return *this;
  }
  constexpr modint &operator-=(const modint rhs) noexcept {
    if(a < rhs.a) {
      a += Modulus;
    }
    a -= rhs.a;
    return *this;
  }
  constexpr modint &operator*=(const modint rhs) noexcept {
    a = a * rhs.a % Modulus;
    return *this;
  }
  constexpr modint &operator/=(modint rhs) noexcept {
    i64 a_ = rhs.a, b = Modulus, u = 1, v = 0;
    while(b){
      i64 t = a_/b;
      a_ -= t * b; swap(a_,b);
      u -= t * v; swap(u,v);
    }
    a = a * u % Modulus;
    if(a < 0) a += Modulus;
    return *this;
  }

  constexpr bool operator==(const modint rhs) noexcept {
    return a == rhs.a;
  }
  constexpr bool operator!=(const modint rhs) noexcept {
    return a != rhs.a;
  }
  constexpr bool operator>(const modint rhs) noexcept {
    return a > rhs.a;
  }
  constexpr bool operator>=(const modint rhs) noexcept {
    return a >= rhs.a;
  }
  constexpr bool operator<(const modint rhs) noexcept {
    return a < rhs.a;
  }
  constexpr bool operator<=(const modint rhs) noexcept {
    return a <= rhs.a;
  }
  template<typename T>
  friend constexpr modint modpow(const modint &mt, T n) noexcept {
    if(n < 0){
      modint t = (modint(1) / mt);
      return modpow(t, -n);
    }
    modint res = 1, tmp = mt;
    while(n){
      if(n & 1)res *= tmp;
      tmp *= tmp;
      n /= 2;
    }
    return res;
  }
  friend constexpr modint modinv(const modint &rhs) noexcept {
    i64 a_ = rhs.a, b = Modulus, u = 1, v = 0;
    while(b){
      i64 t = a_/b;
      a_ -= t * b; swap(a_,b);
      u -= t * v; swap(u,v);
    }
    u %= Modulus;
    if(u < 0) u += Modulus;
    return modint(u);
  };
};

const long long MOD = 1e9+7;
using mint = modint<MOD>;
// iostream
std::ostream &operator<<(std::ostream &out, const modint<MOD> &m) {
  out << m.a; return out;
};
std::istream &operator>>(std::istream &in, modint<MOD> &m) {
  long long a; in >> a; m = mint(a); return in;
};

mint fact[500005];

void init() {
  fact[0] = mint(1);
  for(int i = 1; i < 500005; i++) {
    fact[i] = fact[i-1] * mint(i);
  }
};

// calculate nCr mod
mint modcomb(long long n, long long r) {
  return fact[n] / fact[r] / fact[n - r];
};

// caluculate nPr mod
mint modp(long long n, long long r) {
  return fact[n]/fact[n-r];
};

class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
      int lcm = a / __gcd(a, b) * b;
      vector<int> vi;
      int i = a;
      while (i < lcm) {
        vi.emplace_back(i);
        i += a;
      }
      i = b;
      while (i < lcm) {
        vi.emplace_back(i);
        i += b;
      }

      vi.emplace_back(lcm);

      sort(All(vi));
      int m = vi.size();
      vector<mint> vm(m);
      for (int i = 0; i < m; i++) {
        vm[i] = mint(vi[i]);
      }

      int x = n / m;
      int y = n % m;

      mint ans = mint(lcm) * mint(x);
      if (y > 0) {
        ans += vm[y-1];
      }

      return ans.a;
    }
};
