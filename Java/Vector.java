public class Vector {
    // Everything is O(n) except for removing and adding to the end of the Vector
    // If we reach capacity, resize double
    // If when removing an item, if size is less than 1/4 of the capacity, then half the array

    private int size;
    private boolean empty;
    private Object[] array;
    public int capacity;
    private int ptr = 0;

    public Vector() { 
        this.size = 0;
        this.capacity = 4;
        this.empty = true;
        this.array = new Object[this.capacity];
    }

    public int size() {
        return this.size;
    }
    
    // number of items it can hold
    public int capacity() {
        return this.capacity;
    }

    public boolean isEmpty() {
        return this.empty;
    }

    // returns item at given index, blows up if index out of bounds
    public Object at(int index) {
        if (index > this.size) {
            return -1;
        } 
        return this.array[index];
    }

    public void push(Object item) {
        if (isFull()) {
            resize(this.capacity * 2);
        }
        this.array[this.ptr] = item;
        this.ptr += 1;
        this.size += 1;
        this.empty = false;
    }

    // inserts item at index, shifts that index's value and trailing elements to the right
    public void insert(int index, Object item) {
        // start shifting from the back
        // 0 1 2
        //     b p
        int bptr = this.ptr - 1; // edge case: 0 items blah

        while (bptr != index) {
            // shift the back pointer to the position of the front pointer
            this.array[this.ptr] = this.array[bptr]; // move backwards
            this.ptr -= 1;
            bptr -= 1;
        }

        this.array[this.ptr] = this.array[bptr]; // move backwards
        this.array[bptr] = item;
        this.size += 1;
        this.ptr = this.size;
        this.empty = false;
    }

    // can use insert above at index 0
    public void prepend(int item) {
        insert(0, item);

    }

    // remove from end, return value
    public Object pop() {
        this.ptr -= 1;
        if (this.ptr < 0) {
            return -1;
        } 
        this.size -= 1;
        if (this.size < this.capacity/4) {
            resize(this.capacity/2);
        }

        if (this.ptr == 0) {
            this.empty = true;
        }
        
        return this.array[this.ptr];
    }

    // delete item at index, shifting all trailing elements left
    public Object delete(int index) {
        Object value = this.array[index];
        int bpointer = index;
        int fpointer = index + 1;
        this.array[index] = 0;
        
        while (this.array[fpointer] != null) {
            this.array[bpointer] = this.array[fpointer];
            bpointer += 1;
            fpointer += 1;

        }
        this.size -= 1;
        this.ptr -= 1;
        if (this.ptr == 0) {
            this.empty = true;
        }
        if (this.size < this.capacity/4) {
            resize(this.capacity/2);
        }

        return value;
    }

    // looks for value and removes index holding it (even if in multiple places)
    public void remove(Object item) {
        int index = find(item);
        while (index != -1) {
            delete(index);
            index = find(item);
        }
    }

    // looks for value and returns first index with that value, -1 if not found
    public int find(Object item) {
        for (int i = 0; i < this.size; i++) {
            // System.out.println(this.array[i] + " " item);
            if (this.array[i] == item) {
                return i;
            }
        }
        return -1;
    }


    private void resize(int new_capacity) {
        Object[] new_array = new Object[new_capacity];
        for (int i = 0; i < this.size; i++) {
            new_array[i] = this.array[i];
        }
        this.array = new_array;
        this.capacity = new_capacity;
    }

    // prints the contents of the vector in order
    public void print() {
        for (int i = 0; i < this.size; i++) {
            System.out.println(this.array[i]);
        }

    }

    // Returns true if the vector is at capacity
    private boolean isFull() {
        return this.size == this.capacity;
    }

    public static void main(String[] args) {
        Vector v = new Vector();
        v.push("String");
        v.push(3);
        v.push(true);
        v.push(5); 
        v.push(8);
        v.print();
        // System.out.println(v.capacity);
        System.out.println("======");
        v.insert(0, 100);
        v.print();
        v.pop();
        v.pop();
        System.out.println("======");
        v.print();
        v.remove(100);
        System.out.println("======");
        v.print();
    }
}

