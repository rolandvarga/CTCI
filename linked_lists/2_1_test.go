package list_test

import (
	"reflect"
	"testing"

	list "github.com/rolandvarga/CTCI/linked_lists"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

// remove duplicates from an unsorted linked list
func deleteDups(head *list.ListNode) *list.ListNode {
	var hashSet = map[int]int{}
	var prev *list.ListNode
	curr := head

	for curr != nil {
		if _, ok := hashSet[curr.Value]; ok {
			prev.Next = curr.Next
		} else {
			hashSet[curr.Value] = 1
			prev = curr
		}
		curr = curr.Next
	}
	return head
}

// remove duplicates from an unsorted linked list without having a temporary buffer
func deleteDupsFollowup(head *list.ListNode) *list.ListNode {
	curr := head

	for curr != nil {
		runner := curr
		for runner.Next != nil {
			if runner.Next.Value == curr.Value {
				runner.Next = runner.Next.Next
			} else {
				runner = runner.Next
			}
		}
		curr = curr.Next
	}
	return head
}

func TestDeleteDups(t *testing.T) {
	var cases = []struct {
		list []int
		want []int
	}{
		{[]int{1, 2, 2, 3, 4, 4, 5}, []int{1, 2, 3, 4, 5}},
	}

	for _, c := range cases {
		head := list.NewListNode(c.list)
		got := deleteDups(head)
		gotInt := got.NodesToInt()

		if !reflect.DeepEqual(gotInt, c.want) {
			t.Errorf("got '%v' want '%v'", gotInt, c.want)
		}
	}
}

func TestDeleteDupsFollowup(t *testing.T) {
	var cases = []struct {
		list []int
		want []int
	}{
		{[]int{1, 2, 2, 3, 4, 4, 5}, []int{1, 2, 3, 4, 5}},
	}

	for _, c := range cases {
		head := list.NewListNode(c.list)
		got := deleteDupsFollowup(head)
		gotInt := got.NodesToInt()

		if !reflect.DeepEqual(gotInt, c.want) {
			t.Errorf("got '%v' want '%v'", gotInt, c.want)
		}
	}
}
