#include <bits/stdc++.h>            
using namespace std;

int INF = 99999999;
auto lamb =[](pair<int,int> a,pair<int,int> b){return a.first<b.first;};

class State
{
public:
	int col;
	array<int,14> arr;
	State(int v,array<int,14> a){
		col = v;
		arr = a;
	}
	inline int myCala(){return 6+col*7;}
	inline int opCala(){return 13-col*7;}
	inline bool myHole(int ind){
		if(col==0) return 0<=ind and ind<=5;
		else return 7<=ind and ind<=12;
	}
	inline bool opHole(int ind){
		return (!myHole(ind) && ind!=myCala() && ind!=opCala());
	}
	pair<int,int> nil(array<int,14>& a){
		int x=0,y=0;
		for (int i = 0; i < 14; ++i)
		{
			if(i<=5 && i>=0) x+= a[i];
			if(i>=7 && i<=12) y+= a[i];
		}
		return make_pair(x,y);
	}
	inline bool terminated(){
		auto x = nil(arr);
		return x.first==0 or x.second==0;
	}
	inline bool maxP(){return col==0;}
	int heur(){
        auto x = nil(arr);
        if(x.first==0 || arr[13]>24) return -INF;
        if(x.second==0 || arr[6]>24) return INF;
		int bin = arr[6] - arr[13];
		int tot = x.first - x.second;
		return bin+tot;
	}
	State move(int ind){
		int v = arr[ind];
		auto newArr = arr;
		newArr[ind] = 0;
		++ind;
		while (v){
			if(opCala()!=(ind%14)){
				++newArr[ind%14];
				--v; 
			}
			++ind;
		}

		int lastPut = (ind-1)%14;
		if(myCala()==lastPut) return State(col,newArr);

		if(myHole(lastPut) && newArr[lastPut]==1){
			int phole = 12- lastPut;
			if(newArr[phole]>0){
				newArr[lastPut] = 1+ newArr[phole];
				newArr[phole] = 0;
			}
		}

		auto x = nil(newArr);
		if(x.first==0) newArr[13] = 48 - newArr[6];
		if(x.second==0) newArr[6] = 48 - newArr[13];
		return State(1-col,newArr);

	}

};

int prune(State& state,int depth,int alpha,int beta){
	if(depth==0 or state.terminated()) return state.heur();

	int v = -INF;
	if(state.maxP()){
		for(int i = 0; i < 14; ++i){
			if(state.myHole(i) && state.arr[i]>0){
				auto child = state.move(i);
				v = max(v,prune(child,depth-1,alpha,beta));
				alpha = max(v,alpha);
				if(beta<=alpha) break;
			}
		}
	}
	else{
		v = INF;
		for(int i = 0; i < 14; ++i){
			if(state.myHole(i) && state.arr[i]>0){
				auto child = state.move(i);
				v = min(v,prune(child,depth-1,alpha,beta));
				beta = min(v,beta);
				if(beta<=alpha) break;
			}
		}
	}
	return v;
}

int move(State state){
	vector<pair<int,int>> v;
	for(int i=0;i<14;i++){
		if (state.myHole(i) && state.arr[i]>0)
		{
			auto child = state.move(i);
			auto a = prune(child,13,-INF,INF);
			v.push_back(make_pair(a,i));
		}
	}
	
	if(state.maxP()) return max_element(v.begin(), v.end(),lamb)->second;
	else return min_element(v.begin(), v.end(),lamb)->second;
}

int main(int argc, char const *argv[])
{
	//auto st = GetTickCount();
	int col;
	array<int,14> arr;
	scanf("%d",&col);--col;
	scanf("%d",&arr[6]);
	for(int i=0;i<6;i++) scanf("%d",&arr[i]);
	scanf("%d",&arr[13]);
	for(int i=7;i<13;i++) scanf("%d",&arr[i]);

	State s = State(col,arr);
	int mv = move(s);
	if(mv>6) cout<<(mv-6)<<endl;
	else cout<<(mv+1)<<endl;

	//cout<<GetTickCount()-st<<endl;
	return 0;
}