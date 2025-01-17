/**
 * Class representing a node in a linked list.
 */
class LinkedListNode<T> {
    /**
     * Data stored in the node.
     */
    data: T;
    /**
     * Pointer to the next node in the linked list.
     */
    next: LinkedListNode<T> | null;

    /**
     * Initializes a new node.
     *
     * @param data Data to be stored in the node.
     */
    constructor(data: T) {
        this.data = data;
        this.next = null;
    }
}

/**
 * Class representing a linked list.
 */
class LinkedList<T> {
    /**
     * Pointer to the first node in the linked list.
     */
    head: LinkedListNode<T> | null;

    /**
     * Initializes an empty linked list.
     */
    constructor() {
        this.head = null;
    }

    /**
     * Traverses the linked list and prints the value of each node.
     */
    traverse(): void {
        let current: LinkedListNode<T> | null = this.head;
        while (current) {
            console.log(current.data, ' -> ');
            current = current.next;
        }
        console.log('None');
    }

    /**
     * Adds a new node to the head of the linked list.
     *
     * @param data Data to be stored in the new node.
     */
    addToHead(data: T): void {
        const newNode = new LinkedListNode<T>(data);
        newNode.next = this.head;
        this.head = newNode;
    }

    /**
     * Adds a new node to the tail of the linked list.
     *
     * @param data Data to be stored in the new node.
     */
    addToTail(data: T): void {
        const newNode = new LinkedListNode<T>(data);
        if (this.head === null) {
            this.head = newNode;
        } else {
            let current: LinkedListNode<T> | null = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    /**
     * Deletes the first node in the linked list.
     */
    deleteHead(): void {
        if (this.head !== null) {
            this.head = this.head.next;
        }
    }

    /**
     * Deletes the last node in the linked list.
     */
    deleteTail(): void {
        if (this.head === null) {
            return;
        }
        if (this.head.next === null) {
            this.head = null;
        } else {
            let current: LinkedListNode<T> | null = this.head;
            while (current?.next?.next) {
                current = current.next;
            }
            current.next = null;
        }
    }

    /**
     * Finds the first node with a value equal to a given value in the linked list.
     *
     * @param value Value to be searched.
     * @returns The node with the value if found, otherwise null.
     */
    find(value: T): LinkedListNode<T> | null {
        let current: LinkedListNode<T> | null = this.head;
        while (current) {
            if (current.data === value) {
                return current;
            }
            current = current.next;
        }
        return null;
    }

    /**
     * Inserts a new node into the linked list at a specific position.
     *
     * @param data Data to be stored in the new node.
     * @param position Position to be inserted (starting from 0).
     */
    insertAtPosition(data: T, position: number): void {
        const newNode = new LinkedListNode<T>(data);
        if (position === 0) {
            this.addToHead(data);
            return;
        }

        let current: LinkedListNode<T> | null = this.head;
        let currentPosition = 0;

        // Use optional chaining to handle potential null
        while (current && currentPosition < position - 1) {
            current = current.next;
            currentPosition += 1;
        }

        if (current === null) {
            console.log(
                `Position ${position} exceeds the length of the linked list.`
            );
        } else {
            newNode.next = current.next;
            current.next = newNode;
        }
    }

    /**
     * Deletes all nodes with a value equal to a given value in the linked list.
     *
     * @param value Value to be deleted.
     */
    deleteValue(value: T): void {
        while (this.head && this.head.data === value) {
            this.head = this.head.next;
        }

        let current: LinkedListNode<T> | null = this.head;
        while (current && current.next) {
            if (current.next.data === value) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }
    }

    /**
     * Reverses the linked list in place (without creating a new linked list).
     */
    reverse(): void {
        let prev: LinkedListNode<T> | null = null;
        let current: LinkedListNode<T> | null = this.head;
        while (current !== null) {
            const nextNode: LinkedListNode<T> | null = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }
        this.head = prev;
    }

    /**
     * Checks if the linked list has a cycle.
     *
     * @returns True if the linked list has a cycle, False otherwise.
     */
    hasCycle(): boolean {
        let slow: LinkedListNode<T> | null = this.head;
        let fast: LinkedListNode<T> | null = this.head;
        while (fast && fast.next) {
            if (slow && fast) {
                slow = slow.next;
                fast = fast.next.next;
                if (slow === fast) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Finds the first k nodes in the linked list.
     *
     * @param k The number of nodes to find.
     * @returns A list containing the values of the first k nodes.
     */
    findFirstKNodes(k: number): T[] {
        const result: T[] = [];
        let current: LinkedListNode<T> | null = this.head;
        while (current && k > 0) {
            result.push(current.data);
            current = current.next;
            k -= 1;
        }
        return result;
    }

    /**
     * Removes the kth node from the end of the linked list.
     *
     * @param k The position of the node to be removed (counting from the end of the linked list).
     */
    removeKthFromEnd(k: number): void {
        let fast: LinkedListNode<T> | null = this.head;
        let slow: LinkedListNode<T> | null | undefined = this.head;

        // Move fast pointer k positions ahead
        for (let i = 0; i < k; i++) {
            if (fast === null) {
                return; // k is greater than or equal to the length of the list
            }
            fast = fast.next;
        }

        // If fast is null after moving k positions, it means k is greater than or equal to the length of the list
        if (fast === null) {
            return;
        }

        // Move both pointers simultaneously until fast reaches the end
        while (fast.next) {
            fast = fast.next;
            slow = slow?.next; // Use optional chaining to handle potential null
        }

        // Now, slow points to the node before the kth node from the end
        if (slow && slow.next) {
            slow.next = slow.next.next;
        } else if (slow) {
            // Handle case when k is equal to the length of the list
            this.head = slow.next;
        }
    }

    /**
     * Finds the intersection point of two linked lists.
     *
     * @param list1 The first linked list.
     * @param list2 The second linked list.
     * @returns The intersection node if found, otherwise null.
     */
    findIntersection(
        list1: LinkedList<T>,
        list2: LinkedList<T>
    ): LinkedListNode<T> | null {
        const getLength = (head: LinkedListNode<T> | null): number => {
            let length = 0;
            while (head) {
                length += 1;
                head = head.next;
            }
            return length;
        };

        let l1: LinkedListNode<T> | null | undefined = list1.head;
        let l2: LinkedListNode<T> | null | undefined = list2.head;
        const len1 = getLength(l1);
        const len2 = getLength(l2);

        // Handle empty lists
        if (len1 === 0 || len2 === 0) {
            return null;
        }

        if (len1 > len2) {
            for (let i = 0; i < len1 - len2; i++) {
                l1 = l1?.next; // Use optional chaining to handle null
            }
        } else {
            for (let i = 0; i < len2 - len1; i++) {
                l2 = l2?.next; // Use optional chaining to handle null
            }
        }

        // Now l1 and l2 are at the same position relative to the intersection point
        while (l1 && l2) {
            if (l1 === l2) {
                return l1; // Intersection point found
            }
            l1 = l1.next;
            l2 = l2.next;
        }
        return null; // No intersection point found
    }
}
