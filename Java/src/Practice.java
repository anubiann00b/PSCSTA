import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Practice {
    
    public static void main(String[] args) throws IOException {
        String problemName = "practiceproblem";
//        BufferedReader reader = new BufferedReader(new FileReader("..\\StudentData\\" + problemName + ".dat"));
        BufferedReader reader = new BufferedReader(new FileReader("H:\\JudgesData\\" + problemName + ".dat"));
        
        int numLines = Integer.valueOf(reader.readLine());
        
        for (int i = 0; i < numLines; i++) {
            System.out.println("Let's play " + reader.readLine() + "!");
        }
    }
}
