#include <vector>
#include <map>

class Solution {
public:
    int equalPairs(std::vector<std::vector<int>>& grid) {
        std::map<std::vector<int>, int> row_map;
        std::map<std::vector<int>, int> col_map;
        int count = 0;
        int n = grid.size();

        // Count row frequencies
        for (const auto& row : grid) {
            row_map[row]++;
        }

        // Count column frequencies
        for (int i = 0; i < n; ++i) {
            std::vector<int> col;
            col.reserve(n);
            for (int j = 0; j < n; ++j) {
                col.push_back(grid[j][i]);
            }
            col_map[col]++;
        }

        // Multiply matching frequencies
        for (const auto& [row, row_count] : row_map) {
            auto it = col_map.find(row);
            if (it != col_map.end()) {
                count += row_count * it->second;
            }
        }

        return count;
    }
};