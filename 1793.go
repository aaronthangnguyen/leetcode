package main

import "fmt"

func maximumScoreOfAGoodSubarray(nums []int, k int) int {
	n := len(nums)
	res := 0
	l, r := k, k
	minVal := nums[k]

	for l >= 0 && r < n {
		minVal = min(minVal, min(nums[l], nums[r]))
		res = max(res, minVal*(r-l+1))

		left := 0
		if l > 0 {
			left = nums[l-1]
		}
		right := 0
		if r < n-1 {
			right = nums[r+1]
		}

		if left >= right {
			l -= 1
		} else {
			r += 1
		}
	}

	return res
}

func assert(condition bool) {
	if !condition {
		panic("Failed.\n")
	}
}

func main() {
	assert(maximumScoreOfAGoodSubarray([]int{1, 4, 3, 7, 4, 5}, 3) == 15)
	fmt.Printf("Passed.\n")
}
