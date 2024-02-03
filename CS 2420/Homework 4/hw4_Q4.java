package com.company;
// Benjamin Swenson CS-2420


import jdk.jshell.spi.ExecutionControl;

import javax.swing.tree.TreeNode;
import java.util.Scanner;
import java.io.*;

class AvlNode {
    public int key;
    public AvlNode left;
    public AvlNode right;
    public int height;

    public AvlNode(int key_input)
    {
        key = key_input;
        height = 0;
        left = null;
        right = null;
    }

}

class AvlTree{
    private AvlNode root;
    public AvlTree(){root = null;}

    public void inOrder()
    {
        inOrder(root);
        System.out.println();
    }
    private void inOrder(AvlNode v)
    {
        if(v == null)
            return;
        inOrder(v.left);
        System.out.print(v.key + " ");
        inOrder(v.right);
    }

    public void preOrder()
    {
        preOrder(root);
        System.out.println();
    }
    private void preOrder(AvlNode v)
    {
        if(v == null)
            return;
        System.out.print(v.key + " ");
        preOrder(v.left);
        preOrder(v.right);
    }

    private int getHeight(AvlNode v){
        if(v == null)
            return -1;
        else
            return v.height;
    }

    public void insert(int x) { root = insert(root, x); }

    public void remove(int x) { root = remove(root, x); }
    
    //please complete the following seven functions
    //this function is overloaded
	private AvlNode insert(AvlNode v, int x) {
        if (v == null) {
            return new AvlNode(x);
        }
        if (x == v.key) {
            return v;
        }
        if (x < v.key) {
            v.left = insert(v.left, x);
        }
        else {
            v.right = insert(v.right, x);
        }
        return balance(v);
    }

    //this function is overloaded
    private AvlNode remove(AvlNode v, int x) {
        if (v == null) {
            return null;
        }
        if (x < v.key) {
            v.left = remove(v.left, x);
            return balance(v);
        }
        if (x > v.key) {
            v.right = remove(v.right, x);
            return balance(v);
        }
        if (v.left == null) {
            return v.right;
        }
        if (v.right == null) {
            return v.left;
        }
        AvlNode u = v.right;
        while (u.left != null) {
            u = u.left;
        }
        v.key = u.key;
        v.right = remove(v.right, u.key);
        return balance(v);
    }

    private AvlNode balance(AvlNode v) {
        if (v == null) {
            return null;
        }
        if (getHeight(v.left) - getHeight(v.right) > 1) {
            if (getHeight(v.left.left) >= getHeight(v.left.right)) {
                v = rightRotate(v);
            }
            else {
                v = doubleLeftRightRotate(v);
            }
        }
        if (getHeight(v.right) - getHeight(v.left) > 1) {
            if (getHeight(v.right.right) >= getHeight(v.right.left)) {
                v = leftRotate(v);
            }
            else {
                v = doubleRightLeftRotate(v);
            }
        }
        v.height = 1 + Math.max(getHeight(v.left), getHeight(v.right));
        return v;
    }

    private AvlNode rightRotate (AvlNode v) {
        AvlNode k2 = v;
        AvlNode k1 = v.left;
        k2.left = k1.right;
        k1.right = k2;
        k2.height = 1 + Math.max(getHeight(k2.left), getHeight(k2.right));
        k1.height = 1 + Math.max(getHeight(k1.left), getHeight(k1.right));
        return k1;
    }

    private AvlNode leftRotate (AvlNode v) {
        AvlNode k2 = v;
        AvlNode k1 = v.right;
        k2.right = k1.left;
        k1.left = k2;
        k2.height = 1 + Math.max(getHeight(k2.left), getHeight(k2.right));
        k1.height = 1 + Math.max(getHeight(k1.left), getHeight(k1.right));
        return k1;
    }

    private AvlNode doubleLeftRightRotate (AvlNode v) {
        v.left = leftRotate(v.left);
        return rightRotate(v);
    }

    private AvlNode doubleRightLeftRotate (AvlNode v) {
        v.right = rightRotate(v.right);
        return leftRotate(v);
    }
}

public class hw4_Q4 {
    public static void main(String[] args) throws IOException
    {

        AvlTree tree = new AvlTree();

        String inputFile = "hw4_Q4_input.txt"; // input file with operations

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
