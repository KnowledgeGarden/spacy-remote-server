/**
 * 
 */
package org.topicquests.os.asr.spacy.api;

import org.topicquests.support.api.IResult;

import net.minidev.json.JSONObject;

/**
 * @author jackpark
 *
 */
public interface ISpacyAgent {

	/**
	 * <p>Process a given {@code sentence} by sending to the
	 * spacy-remote-client. This will return a much larger 
	 * {@code JSONObject} which includes the results of all
	 * spaCy models applied to the give sentence.</p>
	 * <p>{@code sentence} is of the form:<br/>
	 * 		{ "sentenceId":"<some id>", "text":"<sentence text>" }</p>
	 * @param sentence
	 * @return
	 */
	IResult processSentence(JSONObject sentence);
}
