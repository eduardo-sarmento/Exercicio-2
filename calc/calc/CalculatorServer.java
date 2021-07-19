import java.rmi.Naming;
import java.rmi.Remote;
import java.rmi.registry.LocateRegistry; 

public class CalculatorServer { 
   public CalculatorServer() { 
      try { 
            System.setProperty("java.rmi.server.hostname", "localhost");
            LocateRegistry.createRegistry(1099);
            Calculator c = new CalculatorImpl();
            Naming.bind("CalculatorService", (Remote) c);

      } catch (Exception e) { 
            System.out.println("Trouble: " + e); 
      }
   } 
   public static void main(String args[]) { 
         new CalculatorServer();
   }
} 
