import java.utils.*;

public class Quicksort2{

	public static void main(String[] args){
		int[] x = {8,5,7,6,2,4,1,3,9 };
		System.out.println(Arrays.toString(x));
 
		int low = 0;
		int high = x.length - 1;
 
		quickSort(x, low, high);
		System.out.println(Arrays.toString(x));
	}

	public void quickSort(int[] arr, int low, int high){
		if(low>=high){
			return;
		}
		int p=arr[low];
		int partitionAt=partition(arr,low,high);
		quickSort(arr,low,partitionAt-1);
		quickSort(arr,partitionAt+1,high);
	}
	private int partition(int[] arr, int left, int right){
		int pivot=arr[left]
		int start=left+1;
		for(int i=start+1;i<=right;i++){
			if(arr[i]<=pivot){
				swap()
			}
		}
		swap()
	}

}