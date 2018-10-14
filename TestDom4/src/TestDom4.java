/** 
 * http://www.blogjava.net/zzzlyr/articles/314288.html
 */

//import java.io.File;
import java.io.IOException;

//import javax.swing.text.Document;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class TestDom4 {
	public static void parseXml(String fileName) {
		try {
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			DocumentBuilder builder = factory.newDocumentBuilder();
			Document document = builder.parse(fileName);// 获得文档根元素对对象;
			Element root = document.getDocumentElement();// 获得文档根元素下一级子元素所有元素;
			NodeList nodeList = root.getChildNodes();
			System.out.println("Root node name: "+root.getNodeName());
			
			if (null != root) {
				for (int i = 0; i < nodeList.getLength(); i++) {
					System.out.println("Child"+i);
					Node child = nodeList.item(i);// 输出child的属性;
					System.out.println(child);

					if (child.getNodeType() == Node.ELEMENT_NODE) {
						System.out.println("Tag:"+child.getAttributes().getNamedItem(
								"tag").getNodeValue());
					}

					for (Node node = child.getFirstChild(); node != null; node = node.getNextSibling()) {

						if (node.getNodeType() == Node.ELEMENT_NODE) {
							if ("name".equals(node.getNodeName())) {
								System.out.println("Name:"+node.getFirstChild().getNodeValue());
							}
						}//name
						if (node.getNodeType() == Node.ELEMENT_NODE) {
							if ("sex".equals(node.getNodeName())) {
								System.out.println("Sex:"+node.getFirstChild().getNodeValue());
							}
						}//sex
						if (node.getNodeType() == Node.ELEMENT_NODE) {
							if ("age".equals(node.getNodeName())) {
								System.out.println("Age:"+node.getFirstChild()
										.getNodeValue());
							}
						}//age
					}
				}
			}
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (SAXException e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		/*DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		DocumentBuilder builder = factory.newDocumentBuilder();
		try {
			builder = factory.newDocumentBuilder();
			File file=new File("employees.xml");
			Document doc=builder.parse(file);
		} catch (Throwable e) {
			// TODO 自动生成的 catch 块
			e.printStackTrace();
		}*/
		parseXml("employees.xml");
	}

}
