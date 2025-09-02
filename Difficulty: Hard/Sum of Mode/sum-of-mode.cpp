class Solution {
public:
    long long sumOfModes(vector<int>& arr, int k) {
        int n = arr.size();
        if (k > n) return 0;

        unordered_map<int,int> freq;                 // element -> frequency
        map<int, set<int>> freqToElems;              // frequency -> elements
        int maxFreq = 0;
        long long result = 0;

        auto add = [&](int x) {
            int oldFreq = freq[x];
            if (oldFreq > 0) {
                freqToElems[oldFreq].erase(x);
                if (freqToElems[oldFreq].empty()) freqToElems.erase(oldFreq);
            }
            freq[x]++;
            int newFreq = freq[x];
            freqToElems[newFreq].insert(x);
            maxFreq = max(maxFreq, newFreq);
        };

        auto remove = [&](int x) {
            int oldFreq = freq[x];
            freqToElems[oldFreq].erase(x);
            if (freqToElems[oldFreq].empty()) freqToElems.erase(oldFreq);

            freq[x]--;
            if (freq[x] == 0) freq.erase(x);
            else {
                freqToElems[freq[x]].insert(x);
            }

            if (freqToElems.find(maxFreq) == freqToElems.end()) {
                maxFreq--;
            }
        };

        // Initialize first window
        for (int i = 0; i < k; i++) add(arr[i]);
        result += *freqToElems[maxFreq].begin();

        // Slide window
        for (int i = k; i < n; i++) {
            add(arr[i]);
            remove(arr[i - k]);
            result += *freqToElems[maxFreq].begin();
        }

        return result;
    }
};

