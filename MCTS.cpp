#include <bits/stdc++.h>
using namespace std;


class State
{
public:
	int col;
	array<int,14> arr;
	State(int v,array<int,14> a){
		col = v;
		arr = a;
	}
	virtual vector<int> possbl_moves() = 0;
	virtual State& move(int mv) = 0;
	virtual bool terminated() = 0;
	virtual double result() = 0;
	virtual bool maxP() = 0;
};

class Node
{
public:
	State* state;
	Node* parent;
	double wins = 0,visits = 1;
	map<int,Node*> children;

	Node(State* st,Node* prnt){
		state = st;
		parent = prnt;
		for(int x:state->possbl_moves()) children[x] = nullptr;
	}
	
};

bool comp(Node* a,Node* b){
	auto x = a->wins/a->visits + sqrt(2*log(a->parent->visits/a->visits));
	auto y = b->wins/b->visits + sqrt(2*log(b->parent->visits/b->visits));
	return x<y;
}

Node* select(Node* root){
	vector<Node*> v;
	for(auto& kv:root->children){
		if (!kv.second){
			return root;
		}
		v.push_back(kv.second);
	}
	if(v.empty()) return nullptr;
	auto best = *max_element(v.begin(),v.end(),comp);
	return select(best);
}

int main(int argc, char const *argv[])
{
	/* code */
	return 0;
}



