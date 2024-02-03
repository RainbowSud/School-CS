//Benjamin Swenson
package com.company;

import com.sun.source.tree.Tree;

import java.util.Scanner;
import java.io.*;

class TreeNode
{
    public int key;
    public TreeNode left;
    public TreeNode right;

    public TreeNode(int key_input, TreeNode left_input, TreeNode right_input)
    {
        key = key_input;
        left = left_input;
        right = right_input;
    }
}


class BST
{
    private TreeNode root;

    public BST()
    {
        root = null;
    }
    
	//the pre-order traversal of the tree
	public void preOrder() {
        preOrder(root);//call the overloaded function
        System.out.println();
    }

	//the pre-order traversal overloaded function
    private void preOrder(TreeNode v) {
        if(v != null) {
			System.out.print(v.key + " ");
        	preOrder(v.left);
        	preOrder(v.right); 
		}
	}
	
	//the in-order traversal of the tree
	public void inOrder() {
        inOrder(root);//call the overloaded function
        System.out.println();
    }

	//the in-order traversal overloaded function
    private void inOrder(TreeNode v) {
        if(v == null)
            return;
        inOrder(v.left);
        System.out.print(v.key + " ");
        inOrder(v.right);
    }

    //please complete the following function; you can overload it if you want
    public boolean search(int x) {
    	TreeNode v = root;
    	while(v != null && x != v.key) {
    		 if(x < v.key) { // left case
    		 	v = v.left;
			 } else { // right case 
    		 	v = v.right;
			 }
		}
		return v != null;
    }


	//please complete the following function; you can overload it if you want
    public void insert(int x) {
    	if(root == null) { // If no root, new root ez
    		root = new TreeNode(x, null, null);
		}
    	TreeNode v = root;
    	while(x != v.key){
    		if(x < v.key){ // Left case
    			if(v.left == null) {
    				v.left = new TreeNode(x, null, null);
    				return;
				} else {
    				v = v.left;
				}
			} else { // Right case
    			if(v.right == null) {
    				v.right = new TreeNode(x, null, null);
    				return;
				} else {
    				v = v.right;
				}
			}
		}
    }

	//please complete the following function; you can overload it if you want
    public void remove(int x) {
    	root = remove(root, x); //Call overloaded function
    }

    private TreeNode remove(TreeNode v, int x) {
		if(v == null) {
			return v;
		}
		if(x < v.key) { // 1 child left
			v.left = remove(v.left, x);
		} else if(x > v.key) {
			v.right = remove(v.right, x); // 1 child right
		} else { // 2 child
			if(v.left == null) {
				return v.right;
			} else if(v.right == null) {
				return v.left;
			}
			v.key = findMin(v.right);
			v.right = remove(v.right, v.key);
		}
		return v;
	}

	//please complete the following function; you can overload it if you want
	public int findMin(TreeNode v) {
    	int value = v.key;
    	while(v.left != null) {
    		value = v.left.key;
    		v = v.left;
		}
    	return value;
	}

	public TreeNode getRoot() {
		return root; // Made this to get my idea of findMin to work.
	}
}


public class hw3_Q4
{
	public static void main(String[] args) throws IOException
	{

		BST tree = new BST();

		String inputFile = "hw3_Q4_input.txt"; // input file with operations 

  	 	//open the input file
        File myFile = new File(inputFile);
        Scanner input = new Scanner(myFile);

		//read operations from the input file
		String op;
		int x;
		while(input.hasNext())
		{
			Scanner nextLine = new Scanner(input.nextLine());
			op = nextLine.next();

			if (op.equals("insert"))
			{
				x = nextLine.nextInt(); // read the value x for insert
				tree.insert(x);
			}
			if (op.equals("remove"))
			{
				x = nextLine.nextInt(); // read the value x for remove 
				tree.remove(x);
			}
			if (op.equals("search"))
			{
				x = nextLine.nextInt();
				if (tree.search(x) == true)
					System.out.println("The key " + x + " is in the current tree.");
				else// x is not in the tree
					System.out.println("The key " + x + " is not in the current tree.");
			}
			if (op.equals("findMin"))
				System.out.println("The smallest key in the current tree is " + tree.findMin(tree.getRoot()));
		}

		//print the pre-odrder traversal on the console/screen 
		System.out.println("The pre-order traversal list is: ");
		tree.preOrder();

		//print the in-odrder traversal 
		System.out.println("The in-order traversal list is: ");
		tree.inOrder();

		input.close();

	}
}

