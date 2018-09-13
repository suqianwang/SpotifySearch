//
//  parser.cpp
//  playlistIDExtracter
//
//  Created by Susan Wang on 2/17/18.
//  Copyright © 2018 Suqian Wang. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    string line;
    vector<string> ids;
    size_t pos;
    string temp_id;
    string filename = "/Users/SuqianWang/Downloads/Spring2018/CSCE470/Project/SpotifyCrawl-master/spotifyPlaylists.txt";
    
    ifstream infile(filename);
    
    while(getline(infile, line)) {
        pos = line.find("playlist:");
        temp_id = line.substr(pos+9, 22);
        cout << temp_id << endl;
        ids.push_back(temp_id);
    }
    
    ofstream outputFile("/Users/SuqianWang/Downloads/Spring2018/CSCE470/Project/SpotifyCrawl-master/playlist_id.txt");
    for (int i = 0; i < ids.size(); i++) {
        outputFile << ids.at(i) << endl;
    }
}
