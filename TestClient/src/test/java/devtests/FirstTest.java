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

/**
CODE 200
A 
B {"sentenceId":"12345","text":"CO2 causes climate change","results":{"parse_list":[{"POS_fine":"NNP","POS_coarse":"PROPN","NE":"","lemma":"CO2","word":"CO2"},{"POS_fine":"VBZ","POS_coarse":"VERB","NE":"","lemma":"cause","word":"causes"},{"POS_fine":"NN","POS_coarse":"NOUN","NE":"","lemma":"climate","word":"climate"},{"POS_fine":"NN","POS_coarse":"NOUN","NE":"","lemma":"change","word":"change"}],"len":4,"parse_tree":[{"POS_fine":"VBZ","arc":"ROOT","POS_coarse":"VERB","NE":"","lemma":"cause","modifiers":[{"POS_fine":"NNP","arc":"nsubj","POS_coarse":"PROPN","NE":"","lemma":"CO2","modifiers":[],"word":"CO2"},{"POS_fine":"NN","arc":"dobj","POS_coarse":"NOUN","NE":"","lemma":"change","modifiers":[{"POS_fine":"NN","arc":"compound","POS_coarse":"NOUN","NE":"","lemma":"climate","modifiers":[],"word":"climate"}],"word":"change"}],"word":"causes"}],"noun_phrases":["CO2","climate change"],"tokens":["CO2","causes","climate","change"],"text":"CO2 causes climate change"}}

 */
