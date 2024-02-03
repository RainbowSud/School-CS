//Benjamin Swenson - CS 2420
package com.company;

import java.io.*;
import java.util.NoSuchElementException;
import java.util.Scanner;

class ListNode
{
    int value;
    ListNode next;

    //class constructor
    ListNode (int input_value, ListNode input_next)
    {
        value = input_value;
        next = input_next;
    }
}

class Queue
{
	private ListNode front, rear;

    public Queue()
    {
        front = null;
        rear = null;
    }

    //please complete the following function
    public void enqueue(int x) {
        ListNode value = new ListNode(x, null);
        if (front == null) {
            front = value;
            rear = value;
        } if (front == rear) {
            front.next = value;
            rear = value;
        }
        rear.next = value;
        rear = value;

    }

    //please complete the following function
    public int dequeue() {
        int value = front.value;
        if (rear == front) {
            rear = null;
        }
        front = front.next;
        return value;
    }
	
	//check whether the queue is empty
	public boolean isEmpty()
    {
        if(front == null)
            return true;
        else
            return false;
    }

}

public class hw2_Q2
{
	public static void main(String[] args) throws IOException
	{ 
		final int ARRAY_SIZE = 100; 
		int[] A = new int[ARRAY_SIZE];//store numbers for doing enqueue operations 
		int n = 0;//the number of elements that will be stored in A
		String inputFile1 = "hw2_Q2_input.txt"; // file with input data for enqueue

		n = input(A, inputFile1); 

		Queue queue = new Queue();

		//perform enqueue operations
		for (int i = 0; i < n; i++)
			queue.enqueue(A[i]);

		//perform ten dequeue operations
		for (int i = 0; i < 10; i++)
		{
			//perform dequeue operation if queue is not empty
			if(queue.isEmpty() == false)
			{
				int x = queue.dequeue();
				System.out.print(x + " ");
			}
		}
		System.out.println();
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
}
