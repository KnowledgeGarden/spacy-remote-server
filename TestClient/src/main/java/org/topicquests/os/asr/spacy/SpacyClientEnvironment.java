/**
 * 
 */
package org.topicquests.os.asr.spacy;

import org.topicquests.os.asr.spacy.api.ISpacyAgent;
import org.topicquests.support.RootEnvironment;

/**
 * @author jackpark
 *
 */
public class SpacyClientEnvironment extends RootEnvironment {
	private HttpClient http;
	private ISpacyAgent agent;
	
	/**
	 */
	public SpacyClientEnvironment() {
		super("config-props.xml", "logger.properties");
		http = new HttpClient(this);
		agent = new SpacyAgent(this, http);
				
	}

	public ISpacyAgent getAgent() {
		return agent;
	}
	
	public HttpClient getHttpClient() {
		return http;
	}
	
	@Override
	public void shutDown() {
		System.out.println("SpacyClientEnvironment.shutDown");

	}

}
