#include <stdbool.h>

	/*A vector (mutable array with automatic resizing)
	Attributes: power = current power of 2 (2 ** power = size of array)
	filled_size = number of elements in teh array
	array: the actual array
	*/

	int power = 4;
	int arr[2 ** power];
	int filled_size = 0;

	void vector_init(int init_vector[]) {

	}

