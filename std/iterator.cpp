#include <iostream>
#include <vector>
#include <iterator>
#include <map>


int main() {
  std::map<int, int> m;
  for (int i = 0; i < 5; i++) {
    m.emplace(i, i);
  }

  auto it = m.begin();
  // // Supported from g++ 10 (--std=c++2a)
  // auto n = std::ranges::next(it, 3);
  // std::cout << *n.second << std::endl;
  
  std::cout << (*it).second << std::endl;

  std::advance(it, 2);
  std::cout << it->second << std::endl;

  return 0;
}

