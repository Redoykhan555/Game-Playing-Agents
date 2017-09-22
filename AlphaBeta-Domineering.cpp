#include <bits/stdc++.h>
#include <time.h>
using namespace std;

typedef pair<bool,uint64_t> Board;
typedef pair<int,int> Pos;

int INF = 2147483647;

inline bool maxP(Board b) {return b.first==true; }

inline bool index(Board b,int i,int j) {
	int ind = i*8+j;
	return (b.second>>ind)&1;
}

bool empty (Board b,bool c,int i,int j) {
			if(c) return index(b,i,j) && index(b,i+1,j);
			else return index(b,i,j) && index(b,i,j+1);
	}

bool safe (Board b,bool c,int i,int j) {
		if(c) return (j==7 or not empty(b,false,i,j)) and (j==0 or not empty(b,false,i,j-1));
		else return  (i==7 or not empty(b,true,i,j)) and (i==0 or not empty(b,true,i-1,j));
	}

bool socr (Board b,bool c,int i,int j) {
		if(not safe(b,c,i,j)) return false;
		if(c) return safe(b,c,i+1,j);
		else return safe(b,c,i,j+1);
	}



double helper(Board b,bool (*func) (Board b,bool c,int i,int j)){
	double ans = 0;
	int v[8][8] = {0};
	int h[8][8] = {0};
	for(int i=0;i<7;i++){
		for(int j=0;j<8;j++){
			if(func(b,true,i,j) and v[i][j]==0){
				ans = ans + 1;
				v[i+1][j]=1;
			}
		}
	}
	for(int i=0;i<8;i++){
		for(int j=0;j<7;j++){
			if(func(b,false,i,j) and h[i][j]==0){
				ans = ans - 1;
				h[i][j+1] = 1;
			}
		}
	}
	return ans;
}

double heur(Board b) {

	double real = helper(b,empty);
	double safe_vals = helper(b,socr);
	return real+safe_vals;
}
	
vector<Board> childs(Board b){
	vector<Board> ans;
	uint64_t k = 1;
	int x=8,y=7,d=1;
	if (maxP(b))
	{
		x=7;y=8;d=8;
	}
	for(int i=0;i<x;i++){
		for(int j=0;j<y;j++){
			int ind = i*8+j;
			if(((b.second>>ind)&1) and ((b.second>>(ind+d))&1)){
				uint64_t v = b.second;
				v &= ~(k<<ind);
				v &= ~(k<<(ind+d));
				ans.push_back(make_pair(b.first^1,v));
			}
		}
	}
	return ans;
}

bool terminated (Board b){return childs(b).size()<1;}

void print(Board b){
	string ans = "";
	if(b.first) ans = "v\n";
	else ans = "h\n";
	for(int i=0;i<8;i++){
		for(int j=0;j<8;j++){
			int ind = i*8+j;
			if((b.second>>ind)&1)  ans = ans + "-";
			else ans = ans + "x";
		}
		ans = ans +"\n";
	}
	cout<<ans<<endl;
}

double prune(Board b,int depth,double alpha,double beta){
	if(depth==0 or terminated(b)) return heur(b);

	double v = -INF;
	if(maxP(b)){
		for(auto child:childs(b)){
			v = max(v,prune(child,depth-1,alpha,beta));
			alpha = max(v,alpha);
			if(beta<=alpha) break;
		}
	}
	else{
		v = INF;
		for(auto child:childs(b)){
			v = min(v,prune(child,depth-1,alpha,beta));
			beta = min(v,beta);
			if(beta<=alpha) break;
		}
	}
	return v;
}


Pos move(Board b){
	auto cs = childs(b);
	vector<pair<double,Board>> temp;
	for(auto c:cs){
		temp.push_back(make_pair(prune(c,3,-INF,INF),c));
		//cout<<temp[temp.size()-1].first<<endl;
	}
	stable_sort(temp.begin(),temp.end());

	auto ans = temp[0].second;
	if(maxP(b)) ans = temp[cs.size()-1].second;

	for(int i=0;i<8;i++){
		for(int j=0;j<8;j++){
			int x=i*8+j;
			bool p = (b.second>>x)&1,q = (ans.second>>x)&1;
			if(p!=q) {
				return make_pair(i,j);
			}
		}
	}
    return make_pair(0,0);
}

int main()
{
	char c,y;
	uint64_t grid = 0,k=1;
	cin>>c;
	for(int i=0;i<8;i++){
		for(int j=0;j<8;j++){
			int ind = i*8+j;
			cin>>y;
			if(y=='-') grid|=(k<<ind);
		}
	}
	bool pl = true;
	if(c=='h') pl = false;
	auto b = make_pair(pl,grid);
	//print(b);
	auto start = clock();
	auto x = move(b);
	cout<<x.first<<" "<<x.second<<endl;
	return 0;
}