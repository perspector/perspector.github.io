package arr;
public class arrayExampleAnswer
{
   public static void main(String[] args)
   {
    /*** Uncomment the code as you come to it.  It is there to help you. ***/
        /* Step One */
        //Create an array of integers called arrayInt with 10 elements.
        int[] arrayInt = new int[10];
        //Create a String array called arrayString with the following elements.
        //one, two, three, four, five
        String[] arrayString = {"one", "two", "three", "four", "five"};
        //Create a double array called arrayDouble with 15 elements.
        double[] arrayDouble = new double[15];
        
        /* Step Two*/
        // print to the user the length of the arrayString
        System.out.print("arrayString length: ");
        System.out.println(arrayString.length);

        /* Step Three */
        // Fill arrayInt with the even numbers from 0 to 18 using a for loop.
        int count = 0;
       for(int i = 0; i < arrayInt.length; i++)
        {
            arrayInt[i] = count;
            count += 2;
          } 

        //The code below will print out your array.  Make sure you have even numbers 0-18 printed.
        System.out.print("arrayInt contents: ");
        for (int i = 0; i < arrayInt.length; i++)
        {
            System.out.print(arrayInt[i] + " ");
        }
        System.out.println();

        /*Step Four*/
        // Fill arrayDouble with every half number, meaning 0.0, 0.5, 1.0, etc.  till you have all 15 elements filled.
        double countDouble = 0.0;
        for(int i = 0; i < arrayDouble.length; i++)
        {
            arrayDouble[i] = countDouble;
            countDouble += 0.5;
        }

        // print out the array to confirm that you stored the information correctly.
        System.out.print("arrayDouble contents: ");
        for(int i = 0; i < arrayDouble.length; i++)
        {
                System.out.print(arrayDouble[i] + " ");
        }
        System.out.println();
        /* Step Five */
        // Add up all of the elements in the arrayInt and print out their sum. 
        int sum = 0;
        for(int i = 0; i < arrayInt.length; i++)
        {
                sum += arrayInt[i];
        }
        // Average the numbers in arrayInt.  Do not hard code.  Meaning divide by the array length, NOT 10. Type casting?
        double average = 0.0;
        average = (double) sum / arrayInt.length;
        // print out sum
        System.out.println("Sum: " + sum);
        System.out.println("Average: " + average);

        /* Step Six */
         // Add the elements in each array together and print out.
         double countTotal = 0.0;
         double sumDouble = 0.0;
         for(int i = 0; i < arrayDouble.length; i++)
         {
                sumDouble += arrayDouble[i];
         }
         System.out.println("Sum of Double array: " + sumDouble);
         countTotal = sum + sumDouble;
         System.out.println("Sum of Total: " + countTotal);

        /* Step Seven*/
         // Reverse the elements in the arrayDouble.  Your first element should be 7.0 then 6.5 and so on.
         // Hint: you may need a temporary array.
         double[] tempArray = new double[arrayDouble.length];
         int countReverse = 0;
         for(int i = arrayDouble.length - 1; i >= 0; i--)
         {
                 tempArray[countReverse] = arrayDouble[i];
                 countReverse++;
         }
         //print the doubleArray to prove that the Reverse has been stored.
         System.out.print("tempArray contents: ");
         for(int i = 0; i < tempArray.length; i++)
         {
                 System.out.print(tempArray[i] + " ");
         }
         System.out.println();
       }
}