/**
 * 
 */
package devtests;

/**
 * @author jackpark
 *
 */
public class BootTest extends TestRoot {

	/**
	 * 
	 */
	public BootTest() {
		super();
		
		System.out.println("A "+environment.getProperties());
		environment.shutDown();
		System.exit(0);
	}

}
