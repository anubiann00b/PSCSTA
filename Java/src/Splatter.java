import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Splatter {
    
    public static void main(String[] args) throws IOException {
        String problemName = "splatter";
//        BufferedReader reader = new BufferedReader(new FileReader("..\\StudentData\\" + problemName + ".dat"));
        BufferedReader reader = new BufferedReader(new FileReader("H:\\JudgesData\\" + problemName + ".dat"));
        
        int numSets = Integer.valueOf(reader.readLine());
        
        for (int i=0;i<numSets;i++) {
            String[] dims = reader.readLine().split(" ");
            boolean[][] arr = new boolean[Integer.valueOf(dims[0])][Integer.valueOf(dims[1])];
            int loops = Integer.valueOf(reader.readLine());
            for (int j=0;j<loops;j++) {
                String[] coords = reader.readLine().split(" ");
                int x = Integer.valueOf(coords[0]);
                int y = Integer.valueOf(coords[1]);
                
                fillArr(arr, x,y);
                fillArr(arr, x+1,y);
                fillArr(arr, x,y+1);
                fillArr(arr, x-1,y);
                fillArr(arr, x,y-1);
                fillArr(arr, x+1,y+1);
                fillArr(arr, x-1,y-1);
                fillArr(arr, x+1,y-1);
                fillArr(arr, x-1,y+1);
                
                fillArr(arr, x+2,y);
                fillArr(arr, x-2,y);
                fillArr(arr, x,y+2);
                fillArr(arr, x,y-2);
            }
            
            boolean good = true;
            for (boolean[] arr1 : arr)
                for (boolean b : arr1)
                    if (!b)
                        good = false;
            System.out.println(good?"YES":"NO");
        }
    }
    
    static void fillArr(boolean[][] arr, int x, int y) {
        try {
            arr[x][y] = true;
        } catch (ArrayIndexOutOfBoundsException e) {
        }
    }
}
