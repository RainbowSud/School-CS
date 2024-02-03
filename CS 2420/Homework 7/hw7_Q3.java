package com.company;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class hw7_Q3 {
    public static void main(String[] args) throws IOException {
        final int ARRAY_SIZE = 100; // the fixed size of an array we will use

        int[] A = new int[ARRAY_SIZE];

        String inputFile = "hw7_input.txt"; // the name of the input file
        File myFile = new File(inputFile);
        Scanner input = new Scanner(myFile);

        //read numbers from the input file, after the while loop all numbers are stored in A[0,...,n-1], i.e., n is the number of elements in A
        int n = 0;// the number of elements stored in A
        while(input.hasNext())
        {
            int value = input.nextInt();
            A[n] = value;
            n++;
        }
        input.close();//close the input file

        //call quicksort
        quickSort(A, 0, n-1);

        System.out.println("The following is the list after quick sort:");
        for(int i = 0; i < n; i++)
            System.out.print(A[i] + " ");
        System.out.println();
    }

    //please complete the following function
    //sort the elements in the subarray A[low,...,high]
    private static void quickSort(int[] A, int low, int high) {
        if (low >= high) {
            return;
        }
        else {
            int i = partition(A, low ,high);
            quickSort(A, low, i-1);
            quickSort(A, i+1, high);
        }
    }

    //please complete the following function, which is needed in the above quickSort() function
    //partition A[low,...,high] into two subarrays by using a pivot (we will pick the last element A[high] as the pivot), and return the index of the pivot in the resulting partition
    private static int partition(int[] A, int low, int high) {
        int i = low;
        int k = high - 1;
        int pivot = A[high];
        while (true) {
            while (A[i] < pivot) {
                i++;
                if (i == high) {
                    return i;
                }
            }
            while (A[k] > pivot) {
                k--;
                if (k < low) {
                    int temp = A[low];
                    A[low] = A[high];
                    A[high] = temp;
                    return low;
                }
            }
            if (i < k) {
                int temp = A[i];
                A[i] = A[k];
                A[k] = temp;
            }
            else {
                int temp = A[i];
                A[i] = A[high];
                A[high] = temp;
                return i;
            }
        }
    }
}
