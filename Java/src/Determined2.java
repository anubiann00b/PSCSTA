import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Determined2 {
    
    public static void main(String[] args) throws IOException {
        String problemName = "determined2";
//        BufferedReader reader = new BufferedReader(new FileReader("..\\StudentData\\" + problemName + ".dat"));
        BufferedReader reader = new BufferedReader(new FileReader("H:\\JudgesData\\" + problemName + ".dat"));
        
        int numMatrices = Integer.valueOf(reader.readLine());
        
        for (int i=0;i<numMatrices;i++) {
            String[] firstRow = reader.readLine().split(" ");
            int[][] arr = new int[firstRow.length][firstRow.length];
            for (int j = 0; j < firstRow.length; j++) {
                arr[0][j] = Integer.valueOf(firstRow[j]);
            }
            for (int j = 1; j < firstRow.length; j++) {
                String[] rowString = reader.readLine().split(" ");
                for (int k = 0; k < firstRow.length; k++) {
                    arr[j][k] = Integer.valueOf(rowString[k]);
                }
            }
            
            System.out.println(detMatrix(arr, arr.length));
        }
    }
    static int detMatrix(int[][] arr, int size) {
        if (size == 2)
            return arr[0][0] * arr[1][1] - arr[0][1]*arr[1][0];
        int m = 1;
        int sum = 0;
        for (int col = 0; col < size; col++) {
            sum += m*arr[0][col]*detMatrix(delOne(arr, 0, col), size-1);
            m = -m;
        }
        return sum;
    }
    
    static int[][] delOne(int[][] arr, int delRow, int delCol) {
        int[][] newArr = new int[arr.length-1][arr.length-1];
        
        for (int row = 0; row < delRow; row++) {
            for (int col = 0; col < delCol; col++) {
                newArr[row][col] = arr[row][col];
            }
            for (int col = delCol+1; col < arr.length; col++) {
                newArr[row][col-1] = arr[row][col];
            }
        }
        
        for (int row = delRow+1; row < arr.length; row++) {
            for (int col = 0; col < delCol; col++) {
                newArr[row-1][col] = arr[row][col];
            }
            for (int col = delCol+1; col < arr.length; col++) {
                newArr[row-1][col-1] = arr[row][col];
            }
        }
        return newArr;
    }}
