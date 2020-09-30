/**
 * 
 */
package devtests;

import org.topicquests.support.api.IResult;

import net.minidev.json.JSONObject;

/**
 * @author jackpark
 *
 */
public class FirstTest extends TestRoot {
	private final String
		S1 = "CO2 causes climate change",
		ID1 = "12345";
	/**
	 * 
	 */
	public FirstTest() {
		super();
		JSONObject sentence =  new JSONObject();
		sentence.put("sentenceId", ID1);
		sentence.put("text", S1);
		IResult r = agent.processSentence(sentence);
		System.out.println("A "+r.getErrorString());
		System.out.println("B "+r.getResultObject());
		environment.shutDown();
		System.exit(0);
		
	}

}
