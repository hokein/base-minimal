#include <src/base/memory/scoped_ptr.h>

int main() {
  scoped_ptr<int> ptr(new int(1));
  return 0;
} 
