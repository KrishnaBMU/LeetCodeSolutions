// Link: https://leetcode.com/problems/search-a-2d-matrix/
// Difficulty: Medium
// Time complexity: O(logn)
// Space complexity: O(1)

class Search2DMatrix {

    public boolean Search2DMatrix(int[][] matrix, int target) {
        
        // determining number of rows and columns of 2D matrix
        int m = matrix.length;
        if (m == 0) return false;
        int n = matrix[0].length;
        
        // determining values for binary search
        int left = 0;
        int right = (m * n) - 1;
        while (left <= right) {
            int pos = (left + right) / 2;
            int element = matrix[pos / n][pos % n];
            
            // position = target then found target
            if (element == target) {
                return true;
            }
            
            // position is too small, then need to move to the right
            else if (element < target) {
                left = pos + 1;
            }
            
            // position is too large, then need to move to the left
            else {
                right = pos - 1;
            }
        }
        return false;
        
    }
}