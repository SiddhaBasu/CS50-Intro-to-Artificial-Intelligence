import java.io.*;
import java.util.*;
// DO NOT IMPORT ANYTHING ELSE
// NO PACKAGE STATMENTS 
// NO OVERRIDE STATMENTS 

public class ComplexSwamp
{
	static int[][] swamp;  // NOW YOU DON'T HAVE PASS THE REF IN/OUT METHODS

 	public static void main(String[] args) throws Exception
	{
		int[] dropInPt = new int[2]; // row and col will be on the 2nd line of input file;
		swamp = loadSwamp( args[0], dropInPt );
		int row=dropInPt[0], col = dropInPt[1];
		String path = ""; // with each step grows to => "[2,3][3,4][3,5][4,6]" etc
		dfs( row, col, path );

	} // END MAIN

 	// JUST FOR YOUR DEBUGGING - DELETE THIS METHOD AND ITS CALL BEFORE HANDIN
	// ----------------------------------------------------------------
	private static void printSwamp(String label, int[][] swamp )
	{
		System.out.println( label );
		System.out.print("   ");
		for(int c = 0; c < swamp.length; c++)
			System.out.print( c + " " ) ;
		System.out.print( "\n   ");
		for(int c = 0; c < swamp.length; c++)
			System.out.print("- ");
		System.out.print( "\n");

		for(int r = 0; r < swamp.length; r++)
		{	System.out.print( r + "| ");
			for(int c = 0; c < swamp[r].length; c++)
				System.out.print( swamp[r][c] + " ");
			System.out.println("|");
		}
		System.out.print( "   ");
		for(int c = 0; c < swamp.length; c++)
			System.out.print("- ");
		System.out.print( "\n");
	}
	// --YOU-- WRITE THIS METHOD 
	// (you may copy from YOURSELF from YOUR lab7 not someone else's)
   	// ----------------------------------------------------------------
	private static int[][] loadSwamp( String infileName, int[] dropInPt  ) throws Exception
	{
		int[][] theSwamp;
		Scanner infile = new Scanner(new File(infileName));
		// open infile with Scanner
		int dimension = infile.nextInt();
		theSwamp = new int[dimension][dimension];

	   dropInPt[0] = infile.nextInt();
	   dropInPt[1] = infile.nextInt();

		for(int r = 0; r < dimension; r++){
			for(int c = 0 ;c < dimension; c++){
				int cell = infile.nextInt();
				theSwamp[r][c] = cell;
			}
		}

		infile.close();
		return theSwamp; // actually must return a loaded swamp grid SEE YOUr OWN LAB#7
	}
	static void dfs(int row, int col, String path) {

		path += "[" + (row) + "," + col + "]";

	
		// Check if we've reached a goal state
		if (row==0 || row==swamp.length-1 || col ==0 || col==swamp.length-1) {
			System.out.println(path);
			swamp[row][col] = 1; // Unmark the cell so other paths can reach it
			return;
		}
	
		// Check the neighbors of the current cell
		if (swamp[row-1][col] == 1) { // Check north neighbor
			swamp[row][col] = -1;
			dfs(row-1, col, path);
			swamp[row][col] = 1;
		}
		if (swamp[row-1][col+1] == 1) { // Check northeast neighbor
			swamp[row][col] = -1;

			dfs(row-1, col+1, path);
			swamp[row][col] = 1;
		}
		if (swamp[row][col+1] == 1) { // Check east neighbor
			swamp[row][col] = -1;

			dfs(row, col+1, path);
			swamp[row][col] = 1;

		}
		if (swamp[row+1][col+1] == 1 ) { // Check southeast neighbor
			swamp[row][col] = -1;
			dfs(row+1, col+1, path);
			swamp[row][col] = 1;
		}
		if (swamp[row+1][col] == 1) { // Check south neighbor
			swamp[row][col] = -1;
			dfs(row+1, col, path );
			swamp[row][col] = 1;
		}
		if (swamp[row+1][col-1] == 1) { // Check southwest neighbor
			swamp[row][col] = -1;
			//System.out.printf("(((%d, %d)))", row, col);
			dfs(row+1, col-1, path );
			swamp[row][col] = 1;
		}
		if (swamp[row][col-1] == 1) { // Check west neighbor
			swamp[row][col] = -1;
			dfs(row, col-1, path );
			swamp[row][col] = 1;
		}
		if (swamp[row-1][col-1] == 1) { // Check northwest neighbor
			swamp[row][col] = -1;

			dfs(row-1, col-1, path );
			swamp[row][col] = 1;
		}

		

		
	
		// Unmark the current cell so other paths can reach it

		
	

	}
	

		// IMPLEMENT THE DFS ALGORITHM IN HERE
	}	
