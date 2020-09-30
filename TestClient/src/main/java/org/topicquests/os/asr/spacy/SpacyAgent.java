/**
 * 
 */
package org.topicquests.os.asr.spacy;

import org.topicquests.os.asr.spacy.api.ISpacyAgent;
import org.topicquests.support.ResultPojo;
import org.topicquests.support.api.IResult;

import net.minidev.json.JSONObject;

/**
 * @author jackpark
 *
 */
public class SpacyAgent implements ISpacyAgent {
	private SpacyClientEnvironment environment;
	private HttpClient http;
	private final String
		SERVER,
		PORT,
		URL;

	/**
	 * 
	 */
	public SpacyAgent(SpacyClientEnvironment env, HttpClient cl) {
		environment = env;
		http = cl;
		SERVER = environment.getStringProperty("ServerURl");
		PORT = environment.getStringProperty("ServerPort");
		URL = "http://"+SERVER+":"+Integer.parseInt(PORT)+"/analyze/foo";
	}

	@Override
	public IResult processSentence(JSONObject sentence) {
		IResult result = new ResultPojo();
		String text = sentence.toJSONString();
		//TODO may have to url encode this
		IResult r = http.put(URL, text);
		environment.logDebug("A "+r.getErrorString());
		environment.logDebug("B "+r.getResultObject());
		//TODO convert r to a JSONObject and put it in result
		return result;
	}

}
