/**
 * A program to carry on conversations with a human user.
 * This is the initial version that:  
 * <ul><li>
 *       Uses indexOf to find strings
 * </li><li>
 * 		    Handles responding to simple words and phrases 
 * </li></ul>
 * This version uses a nested if to handle default responses.
 * @author Mrs. Miller
 * @version March 2024
 */
public class Magpie
{
	/**
	 * Get a default greeting 	
	 * @return a greeting
	 */
	public String getGreeting()
	{
		return "Hello, let's talk.";
	}
	



	private int findKeyword(String statement, String goal, int startPos)
	{
		String phrase = statement.trim();
		int psn = phrase.toLowerCase().indexOf(goal.toLowerCase(), startPos);
		while (psn >= 0)
		{
			String before = " ", after = " ";
			if (psn > 0)
			{
				before = phrase.substring (psn - 1, psn).toLowerCase();
			}
			if (psn + goal.length() < phrase.length())
			{
				after = phrase.substring(psn + goal.length(), psn + goal.length() + 1).toLowerCase();
			}
			/* determine the values of psn, before, and after at this point in the method. */
			if (((before.compareTo ("a") < 0 ) || (before.compareTo("z") > 0)) && ((after.compareTo ("a") < 0 ) || (after.compareTo("z") > 0)))
			{
				return psn;
			}
			psn = phrase.indexOf(goal.toLowerCase(), psn + 1);
		}
		return -1;
	}





	/**
	 * Gives a response to a user statement
	 * 
	 * @param statement
	 *            the user statement
	 * @return a response based on the rules given
	 */
	public String getResponse(String statement)
	{
		String response = "";
		if (statement.indexOf("no") >= 0)
		{
			response = "Why so negative?";
		}
		else if (statement.indexOf("mother") >= 0
				|| statement.indexOf("father") >= 0
				|| statement.indexOf("sister") >= 0
				|| statement.indexOf("brother") >= 0)
		{
			response = "Tell me more about your family.";
		}
		else if (statement.indexOf("cat") >= 0
			&& statement.indexOf("dog") >= 0)
		{
			response = "That's a lot of pets! Can you tell me more?";
		}
		else if (statement.indexOf("cat") >= 0
			|| statement.indexOf("dog") >= 0)
		{
			response = "Tell me more about your pets.";
		}
		else if (statement.indexOf("Mrs. Miller") >= 0
			|| statement.indexOf("Mrs. Zienty") >= 0
			|| statement.indexOf("Mrs. Gallo") >= 0
			|| statement.indexOf("Mrs. Sangwan") >= 0)
		{
			response = "She sounds like a fantastic teacher!";
		}
		else if (statement.trim().length() == 0)
		{
			response = "Say something, please.";
		}
		else if (statement.indexOf("code") >= 0
			|| statement.indexOf("computer") >= 0)
		{
			response = "Computers are cool! What is your IP?";
		}
		else if (statement.indexOf("bye") >= 0
			|| statement.indexOf("see you later") >= 0)
		{
			response = "Goodbye.";
		}
		else if (statement.indexOf("magpie") >= 0
			|| statement.indexOf("you") >= 0)
		{
			response = "I am Magpie, a simple chatbot that has preprogrammed responses to common keywords.\nAs I am open source, you are welcome to look at my code!";
		}
		else if (statement.indexOf("test") >= 0)
		{
			response = "";
			System.out.println(findKeyword("She's my sister", "sister", 0)); 
			System.out.println(findKeyword("Brother Tom is helpful", "brother", 0)); 
			System.out.println(findKeyword("I can't catch wild cats.", "cat", 0)); 
			System.out.println(findKeyword("I know nothing about snow plows.", "no", 0)); 

			int numFound = findKeyword("I know nothing about snow plows.", "no", 0);
			System.out.print(numFound);
		}




		else
		{
			response = getRandomResponse();
		}
		return response;
	}

	/**
	 * Pick a default response to use if nothing else fits.
	 * @return a non-committal string
	 */
	private String getRandomResponse()
	{
		final int NUMBER_OF_RESPONSES = 7;
		double r = Math.random();
		int whichResponse = (int)(r * NUMBER_OF_RESPONSES);
		String response = "";
		
		if (whichResponse == 0)
		{
			response = "Interesting, tell me more.";
		}
		else if (whichResponse == 1)
		{
			response = "Hmmm.";
		}
		else if (whichResponse == 2)
		{
			response = "Do you really think so?";
		}
		else if (whichResponse == 3)
		{
			response = "You don't say.";
		}
		else if (whichResponse == 4)
		{
			response = "42.";
		}
		else if (whichResponse == 5)
		{
			response = "Honestly, I do not know much about this topic.";
		}
		else if (whichResponse == 6)
		{
			response = "So it has come to this...";
		}

		return response;
	}
}
