/**
 * 
 */
package devtests;

import org.topicquests.os.asr.spacy.SpacyClientEnvironment;
import org.topicquests.os.asr.spacy.api.ISpacyAgent;

/**
 * @author jackpark
 *
 */
public class TestRoot {
	protected SpacyClientEnvironment environment;
	protected ISpacyAgent agent;

	/**
	 * 
	 */
	public TestRoot() {
		environment = new SpacyClientEnvironment();
		agent = environment.getAgent();
		
	}

}
