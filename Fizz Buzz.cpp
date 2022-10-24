class Solution {
public:
    vector<string> fizzBuzz(int n){
         vector<string> test;
         for (int i = 1; i <= n; i++) {
             
            if (i%15 == 0)
                test.push_back("FizzBuzz");
             
            else if (i%3 == 0)
                test.push_back("Fizz");
             
            else if (i%5 == 0)
                test.push_back("Buzz");
             
            else
                test.push_back(to_string(i));
        }
        return test;
    }
};
