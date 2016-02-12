import java.util.*;
public class topK {
	private static final int TOP_K = 3;
	public static void main(String args[]) {
		int[] _array = new int[]{8,5,7,6,2,4,1,3,9};
		if (_array.length == 0) {
			System.out.println("Empty Array");
			System.exit(0);
		} else if (_array.length == 1) {
			System.out.println("Only one element, Array already sorted");
		} else {
			select(_array, 0, _array.length-1, _array.length-TOP_K);
		}
		for (int i = _array.length-TOP_K; i <= _array.length - 1; i++) {
			System.out.println(_array[i]);
		}
	}
public static int partition(int[] input, int p, int q) {
	int x = input[p];
	int i = p;
	for (int j = (p + 1); j <= q; j++) {
		if (input[j] >= x) {
		i = i + 1;
			if(i < j){
				int temp = input[j];
				input[j] = input[i];
				input[i] = temp;
			}
		}
	}
	int temp1 = input[p];
	input[p] = input[i];
	input[i] = temp1;
	return i;
}
public static void select(int[] list, int left, int right, int k){
	int pivotIndex = partition(list, left, right);
	if(pivotIndex == k){
		return;
	}
	else if(k < pivotIndex){
		select(list, left, pivotIndex -1, k);
	}else{
		select(list, pivotIndex +1 , right, k);
	}
}
}