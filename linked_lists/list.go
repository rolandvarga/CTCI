package list

type ListNode struct {
	Value int
	Next  *ListNode
}

func NewListNode(data []int) *ListNode {
	head := &ListNode{Value: -1}
	curr := head
	for _, d := range data {
		node := &ListNode{Value: d}
		curr.Next = node
		curr = node
	}
	return head.Next
}

func (this *ListNode) NodesToInt() []int {
	all := []int{}
	node := this
	for node != nil {
		all = append(all, node.Value)
		node = node.Next
	}
	return all
}
