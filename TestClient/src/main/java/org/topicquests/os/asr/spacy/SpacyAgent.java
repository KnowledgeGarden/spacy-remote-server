/**
 * 
 */
package org.topicquests.os.asr.spacy;

import java.util.ArrayList;
import java.util.List;

import org.topicquests.os.asr.spacy.api.ISpacyAgent;
import org.topicquests.support.ResultPojo;
import org.topicquests.support.api.IResult;

import net.minidev.json.JSONObject;
import net.minidev.json.parser.JSONParser;

/**
 * @author jackpark
 *
 */
public class SpacyAgent implements ISpacyAgent {
	private SpacyClientEnvironment environment;
	private HttpClient http;
	private final List<String> models;
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
		models = new ArrayList<String>();
		models.add("en_ner_jnlpba_md");
		models.add("en_ner_bc5cdr_md");
		models.add("en_ner_bionlp13cg_md");
		models.add("en_ner_craft_md");
		models.add("en_core_web_lg");
		models.add("en_core_sci_lg");
		SERVER = environment.getStringProperty("ServerURl");
		PORT = environment.getStringProperty("ServerPort");
		URL = "http://"+SERVER+":"+Integer.parseInt(PORT)+"/all";
	}

	@Override
	public IResult processSentence(JSONObject sentence) {


		sentence.put("models", models);

		IResult result = new ResultPojo();
		result.setResultObject(sentence);
		String text = sentence.toJSONString();
		//TODO may have to url encode this
		IResult r = http.put(URL, text);
		//environment.logDebug("A "+r.getErrorString());
		//environment.logDebug("B "+r.getResultObject());
		String json = (String)r.getResultObject();
		
		if (json != null) {
			try {
				JSONParser p = new JSONParser(JSONParser.MODE_JSON_SIMPLE);
				JSONObject jo = (JSONObject)p.parse(json);
				sentence.put("results", jo);
				sentence.remove("models");

			} catch (Exception e) {
				e.printStackTrace();
				result.addErrorString(e.getLocalizedMessage());
				environment.logError(e.getLocalizedMessage(), e);
			}
		}
		return result;
	}

}
