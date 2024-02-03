package com.company;

import java.io.File;
import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

//the vertex class
class Vertex implements Comparator<Vertex>
{
    int id;//the id of the vertex
    int weight; //the weight of an edge (u,v), where v is the current vertex and v is in the adj list of vertex u
    Vertex next;

    public Vertex() {}

    public Vertex(int id_input, int weight_input)
    {
        id = id_input;
        weight = weight_input;
        next = null;
    }

    @Override
    public int compare(Vertex node1, Vertex node2)
    {
        if (node1.weight < node2.weight)
            return -1;
        if (node1.weight > node2.weight)
            return 1;
        return 0;
    }

}

class Graph
{
    private int[] pre; //the predecessor array
    private int[] dis; //the shortest path distance array

    public PriorityQueue<Vertex> pq;
    public int n;//the number of vertices, the ids of the vertices are from 0 to n-1
    public Vertex[] adj;//adj[i] is the head of the adjacency list of vertex i, for i from 0 to n-1

    //class constructor, initialize the graph by getting the number of vertices from n_input
    public Graph(int n_input)
    {
        n = n_input;
        adj = new Vertex [n];

        pq = new PriorityQueue<>(n, new Vertex());
        //initialize adj[i] to null
        for(int i = 0; i < n; i++)
            adj[i] = null;

        //create the pre and dis arrays
        pre = new int [n];
        dis = new int [n];
    }

    //build the adjacency lists from the adjacency matrix adjM
    public void setAdjLists(int[][] adjM)
    {
        for(int i = 0; i < n; i++)
        {
            //create the i-th adj list adj[i], note that it scans the vertices in the reverse order from n-1 to 0 so that it can
            //construct the adjacent list of each vertex in the increasing index order because a new vertex is always inserted to the front of a list
            for(int j = n-1; j >= 0; j--)
            {
                if(adjM[i][j] > 0)//larger than 0 means there is an edge (i,j)
                {
                    //create a new node and add it to the front of adj[i]
                    Vertex v = new Vertex (j, adjM[i][j]);//the second argument is the weight of the edge (i,j)
                    v.next = adj[i];
                    adj[i] = v;
                }
            }
        }
    }

    //print the adjacency lists of the graph
    public void printAdjLists()
    {
        for(int i = 0; i < n; i++)
        {
            System.out.print("Adj list of vertex " + i + ": ");
            Vertex v = adj[i];
            while(v != null)
            {
                if (v.next != null)
                    System.out.print(v.id + "(" + v.weight + ")" + "->");
                else
                    System.out.print(v.id + "(" + v.weight + ")");
                v = v.next;
            }
            System.out.println();
        }
        System.out.println();
    }

    //get the shortest path distance from the source to vertex i
    public int getSPdis(int i)
    {
        return dis[i];
    }

    //print the shortest path from the source vertex to the destination vertex by using the predecessor array pre[]
    public void printSP(int source, int destination)
    {
        if(destination == source)
            System.out.print(source);
        else
            {
                printSP(source, pre[destination]);
                System.out.print("->" + destination);
            }
    }


    //please complete the following function, which computes shortest paths from the source to all other vertices;
    //as discussed in class, the shortest path information should be stored in the two arrays pre[] and dis[]
    public void Dijkstra(int source) {
        for (int i = 0; i < n; i ++) {
            dis[i] = Integer.MAX_VALUE;
            pre[i] = -1;
        }
        dis[source] = 0;
        pq.add(new Vertex(source, 0));
        for (int i = 0; i < n; i ++) {
            pq.add(new Vertex(i, dis[i]));
        }
        while (!pq.isEmpty()) {
            Vertex vertex = pq.remove();
            int i = vertex.id;
            Vertex v = adj[i];
            while (v != null) {
                if (dis[v.id] > dis[i] + v.weight) {
                    dis[v.id] = dis[i] + v.weight;
                    pre[v.id] = i;
                    pq.add(new Vertex(v.id, dis[v.id]));
                }
                v = v.next;
            }
        }
    }
}

public class hw9_Q2 {
    public static void main(String[] args) throws IOException{
        //open files
        String inputFile = "hw9_Q2_input.txt"; // the name of the input file
        File myFile = new File(inputFile);
        Scanner input = new Scanner(myFile);

        //read the number in the first line, which is the number of vertices of the input graph
        int n;//the number of vertices of the graph
        n = input.nextInt();

        //System.out.println("The number of vertices is: " + n);

        //Next we read the adjacency matrix from the file to an two-dimensional array M
        int[][] M = new int[n][n];
        int i = 0;//row index for M
        int j = 0;//column index for M
        int value;
        while(input.hasNext())
        {
            value = input.nextInt();
            M[i][j] = value;
            j++;
            if(j == n)//j reaches the end of a row
            {
                i++;//start a new row
                j=0;//the column index becomes zero
            }
        }
        input.close();

        //uncomment the following piece of code if you want to check see the adj matrix
     	/*System.out.println("The following is the matrix:");
	    for(i = 0; i < n; i++)
	    {
	        for(j = 0; j < n; j++)
	            System.out.print(M[i][j] + " ");
            System.out.println();
	    }*/

        //initialize the graph by passing n to it
        Graph graph = new Graph(n);

        //construct the adj lists from M by using the method setAdjLists()
        graph.setAdjLists(M);

        //uncomment the following line if you want to print the adj lists along with the edge weights
       // graph.printAdjLists();

        //compute shortest paths with 0 as the source vertex, by calling the method Dijkstra(), which will store the shortest path information in two arrays dis[] and pre[]
        int source = 0;
        graph.Dijkstra(source);

        //after the Dijkstra's algorithm, the following loop is supposed to print the shortest paths from the source vertex to all other vertices
        for(i = 1; i <= n-1; i++)
        {
            System.out.print("The shortest path from the source vertex " + source + " to vertex " + i +": ");
            graph.printSP(source, i);
            System.out.println();
        }

        System.out.println();

        //the following loop is supposed to print the shortest path distances from the source vertex to all other vertices
        for(i = 1; i <= n-1; i++)
        {
            System.out.print("The shortest path distance from the source vertex " + source + " to vertex " + i + " is: ");
            System.out.println(graph.getSPdis(i));
        }
    }
}
