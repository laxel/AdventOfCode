#include "d01.h"

bool readInp(string fileName, vector<int> & vec) {
    ifstream myfile;
    string line;
    myfile.open(fileName);
    if (myfile.is_open()) {
        while(getline(myfile,line)){
            vec.push_back(stoi(line,nullptr,10));
        }
        myfile.close();
        return true;
    }
    else {
        return false;
    }
}

void day01(string* res, string fileName) {
    vector<int> inp;
    readInp(fileName, inp);

    for (int i = 0; i < inp.size(); i++) {
        int a = inp[i];
        for (int j = i+1; j < inp.size(); j++) {
            int b = inp[j];
            if(a + b == 2020) {
                res[0] = to_string(a*b);
            }
            if(a+b >= 2020)
                continue;
            for(int k = j+1; k < inp.size(); k++) {
                int c = inp[k];
                if(a + b + c == 2020) {
                    res[1] = to_string(a*b*c);
                    goto end;
                }
            }
        }
    }
end:

    return;
}