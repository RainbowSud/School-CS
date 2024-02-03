package com.company;

import java.io.*;
import java.util.Scanner;

public class hw1_Q6 // Benjamin Swenson
{
	public static void main(String[] args) throws IOException
	{
		final int ARRAY_SIZE = 100;
		int[] A = new int[ARRAY_SIZE];//store the sorted numbers
		int[] B = new int[ARRAY_SIZE];//store the numbers to be searched
		int[] C = new int[ARRAY_SIZE];//hold the search results temporarily
		int n = 0;// the number of elements stored in A
		int m = 0;// the number of elements stored in B
		String dataFile = "hw1_Q6_data.txt"; // the name of the data file, which stores the sorted numbers
		String searchFile = "hw1_Q6_search.txt"; // the name of the search file 
		String outputFile = "hw1_Q6_output.txt"; // the name of the output file 

    	//input all numbers from the data file to the array A in a
		//function input(), which also returns the number of elements
		//of A
		n = input(A, dataFile); 
    
		//input all numbers from the search file to the array B
		m = input(B, searchFile); 

		//for (int i = 0; i< n; i++)
		//	System.out.print(A[i]+" ");
		//System.out.println();


		//print the search results on the screen
		for (int i = 0; i < m; i++)
		{
			C[i] = binarySearch(A, 0, n-1, B[i]); 
			System.out.println("The position of " + B[i] + " is " + C[i]); 
		}

		//output the search results to the output file
		output(C, B, m, outputFile);
	}

	private static int input(int[] A, String fileName) throws IOException
	{
		File myFile = new File(fileName);
		Scanner input = new Scanner(myFile);

		int i = 0;

		while(input.hasNext())
		{
			int value = input.nextInt();
			A[i] = value;
			i++;
		}

		input.close();

		return i;
	}

	private static void output(int[] C, int[] B, int m, String fileName) throws IOException
	{
		PrintWriter output = new PrintWriter(fileName);

		for(int i = 0; i < m; i++)
			output.println("The position of " + B[i] + " is " + C[i]);

		output.close();
	}

	//please complete the following function. x is the search value. If x is in the array, return the index of x in the array; otherwise return -1. 
	private static int binarySearch(int[] array, int low, int high, int x)
	{
		if (low > high){
			return -1;
		}
		int mid = (low + high) / 2;
		if (x == array[mid]){
			return mid;
		}
		if (x < array[mid]) {
			return binarySearch(array, low, mid-1, x);
		}
		if (x > array[mid]){
			return binarySearch(array, mid+1, high, x);
		}
		return 0;
	}
}

