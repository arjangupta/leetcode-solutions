#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Person {
    string name;
    int height;
    bool operator() (Person i, Person j) {
        return i.height > j.height;
    }
};

class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<Person> people;
        people.reserve(names.size());
        for (int i = 0; i < names.size(); i++) {
            Person person;
            person.name = names[i];
            person.height = heights[i];
            people.push_back(person);
        }
        sort(people.begin(), people.end(), Person());
        for (int i = 0; i < names.size(); i++) {
            names[i] = people[i].name;
        }
        return names;
    }
};