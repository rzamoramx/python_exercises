package com.ivansoft.java.exercises.challenges;

public class ValorObjetivo {
    /*
    Input:
    nums = [2, 7, 11, 15]
    target = 9

    Output:
    [0, 1]
     */

    public void twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int c = i; c < nums.length; c++) {
                if (nums[i] + nums[c] == target) {
                    System.out.println("[" + i +", " + c + "]");
                }
            }
        }
    }

    public static void main(String[] args) {
        ValorObjetivo vo = new ValorObjetivo();
        int[] nums = {2, 7, 11, 15};
        int target = 17;
        vo.twoSum(nums, target);
    }
}
