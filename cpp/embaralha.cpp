#include <deque>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

std::tuple<vector<int>, int> embaralha(int N) {
  vector<int> remaning_cards(N - 1);
  deque<int> initial_deck(N);
  for (int i = 0; i < N; i++) {
    initial_deck[i] = i + 1;
  }
  for (int i = 0; i < N - 1; i++) {
    remaning_cards[i] = initial_deck.front();
    initial_deck.pop_front();
    initial_deck.push_back(initial_deck.front());
    initial_deck.pop_front();
  }
  return std::make_tuple(remaning_cards, initial_deck.front());
}

void print_result(vector<int> a, int b, int N) {
  cout << "[[";
  for (int i; i < N - 2; i++) {
    cout << a[i] << ",";
  }
  cout << a[N - 2] << "]," << b << "]" << endl;
}

int main(int argc, char **argv) {
  int card, N;
  vector<int> deck(N);

  sscanf(argv[1], "%d", &N);
  tie(deck, card) = embaralha(N);
  print_result(deck, card, N);
  return 0;
}
